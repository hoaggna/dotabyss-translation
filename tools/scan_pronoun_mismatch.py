#!/usr/bin/env python3
"""
Scan phát hiện các câu nghi ngờ nhầm ngôi xưng hô trong hmr_*/en.json.

Logic phân vai dựa trên key tiếng Nhật:
- Nữ nói: わたし, あたし, ボク(một số nhân vật), ～ですぅ, 司令官殿, 旦那様, ご主人様
- Nam nói: 俺, お前, ～だろ, ～ぞ, きみ(em)
- Narration: câu miêu tả không có marker rõ

Phát hiện mâu thuẫn:
- Key có marker NỮ nhưng value dùng "Anh thích/yêu em" (nam nói)
- Key có marker NAM nhưng value dùng "Em thích/yêu anh" (nữ nói)
- Key nữ nói nhưng value xưng "tôi" + gọi đối phương "cô ấy/cô"

Cách dùng:
    py tools/scan_pronoun_mismatch.py                    # Scan tất cả
    py tools/scan_pronoun_mismatch.py --folder hmr_10160100032  # 1 folder
    py tools/scan_pronoun_mismatch.py --save             # Lưu report JSON
"""

import os
import json
import re
import glob
import argparse
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
NOVELS_DIR = ROOT_DIR / "translations" / "novels"

# ─── Markers phân vai ────────────────────────────────────────────────────────

FEMALE_SPEAKER = re.compile(
    r'(わたし|あたし|私[、。！]|'
    r'司令官殿|司令官様|司令官さん|司令官くん|'
    r'旦那様|旦那さま|ご主人様|ご主人さま|'
    r'ですぅ|ますぅ|ですか[？?]|ませんか|'
    r'してください|お願い|ありがとう|'
    r'よぉ[～♡]|のぉ[～♡]|ねぇ[～♡]|わぁ[～♡]|'
    r'ですわ|かしら|だもん|なのぉ|'
    # Moaning / thán từ rên = NỮ
    r'んっ.*♡|あぁっ.*♡|はぁっ.*♡|ひぅっ|ふぁっ|'
    r'イク|イグ|イッちゃ|'
    # ♡ trong câu = hầu như luôn là nữ nói
    r'♡|'
    # Gọi MC bằng tên thân mật (nữ)
    r'兄さん|おにーさん|お兄さん|お兄ちゃん)'
)

MALE_SPEAKER = re.compile(
    r'(俺[はがのもを、。]|僕[はがのもを]|'
    r'お前[はがのもを]|'
    r'だろ[？?。]|ぞ[。！]|ぜ[。！]|'
    r'てくれ[。！]|しろ[。！]|'
    r'きみ[がはのを])'
)

NARRATION = re.compile(
    r'^[^「」（）]*$'  # Không có dấu ngoặc thoại → miêu tả
)

# ─── Mismatch patterns ───────────────────────────────────────────────────────

# Nữ nói nhưng value giống nam nói
FEMALE_BUT_MALE_VALUE = [
    re.compile(r'\bAnh (?:thích|yêu) em\b', re.I),
    re.compile(r'\bAnh sẽ\b.*\bcho em\b', re.I),
    re.compile(r'\bAnh muốn\b.*\bem\b', re.I),
    re.compile(r'\bcủa anh\b.*\bvào (?:trong|sâu)\b', re.I),  # "thanh thịt của anh vào trong"
    re.compile(r'\bĐể anh\b', re.I),
    re.compile(r'\bAnh đã\b.*\bvào em\b', re.I),
]

# Nam nói nhưng value giống nữ nói
MALE_BUT_FEMALE_VALUE = [
    re.compile(r'\bEm (?:thích|yêu) anh\b', re.I),
    re.compile(r'\bEm muốn\b.*\banh\b', re.I),
    re.compile(r'\bEm sắp\b.*\blên đỉnh\b', re.I),
    re.compile(r'\bTư lệnh ơi\b', re.I),
    re.compile(r'\bChủ nhân ơi\b', re.I),
]

# Nữ nói nhưng value dùng "cô ấy" (đang nói về chính mình?)
FEMALE_BUT_THIRD_PERSON = [
    re.compile(r'\bcô ấy (?:rên|thở|run|giật|lên đỉnh|ra)\b', re.I),
    re.compile(r'\bcơ thể cô ấy\b', re.I),
    re.compile(r'\bâm đạo cô ấy\b', re.I),
]

# Narration nhưng value dùng "tôi" như nữ tự thuật (nghi nhầm)
NARR_BUT_FIRST_PERSON_FEMALE = [
    re.compile(r'\btôi (?:rên|thở dốc|lên đỉnh|ra rồi|sướng)\b', re.I),
]


