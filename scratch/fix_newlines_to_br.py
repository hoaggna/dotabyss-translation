# -*- coding: utf-8 -*-
import json
import re
import subprocess
from pathlib import Path

ROOT_DIR = Path(r"d:\idontknow\dotabyss-translation")
folders = [
    "hmr_10220100011", "hmr_10220100012", "hmr_10220100013",
    "hmr_10220100021", "hmr_10220100022", "hmr_10220100023",
    "hmr_10220100031", "hmr_10220100032", "hmr_10220100033",
    "hmr_11030100011", "hmr_11030100012", "hmr_11030100013",
    "hmr_11030100021", "hmr_11030100022", "hmr_11030100023",
    "hmr_11030100031", "hmr_11030100032", "hmr_11030100033",
]

total_keys = 0
fixed_nl = 0
long_lines_75 = 0

for folder in folders:
    rel_path = f"translations/novels/{folder}/en.json"
    file_path = ROOT_DIR / rel_path
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    cleaned_data = {}
    for ja, vi in data.items():
        total_keys += 1
        # Convert literal newlines to <br>
        if "\n" in vi:
            vi = vi.replace("\r\n", "<br>").replace("\n", "<br>")
            fixed_nl += 1
            
        # Clean leading/trailing <br>
        vi = re.sub(r"^(?:\s*<br\s*/?>)+", "", vi)
        vi = re.sub(r"(?:<br\s*/?>\s*)+$", "", vi)
        vi = re.sub(r"(?:<br\s*/?>\s*){2,}", "<br>", vi)
        
        # Check line length
        lines = re.split(r"<br\s*/?>", vi)
        for idx, line in enumerate(lines):
            disp = re.sub(r"<[^>]+>", "", line).strip()
            if len(disp) > 75:
                long_lines_75 += 1
                print(f"[{folder}] Dòng > 75 ký tự ({len(disp)}): {disp}")
                
        cleaned_data[ja] = vi
        
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)
        f.write("\n")

print(f"\nTổng kết: {len(folders)} file, {total_keys} câu.")
print(f"Đã sửa newline -> <br>: {fixed_nl}")
print(f"Số dòng > 75 ký tự: {long_lines_75}")
