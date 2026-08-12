import glob
import json
import os
import re

MASTER_KEYWORDS = ("旦那様", "旦那さま", "だんな様", "だんなさま", "ご主人様", "ご主人さま", "ご主人")

def fix_master(ja: str, vi: str) -> tuple[str, list[str]]:
    reasons = []
    if any(w in ja for w in MASTER_KEYWORDS):
        prev = vi
        vi = re.sub(r"\bChủ nhân điện hạ\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\b[Dd]-(?:thưa ngài|thưa ông|chồng)\b", "C-Chủ nhân", vi)
        vi = re.sub(r"\b[Đđ]-chồng\b", "Đ-Chủ nhân", vi)
        vi = re.sub(r"\bch-chồng\b", "C-Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bX-thưa ngài\b", "C-Chủ nhân", vi, flags=re.I)
        vi = re.sub(r'\"?Vâng, thưa ngài\.\.\.\?', "Chủ nhân...?", vi)
        vi = re.sub(r"\bthanh thịt chồng em\b", "thanh thịt của Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bthanh thịt của chồng(?: bạn| em)?\b", "thanh thịt của Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bthanh thịt của chồng\b", "thanh thịt của Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\b(?:tinh trùng|hạt giống) của chồng(?: em)?\b", "tinh hoa của Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bcon Chủ nhân tràn ngập\b", "tinh hoa của Chủ nhân tràn ra", vi, flags=re.I)
        vi = re.sub(r"\bchồng (?:bạn|em|tôi|mình|anh)\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bchồng của (?:bạn|em|tôi|mình|anh)\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bngười chồng yêu dấu\b", "Chủ nhân yêu dấu", vi, flags=re.I)
        vi = re.sub(r"\bngười chồng\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bông xã\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bChồng ơi\b", "Chủ nhân ơi", vi, flags=re.I)
        vi = re.sub(r"\bChồng\s*(\.{2,}|…+)", r"Chủ nhân\1", vi, flags=re.I)
        vi = re.sub(r"\bchồng\s*,\s*anh\b", "Chủ nhân, ngài", vi, flags=re.I)
        vi = re.sub(r"\bchồng\s*à\b", "Chủ nhân à", vi, flags=re.I)
        vi = re.sub(r"\bthưa ngài\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"\bthưa ông\b", "Chủ nhân", vi, flags=re.I)
        vi = re.sub(r"(^|[,\.\?!;\n]|<br>)\s*Chồng\b", r"\1 Chủ nhân", vi)
        vi = re.sub(r"\bchồng\b", "Chủ nhân", vi, flags=re.I)
        if vi != prev:
            reasons.append("dannasama_chu_nhan")
    return vi, reasons

hmr_files = sorted(glob.glob("translations/novels/hmr_*/en.json"))
diffs = []
for f in hmr_files:
    with open(f, "r", encoding="utf-8") as fp:
        try:
            d = json.load(fp)
        except Exception:
            continue
    for k, v in d.items():
        if not v:
            continue
        new_v, reasons = fix_master(k, v)
        if new_v != v:
            diffs.append((f, k, v, new_v))

print(f"Total master lines fixed: {len(diffs)}")
for f, k, old_v, new_v in diffs:
    folder = os.path.basename(os.path.dirname(f))
    print(f"[{folder}]")
    print(f"  JA : {k}")
    print(f"  OLD: {old_v}")
    print(f"  NEW: {new_v}\n")
