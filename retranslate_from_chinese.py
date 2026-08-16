#!/usr/bin/env python3
"""
Dịch lại hmr_* từ bản tiếng Trung (extracted_hmr/*.md) → tiếng Việt.
Chiến lược: ZH → VI cho chất lượng tốt hơn JP → VI trực tiếp.

Cách dùng:
    py retranslate_from_chinese.py                    # Dịch tất cả
    py retranslate_from_chinese.py --dry-run          # Chỉ báo cáo
    py retranslate_from_chinese.py --folder hmr_10010100011  # Chỉ 1 folder
    py retranslate_from_chinese.py --workers 10       # Số thread
"""

import os
import sys
import json
import re
import glob
import time
import argparse
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOVELS_DIR = os.path.join(BASE_DIR, "translations", "novels")
EXTRACTED_DIR = r"D:\dotabyss-translation\extracted_hmr"

MAX_LINE_LEN = 76

# ─── Parse extracted_hmr/*.md ─────────────────────────────────────────────────

def parse_extracted_md(md_path: str) -> dict:
    """Parse 1 file .md → {folder_name: {jp_key: zh_value}}"""
    result = {}
    current_folder = None

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tìm tất cả các block ### hmr_XXXXX (suffix: NN)
    # Theo sau là ```json ... ```
    pattern = re.compile(
        r'### (hmr_\d+)\s*\(suffix:\s*\d+\)\s*\n+```json\n(.*?)```',
        re.DOTALL
    )

    for match in pattern.finditer(content):
        folder_name = match.group(1)
        json_block = match.group(2).strip()
        try:
            data = json.loads(json_block)
            result[folder_name] = data
        except json.JSONDecodeError:
            # Thử fix JSON không hoàn chỉnh (thiếu } cuối)
            try:
                if not json_block.rstrip().endswith('}'):
                    # Tìm dấu } cuối cùng
                    last_brace = json_block.rfind('}')
                    if last_brace > 0:
                        json_block = json_block[:last_brace + 1]
                data = json.loads(json_block)
                result[folder_name] = data
            except Exception:
                print(f"  ⚠️  Lỗi parse JSON cho {folder_name} trong {md_path}")

    return result


def load_all_chinese_data() -> dict:
    """Load tất cả bản dịch ZH từ extracted_hmr/*.md → {folder: {jp: zh}}"""
    all_data = {}
    md_files = sorted(glob.glob(os.path.join(EXTRACTED_DIR, "hmr_translations_*.md")))

    print(f"📖 Đang đọc {len(md_files)} file extracted_hmr/*.md...")

    for md_path in md_files:
        parsed = parse_extracted_md(md_path)
        all_data.update(parsed)

    print(f"   → Tìm thấy {len(all_data)} folders có bản ZH")
    return all_data


# ─── Google Translate ZH → VI ─────────────────────────────────────────────────

def translate_zh_to_vi(text: str) -> str:
    """Dịch 1 câu ZH → VI qua Google Translate."""
    if not text or not text.strip():
        return text

    # Bảo vệ tags
    protected = {}
    counter = [0]

    def protect(m):
        key = f"§{counter[0]}§"
        protected[key] = m.group(0)
        counter[0] += 1
        return key

    text_safe = re.sub(r'<[^>]+>', protect, text)

    url = (
        "https://translate.googleapis.com/translate_a/single"
        "?client=gtx&sl=zh-CN&tl=vi&dt=t&q="
        + urllib.parse.quote(text_safe)
    )
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            data = json.loads(res.read().decode('utf-8'))
            sentences = data[0]
            result = ''.join([s[0] for s in sentences if s[0]])
    except Exception:
        return text

    # Khôi phục tags
    for key, val in protected.items():
        result = result.replace(key, val)

    return result


# ─── Polish (giống fix_hmr_pipeline) ─────────────────────────────────────────