def detect_speaker(key: str) -> str:
    """Phát hiện người nói từ key JP. Return 'female', 'male', 'narration', 'unknown'."""
    is_female = bool(FEMALE_SPEAKER.search(key))
    is_male = bool(MALE_SPEAKER.search(key))

    # ♡ hoặc moaning = nữ (ưu tiên cao nhất trong hmr_ context)
    if '♡' in key or re.search(r'[んはあひふ][ぁぅっ]', key):
        return 'female'

    if is_female and not is_male:
        return 'female'
    if is_male and not is_female:
        return 'male'
    if is_female and is_male:
        # Cả 2 marker → ưu tiên female trong hmr_ (H-scene, nữ nói nhiều hơn)
        return 'female'

    # Câu miêu tả (narration)
    if re.search(r'(した|ている|であった|のだった|始める|感じる|思う)', key):
        if not re.search(r'[！？♡～]', key):
            return 'narration'

    return 'unknown'


def check_mismatch(key: str, value: str, speaker: str) -> list:
    """Kiểm tra mâu thuẫn ngôi xưng. Trả về danh sách vấn đề."""
    issues = []

    if speaker == 'female':
        for pat in FEMALE_BUT_MALE_VALUE:
            if pat.search(value):
                issues.append(f"female_says_male_line: {pat.pattern}")
                break
        for pat in FEMALE_BUT_THIRD_PERSON:
            if pat.search(value):
                issues.append(f"female_referred_as_third_person: {pat.pattern}")
                break

    elif speaker == 'male':
        for pat in MALE_BUT_FEMALE_VALUE:
            if pat.search(value):
                issues.append(f"male_says_female_line: {pat.pattern}")
                break

    elif speaker == 'narration':
        for pat in NARR_BUT_FIRST_PERSON_FEMALE:
            if pat.search(value):
                issues.append(f"narration_but_first_person: {pat.pattern}")
                break

    return issues


def main():
    parser = argparse.ArgumentParser(description="Scan nhầm ngôi xưng hô trong hmr_*")
    parser.add_argument("--folder", type=str, default=None)
    parser.add_argument("--save", action="store_true", help="Lưu report JSON")
    args = parser.parse_args()

    if args.folder:
        folders = [NOVELS_DIR / args.folder]
    else:
        folders = sorted(NOVELS_DIR.glob("hmr_*"))

    print("=" * 70)
    print("  SCAN PRONOUN MISMATCH — Phát hiện nhầm ngôi xưng hô")
    print("=" * 70)
    print(f"\n📂 Scanning {len(folders)} folders...\n")

    all_issues = []
    total_scanned = 0

    for folder in folders:
        en_path = folder / "en.json"
        if not en_path.exists():
            continue

        try:
            with open(en_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            continue

        for key, value in data.items():
            if not value:
                continue
            total_scanned += 1

            speaker = detect_speaker(key)
            if speaker == 'unknown':
                continue

            issues = check_mismatch(key, value, speaker)
            if issues:
                all_issues.append({
                    "folder": folder.name,
                    "speaker": speaker,
                    "key": key[:80],
                    "value": value[:80],
                    "issues": issues,
                })

    # ─── Report ──────────────────────────────────────────────────────────
    print(f"{'─'*70}")
    print(f"  📊 Scanned: {total_scanned} entries")
    print(f"  ⚠️  Nghi nhầm ngôi: {len(all_issues)} entries")
    print(f"{'─'*70}")

    if all_issues:
        # Group by issue type
        by_type = {}
        for item in all_issues:
            for iss in item["issues"]:
                category = iss.split(":")[0]
                by_type.setdefault(category, []).append(item)

        print(f"\n  Phân loại:")
        for cat, items in sorted(by_type.items(), key=lambda x: -len(x[1])):
            print(f"    • {cat}: {len(items)} entries")

        print(f"\n  Mẫu (20 đầu tiên):")
        for item in all_issues[:20]:
            print(f"\n    📁 {item['folder']} [{item['speaker']}]")
            print(f"    JP: {item['key']}...")
            print(f"    VI: {item['value']}...")
            print(f"    ⚠️  {item['issues']}")

    if args.save and all_issues:
        report_path = ROOT_DIR / "reports" / "pronoun_mismatch_report.json"
        report_path.parent.mkdir(exist_ok=True)
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(all_issues, f, ensure_ascii=False, indent=2)
        print(f"\n💾 Saved: {report_path}")

    print(f"\n{'='*70}")


if __name__ == "__main__":
    main()
