#!/usr/bin/env python3
"""
fix_hmr_translations.py — Script kiểm tra và sửa các lỗi dịch máy CHUYÊN BIỆT cho các folder novel hmr_*.

Các lỗi được xử lý:
1. 旦那様 / 旦那さま / ご主人様 / ご主人さま (Master / Dannasama) dịch sai thành "chồng", "chồng bạn", "chồng anh", "chồng mình", "thưa ngài", "ông xã", "Chủ nhân điện hạ"... -> sửa thành "Chủ nhân".
2. え！？, え？, え…… thán từ bị dịch máy thành "hình ảnh! ?", "hình ảnh?", "bức tranh"... -> giữ nguyên Romaji (Eh!?, Eh?, Eh……).
3. ん？ ở đầu câu bị dịch thành "vâng?" -> đổi thành "Hm?" / "Hửm?".
4. おにーさん / お兄さん (Oni-san khi không cùng huyết thống) dịch sai thành "onii", "Tekaonii", "một onii", "anh trai tôi" -> chuẩn hóa thành "Oni-san".
5. Thoại rên rỉ / lên đỉnh của nữ (イク, イグ, イっちゃう) bị dịch sai thành "bắn tinh", "Iguno" -> sửa thành "ra", "ra đây", "lên đỉnh", v.v.
6. らめ / らめぇ (dame) bị dịch thành "Rame", "Rameee" -> "K-Không được", "Đừng mà".
7. Thuật ngữ H-scene / VN theo TRANSLATION_RULES.md:
   - "nước ép tình yêu" -> "dâm dịch"
   - "con thanh thịt" / "gà trống" -> "thanh thịt"
   - "đôi môi riêng tư" / "đôi môi bí mật" -> "môi dưới"
   - "từ Suzuguchi" / "lỗ sáo Suzuguchi" -> "lỗ sáo"
   - "con tinh trùng" -> "tinh dịch"
   - "công việc thủ công" -> "tự sướng"
   - Lỗi thẻ hỏng như <<br>br> -> <br>
   - Các dòng raw tiếng Nhật còn sót lại trong en.json được dịch chuẩn.

Cách dùng:
    python tools/fix_hmr_translations.py --check             # Chỉ quét kiểm tra & báo cáo lỗi trong các folder hmr_*
    python tools/fix_hmr_translations.py --fix               # Sửa lỗi và ghi đè vào file trong các folder hmr_*
    python tools/fix_hmr_translations.py --target hmr_10020100032  # Chỉ chạy trên 1 folder hmr cụ thể
    python tools/fix_hmr_translations.py --target all        # Tùy chọn mở rộng: Chạy trên tất cả folder novel trong translations/novels
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

# Thư mục gốc dự án
ROOT_DIR = Path(__file__).resolve().parent.parent

# Thư mục chứa toàn bộ novels
NOVELS_DIR = ROOT_DIR / "translations" / "novels"

# Mặc định mục tiêu chỉ là các folder hmr_* (H-scene memories)
DEFAULT_HMR_PATTERN = "hmr_*"

# Các từ khóa chỉ Chủ nhân / Master trong tiếng Nhật
MASTER_KEYWORDS = (
    "旦那様",
    "旦那さま",
    "だんな様",
    "だんなさま",
    "ご主人様",
    "ご主人さま",
    "ご主人",
    "主様",
    "あるじ様",
    "ご主人殿",
)


def fix_translation(ja: str, vi: str) -> tuple[str, list[str]]:
    """
    Sửa chuỗi bản dịch tiếng Việt dựa trên câu tiếng Nhật gốc.
    Trả về (chuỗi mới, danh sách các loại lỗi đã sửa).
    """
    if not vi or not isinstance(vi, str):
        return vi, []

    orig_vi = vi
    reasons: list[str] = []

    # 1. Thẻ HTML bị hỏng
    if "<<br>br>" in vi or "<br/>" in vi or "<br />" in vi:
        vi = re.sub(r"<<br>br>", "<br>", vi)
        vi = re.sub(r"<br\s*/>", "<br>", vi)
        reasons.append("html_tag_fix")

    # 2. Các câu thoại đặc biệt hoặc câu raw Japanese còn sót lại
    if (
        (ja == "はい、旦那様がよいのです。" or ja == "はい、旦那さまがよいのです。")
        and ("chồng" in vi.lower() or "vẫn ổn" in vi.lower())
    ):
        return "Vâng, chỉ cần là Chủ nhân là được ạ.", ["dannasama_special_line"]

    if ja == "ああっ……お、奥にズンズンと当たって……き、気持ちいぃ……っ♡<br>あぁっ……ぁはぁっ……旦那様……私……気持ちいぃです……♡":
        if "ズンズン" in orig_vi or "<<br>br>" in orig_vi:
            return (
                "Aah... c-chạm sâu vào bên trong liên tục... s-sướng quá...♡<br>Aa... a-haa... Chủ nhân... em... sướng lắm...♡",
                ["raw_japanese_replace"],
            )

    if ja == "きもひいいっ♡　いいにょぉっ♡　すきぃ♡　だいすきぃっ♡<br>あぁぁぁっ♡　イク、イクゥゥ――ッ♡":
        if "きもひいいっ" in orig_vi or "イク" in orig_vi:
            return (
                "Sướng quá đi♡ Thích quá đi♡ Thích lắm♡ Yêu nhất luôn á♡<br>Aaah♡ Ra, em ra đâyyy――♡",
                ["raw_japanese_replace"],
            )

    if ja == "はぁっ……ふっ、んっ、ぁぁ……<br>おにーさんのおちんぽ……熱くて、ふっといぃぃ～～……っ！":
        if "おにーさん" in orig_vi or "はぁっ" in orig_vi:
            return (
                "Haa... phu, ưm, aa...<br>Thanh thịt của Oni-san... nóng và to quá đi~~...!",
                ["raw_japanese_replace"],
            )

    if ja == "あぁぁ……んぅぅ……<br>こ、こんなに気持ち良くしてくれるの、おにーさんだけだよぉ……":
        if vi.strip() in ["Aaaa....", "Aaaa..."] or len(vi.strip()) <= 12:
            return (
                "Aaa... ưm...<br>L-Làm cho em sướng thế này, chỉ có Oni-san thôi đấy...",
                ["raw_japanese_replace"],
            )

    # Thoại nữ lên đỉnh Belisa L54:
    if ja == "ぅん！　イクッ、イグゥゥッッ！　ああっ、ふっ――あああ！<br>だいしゅきなおにーさんのおちんぽでイグのぉっ！":
        return (
            "Un! Tôi ra đây, ra đâyyy! Aaaa!<br>ra với thanh thịt của Oni-san!",
            ["female_climax_onisan"],
        )

    # 3. Thán từ: え / エ bị dịch thành 'hình ảnh', 'bức tranh'
    if (
        re.search(r"^(?:え|エ)[！？!\?……\.\,\s～~]*", ja)
        or "え？" in ja
        or "え！" in ja
        or "えっ" in ja
        or "えぇ" in ja
        or "えー" in ja
    ):
        prev = vi
        vi = re.sub(r"\bhình ảnh!\s*\?\s*hình ảnh!\s*\?", "Eh!? Eh!?", vi, flags=re.I)
        vi = re.sub(r"\bhình ảnh\s*!\s*\?", "Eh!?", vi, flags=re.I)
        vi = re.sub(r"\bhình ảnh\s*\?\s*!", "Eh!?", vi, flags=re.I)
        vi = re.sub(r"\bhình ảnh\s*\?+", "Eh?", vi, flags=re.I)
        vi = re.sub(r"\bhình ảnh\s*!+", "Eh!", vi, flags=re.I)
        vi = re.sub(r"\bhình ảnh\s*……\s*\?", "Eh……?", vi, flags=re.I)
        vi = re.sub(r"\bhình ảnh\s*……", "Eh……", vi, flags=re.I)
        vi = re.sub(r"\bhình ảnh\s*\.\.\.\s*\?", "Eh...?", vi, flags=re.I)
        vi = re.sub(r"\bhình ảnh\s*\.\.\.", "Eh...", vi, flags=re.I)
        vi = re.sub(r"^hình ảnh\b", "Eh", vi, flags=re.I)
        if vi != prev:
            reasons.append("interjection_e_romaji")

    # 4. Thán từ: ん？ ở đầu câu bị dịch thành 'vâng?' / 'đúng?'
    if re.search(r"^[んン][？\?]", ja):
        prev = vi
        vi = re.sub(r"^vâng\s*\?", "Hm?", vi, flags=re.I)
        vi = re.sub(r"^đúng\s*\?", "Hm?", vi, flags=re.I)
        if vi != prev:
            reasons.append("interjection_n_question")

    # 5. Danh xưng: おにーさん / お兄さん (chuẩn hóa thành Oni-san do không cùng huyết thống)
    if "おにーさん" in ja or "お兄さん" in ja or "おにいさん" in ja:
        prev = vi
        # Sửa các lỗi biến dạng dịch máy
        vi = re.sub(r"\bTekaonii\b", "Mà lại nói, Oni-san", vi, flags=re.I)
        vi = re.sub(r"\bmột onii\b", "Oni-san", vi, flags=re.I)
        vi = re.sub(r"\bcon thanh thịt của anh trai tôi\b", "thanh thịt của Oni-san", vi, flags=re.I)
        vi = re.sub(r"\bthanh thịt của anh trai tôi\b", "thanh thịt của Oni-san", vi, flags=re.I)
        vi = re.sub(r"\bthanh thịt của onii\b", "thanh thịt của Oni-san", vi, flags=re.I)
        vi = re.sub(r"\bZakozako Onii\b", "Oni-san yếu ớt", vi, flags=re.I)
        vi = re.sub(r"\bTsuyotsuyo Onii\b", "Oni-san mạnh mẽ", vi, flags=re.I)
        vi = re.sub(r"\bZaako của anh trai\b", "Oni-san gà mờ", vi, flags=re.I)
        vi = re.sub(r"\bOnii\b", "Oni-san", vi)
        vi = re.sub(r"\bonii\b", "Oni-san", vi)
        if vi != prev:
            reasons.append("onisan_pronoun")

    # 6. Sửa lỗi tiếng rên rỉ / biến âm của nữ:
    # - イグの / Iguno -> ra
    # - Rameee / Rame -> K-Không được / Đừng mà
    if "イグ" in ja or "イク" in ja or "らめ" in ja:
        prev = vi
        vi = re.sub(r"\bIguno với\b", "ra với", vi, flags=re.I)
        vi = re.sub(r"\bIguno\b", "ra", vi, flags=re.I)
        vi = re.sub(r"\bRameee!\s*Dừng lại đi!", "K-Không được rồi! Dừng lại đi!", vi, flags=re.I)
        vi = re.sub(r"\bRameee!?\b", "K-Không được đâu!?", vi, flags=re.I)
        vi = re.sub(r"\bRame\b", "Không được", vi, flags=re.I)
        if vi != prev:
            reasons.append("slurred_moan_fix")

    # 7. Sửa lỗi "bắn tinh" trong câu thoại của nhân vật NỮ khi lên đỉnh (イク / イグ / 絶頂)
    if "bắn tinh" in vi.lower():
        if "イク" in ja or "イグ" in ja or "シャオレイも" in ja or "またイク" in ja:
            prev = vi
            vi = re.sub(r"\bTôi ra đây,\s*bắn tinh!\b", "Tôi ra đây, ra đâyyy!", vi, flags=re.I)
            vi = re.sub(r"\bTiểu Lôi cũng bắn tinh\b", "Tiểu Lôi cũng ra đây", vi, flags=re.I)
            vi = re.sub(r"\bTôi lại bắn tinh nữa rồi\b", "Tôi lại ra nữa rồi", vi, flags=re.I)
            vi = re.sub(r"\bLại bắn tinh nữa rồi\b", "Lại ra nữa rồi", vi, flags=re.I)
            if vi != prev:
                reasons.append("female_climax_not_ban_tinh")

    # 8. Danh xưng 旦那様 / 旦那さま / ご主人様 / ご主人さま -> Chủ nhân
    if any(w in ja for w in MASTER_KEYWORDS):
        prev = vi
        # Bỏ 'Chủ nhân điện hạ'
        vi = re.sub(r"\bChủ nhân điện hạ\b", "Chủ nhân", vi, flags=re.I)

        # 'だ、旦那様 / だ、旦那さま' -> 'C-Chủ nhân' / 'Đ-Chủ nhân'
        vi = re.sub(r"\b[Dd]-(?:thưa ngài|thưa ông|chồng)\b", "C-Chủ nhân", vi)
        vi = re.sub(r"\b[Đđ]-chồng\b", "Đ-Chủ nhân", vi)
        vi = re.sub(r"\bch-chồng\b", "C-Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bX-thưa ngài\b", "C-Chủ nhân", vi, flags=re.I)
        vi = re.sub(r'\"?Vâng, thưa ngài\.\.\.\?', "Chủ nhân...?", vi)

        # Ngữ cảnh thanh thịt / tinh hoa của Chủ nhân
        vi = re.sub(r"\bthanh thịt chồng em\b", "thanh thịt của Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bthanh thịt của chồng(?: bạn| em)?\b", "thanh thịt của Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bthanh thịt của chồng\b", "thanh thịt của Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\b(?:tinh trùng|hạt giống) của chồng(?: em)?\b", "tinh hoa của Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bcon Chủ nhân tràn ngập\b", "tinh hoa của Chủ nhân tràn ra", vi, flags=re.I)

        # Các cụm 'chồng bạn', 'chồng em', 'chồng anh', 'chồng mình', 'người chồng', 'ông xã'
        vi = re.sub(r"\bchồng (?:bạn|em|tôi|mình|anh)\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bchồng của (?:bạn|em|tôi|mình|anh)\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bngười chồng yêu dấu\b", "Chủ nhân yêu dấu", vi, flags=re.I)
        vi = re.sub(r"\bngười chồng\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bông xã\b", "Chủ nhân", vi, flags=re.I)

        # Lời gọi: 'Chồng ơi,' / 'Chồng...' / 'chồng à'
        vi = re.sub(r"\bChồng ơi\b", "Chủ nhân ơi", vi, flags=re.I)
        vi = re.sub(r"\bChồng\s*(\.{2,}|…+)", r"Chủ nhân\1", vi, flags=re.I)
        vi = re.sub(r"\bchồng\s*,\s*anh\b", "Chủ nhân, ngài", vi, flags=re.I)
        vi = re.sub(r"\bchồng\s*à\b", "Chủ nhân à", vi, flags=re.I)
        vi = re.sub(r"\bthưa ngài\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bthưa ông\b", "Chủ nhân", vi, flags=re.I)

        # Từ 'Chồng' đứng đầu câu hoặc sau dấu câu
        vi = re.sub(r"(^|[,\.\?!;\n]|<br>)\s*Chồng\b", r"\1 Chủ nhân", vi)
        vi = re.sub(r"\bchồng\b", "Chủ nhân", vi, flags=re.I)

        if vi != prev:
            reasons.append("dannasama_chu_nhan")

    # 9. Thuật ngữ H-scene / Visual Novel chung
    prev = vi
    vi = re.sub(r"\bnước ép tình yêu\b", "dâm dịch", vi, flags=re.I)
    vi = re.sub(r"\bcon thanh thịt\b", "thanh thịt", vi, flags=re.I)
    vi = re.sub(r"\bcon gà trống\b", "thanh thịt", vi, flags=re.I)
    vi = re.sub(r"\bgà trống\b", "thanh thịt", vi, flags=re.I)
    vi = re.sub(r"\b(?:lỗ sáo Suzuguchi|từ Suzuguchi|Suzuguchi)\b", "lỗ sáo", vi, flags=re.I)
    vi = re.sub(r"\bđôi môi (?:riêng tư|bí mật)\b", "môi dưới", vi, flags=re.I)
    vi = re.sub(r"\bcon tinh trùng\b", "tinh dịch", vi, flags=re.I)
    vi = re.sub(r"\bcông việc thủ công\b", "tự sướng", vi, flags=re.I)
    if vi != prev:
        reasons.append("hscene_terminology")

    return vi, reasons


def find_target_files(target: str = DEFAULT_HMR_PATTERN) -> list[Path]:
    """
    Tìm danh sách file en.json cần xử lý.
    Mặc định: CHỈ quét các folder hmr_* trong translations/novels/
    """
    if target == DEFAULT_HMR_PATTERN or not target:
        # Chỉ quét các folder hmr_*
        pattern = NOVELS_DIR / "hmr_*" / "en.json"
        return sorted([Path(p) for p in glob.glob(str(pattern))])
    elif target == "all":
        # Tùy chọn nếu người dùng chủ động muốn quét toàn bộ các novel
        pattern = NOVELS_DIR / "*" / "en.json"
        return sorted([Path(p) for p in glob.glob(str(pattern))])
    else:
        # Nếu truyền vào tên một folder cụ thể (ví dụ: hmr_10020100032)
        if "*" in target:
            pattern = NOVELS_DIR / target / "en.json"
            return sorted([Path(p) for p in glob.glob(str(pattern))])
        target_dir = NOVELS_DIR / target
        if target_dir.is_dir():
            target_file = target_dir / "en.json"
            return [target_file] if target_file.exists() else []
        pattern = NOVELS_DIR / f"{target}*" / "en.json"
        return sorted([Path(p) for p in glob.glob(str(pattern))])


def main():
    parser = argparse.ArgumentParser(
        description="Kiểm tra và sửa lỗi dịch novel (mặc định CHỈ quét các folder hmr_*) trong DotAbyss."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Chỉ quét và báo cáo các lỗi phát hiện (dry-run, không ghi đè file).",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Sửa lỗi và ghi đè vào file JSON.",
    )
    parser.add_argument(
        "--target",
        type=str,
        default=DEFAULT_HMR_PATTERN,
        help="Thư mục mục tiêu: 'hmr_*' (mặc định chỉ quét hmr_*), tên folder cụ thể (ví dụ: 'hmr_10020100032'), hoặc 'all'.",
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="In chi tiết từng dòng được sửa.",
    )
    args = parser.parse_args()

    # Mặc định nếu không chỉ định --fix thì chạy ở chế độ check
    is_dry_run = not args.fix

    files = find_target_files(args.target)
    if not files:
        print(f"❌ Không tìm thấy file en.json nào phù hợp với target '{args.target}'.")
        return 1

    mode_str = "🔍 KIỂM TRA (DRY-RUN)" if is_dry_run else "✍️  SỬA VÀ GHI ĐÈ FILE"
    print("=" * 60)
    print(f"DotAbyss HMR Novel Translation Checker & Fixer")
    print(f"Chế độ: {mode_str}")
    print(f"Mục tiêu: {args.target} ({len(files)} files)")
    print("=" * 60)

    stats = defaultdict(int)
    modified_files = 0
    total_modified_entries = 0
    sample_diffs = []

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"⚠️ Lỗi đọc file {file_path}: {e}")
            continue

        if not isinstance(data, dict):
            continue

        file_changed = False
        new_data = {}

        for k, v in data.items():
            if not isinstance(v, str) or not v:
                new_data[k] = v
                continue

            new_v, reasons = fix_translation(k, v)
            if new_v != v:
                file_changed = True
                total_modified_entries += 1
                for r in reasons:
                    stats[r] += 1
                if len(sample_diffs) < 30 or args.verbose:
                    sample_diffs.append((file_path.parent.name, k, v, new_v, reasons))
                new_data[k] = new_v
            else:
                new_data[k] = v

        if file_changed:
            modified_files += 1
            if not is_dry_run:
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(new_data, f, ensure_ascii=False, indent=4)
                    f.write("\n")

    print(f"\n📊 KẾT QUẢ:")
    print(f"  - Tổng số file đã quét: {len(files)}")
    print(f"  - Số file có lỗi/cần sửa: {modified_files}")
    print(f"  - Tổng số câu sửa đổi: {total_modified_entries}")
    print(f"\n📈 Thống kê theo phân loại lỗi:")
    for reason, count in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  * {reason:30s}: {count:4d} lượt")

    if sample_diffs:
        print(f"\n📝 Chi tiết các câu đã sửa ({'toàn bộ' if args.verbose else 'mẫu tối đa 30 câu'}):")
        for folder, ja, old_v, new_v, reasons in sample_diffs:
            print(f"\n[{folder}] ({', '.join(reasons)})")
            print(f"  JA : {ja}")
            print(f"  OLD: {old_v}")
            print(f"  NEW: {new_v}")

    print("\n" + "=" * 60)
    if is_dry_run:
        print("💡 Đây là chế độ kiểm tra (--check). Chưa có file nào bị ghi đè.")
        print("👉 Để thực hiện sửa lỗi, hãy chạy lệnh:")
        print(f"   python tools/fix_hmr_translations.py --fix")
    else:
        print("✅ Đã hoàn tất sửa lỗi và cập nhật các file JSON thành công!")
    print("=" * 60)

    return 0


if __name__ == "__main__":
    sys.exit(main())