POLISH_TERMS = [
    # Xưng hô
    (re.compile(r'\bchỉ huy\b', re.I), 'Tư lệnh'),
    (re.compile(r'\bChỉ huy\b'), 'Tư lệnh'),
    (re.compile(r'\bTổng tư lệnh\b'), 'Tư lệnh'),
    (re.compile(r'\bnhà chứa\b', re.I), 'kỹ viện'),
    (re.compile(r'\bnhà thổ\b', re.I), 'kỹ viện'),
    (re.compile(r'\bgái điếm\b', re.I), 'kỹ nữ'),
    (re.compile(r'\bgái mại dâm\b', re.I), 'kỹ nữ'),
    (re.compile(r'\bkhách hàng\b', re.I), 'vị khách'),
    # H-scene
    (re.compile(r'\bcon gà trống\b', re.I), 'dương vật'),
    (re.compile(r'\bgà trống\b', re.I), 'dương vật'),
    (re.compile(r'\bcặc\b', re.I), 'dương vật'),
    (re.compile(r'\bxuất tinh\b(?!\s*(?:vào|trong))', re.I), 'lên đỉnh'),  # nữ
    (re.compile(r'\bquan hệ tình dục\b', re.I), 'làm chuyện ấy'),
    # Tên nhân vật (ZH → Romaji)
    (re.compile(r'\bLa Sha\b', re.I), 'Rosa'),
    (re.compile(r'\bLuó shā\b', re.I), 'Rosa'),
    (re.compile(r'\b罗莎\b'), 'Rosa'),
    (re.compile(r'\b贝莉莎\b'), 'Belisa'),
    (re.compile(r'\b艾蕾克特拉\b'), 'Electra'),
    (re.compile(r'\b琴音\b'), 'Kotono'),
    (re.compile(r'\b玛丽娜\b'), 'Marina'),
    (re.compile(r'\b露蒂亚\b'), 'Rudia'),
]

PUNCT_MARKS = (',', '.', '!', '?', '…', '~', '♪', '♡', ':', ';', ')', '～')


def condense_and_br(key: str, value: str) -> str:
    """Đặt <br> thông minh, max 76 ký tự/segment."""
    v_clean = re.sub(r'\s*<br\s*/?>\s*', ' ', value)
    v_clean = re.sub(r'\s{2,}', ' ', v_clean).strip()

    br_in_key = key.count('<br>')

    if len(v_clean) <= MAX_LINE_LEN and br_in_key == 0:
        return v_clean

    if len(v_clean) <= 20:
        return v_clean

    # Chia 2 dòng
    mid = len(v_clean) // 2
    best_idx = -1
    best_score = float('inf')

    for match in re.finditer(
        r'([,;.!?…～♡♪]|\bkhi\b|\bvà\b|\brồi\b|\bthì\b|\bnhưng\b|\bmà\b|\bnên\b)',
        v_clean
    ):
        idx = match.end()
        p1 = len(v_clean[:idx].strip())
        p2 = len(v_clean[idx:].strip())
        if p1 > MAX_LINE_LEN or p2 > MAX_LINE_LEN:
            continue
        if p1 < 5 or p2 < 5:
            continue
        score = abs(idx - mid)
        if match.group(0) in ',.!?…～;♡♪':
            score -= 8
        if score < best_score:
            best_score = score
            best_idx = idx

    if best_idx != -1:
        return v_clean[:best_idx].rstrip() + '<br>' + v_clean[best_idx:].lstrip()

    # Fallback
    spaces = [m.start() for m in re.finditer(r'\s+', v_clean)]
    valid = [(abs(s - mid), s) for s in spaces
             if len(v_clean[:s]) <= MAX_LINE_LEN and len(v_clean[s+1:]) <= MAX_LINE_LEN]
    if valid:
        valid.sort()
        return v_clean[:valid[0][1]] + '<br>' + v_clean[valid[0][1]:].lstrip()

    return v_clean


def polish(key: str, value: str) -> str:
    """Polish bản dịch VI."""
    for pat, rep in POLISH_TERMS:
        value = pat.sub(rep, value)

    # Bảo toàn ()
    if ('（' in key or key.startswith('(')) and not ('(' in value or '（' in value):
        value = f"({value})"

    # Bảo toàn <user>
    if '<user>' in key and '<user>' not in value:
        value = re.sub(r'\b(Tư lệnh|người chơi|Chủ nhân)\b', '<user>', value, count=1)

    # Giới hạn ký tự lặp
    def fix_reps(m):
        c = m.group(1)
        if c in '.…': return '……'
        elif c in '!！': return '!'
        elif c in '?？': return '?'
        elif c in '~～': return '~~~~'
        else: return c * 3
    value = re.sub(r'(.)\1{4,}', fix_reps, value)

    # Condense + <br>
    value = condense_and_br(key, value)

    return value.strip()


# ─── Main ────────────────────────────────────────────────────────────────────

def process_folder(folder_name: str, zh_data: dict, workers: int) -> int:
    """Dịch 1 folder từ ZH → VI."""
    en_path = os.path.join(NOVELS_DIR, folder_name, "en.json")
    if not os.path.exists(en_path):
        return 0

    with open(en_path, 'r', encoding='utf-8') as f:
        current_data = json.load(f)

    # zh_data = {jp_key: zh_value}
    items_to_translate = []
    for jp_key, zh_value in zh_data.items():
        if jp_key in current_data and zh_value:
            items_to_translate.append((jp_key, zh_value))

    if not items_to_translate:
        return 0

    def translate_item(item):
        jp_key, zh_value = item
        vi_raw = translate_zh_to_vi(zh_value)
        vi_polished = polish(jp_key, vi_raw)
        return jp_key, vi_polished

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(translate_item, items_to_translate))

    # Merge
    for jp_key, vi_value in results:
        if vi_value:
            current_data[jp_key] = vi_value

    with open(en_path, 'w', encoding='utf-8') as f:
        json.dump(current_data, f, ensure_ascii=False, indent=4)

    return len(results)


def main():
    parser = argparse.ArgumentParser(
        description="Dịch lại hmr_* từ bản Trung (ZH → VI) cho chất lượng cao hơn"
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--folder", type=str, default=None)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    print("=" * 70)
    print("  RETRANSLATE FROM CHINESE (ZH → VI)")
    print("  Nguồn: extracted_hmr/*.md → Google Translate ZH→VI → Polish")
    print("=" * 70)

    # Load bản ZH
    zh_all = load_all_chinese_data()
    if not zh_all:
        print("❌ Không tìm thấy dữ liệu ZH trong extracted_hmr/")
        return

    # Xác định folders cần xử lý
    if args.folder:
        if args.folder in zh_all:
            folders_to_process = {args.folder: zh_all[args.folder]}
        else:
            print(f"❌ Folder {args.folder} không có trong bản ZH")
            return
    else:
        folders_to_process = zh_all

    print(f"\n📂 Sẽ dịch lại {len(folders_to_process)} folders")

    if args.dry_run:
        total_entries = sum(len(v) for v in folders_to_process.values())
        print(f"   Tổng: {total_entries} entries")
        print(f"\n[DRY RUN] Không dịch.")
        return

    # Dịch
    start_time = time.time()
    total_translated = 0
    total_folders = len(folders_to_process)

    for idx, (folder_name, zh_data) in enumerate(sorted(folders_to_process.items()), 1):
        print(f"  [{idx}/{total_folders}] {folder_name} ({len(zh_data)} entries)...",
              end="", flush=True)
        count = process_folder(folder_name, zh_data, args.workers)
        print(f" ✅ {count}")
        total_translated += count
        time.sleep(0.3)  # nhẹ rate limit

    elapsed = time.time() - start_time

    print(f"\n{'='*70}")
    print(f"  HOÀN TẤT!")
    print(f"  ✅ Entries dịch : {total_translated}")
    print(f"  📁 Folders      : {total_folders}")
    print(f"  ⏱️  Thời gian   : {elapsed:.1f}s")
    print(f"{'='*70}")
    print(f"\n💡 Tiếp theo: py fix_hmr_pipeline.py")


if __name__ == "__main__":
    main()
