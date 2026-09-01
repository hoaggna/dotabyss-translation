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

all_issues = []

for folder in folders:
    rel_path = f"translations/novels/{folder}/en.json"
    file_path = ROOT_DIR / rel_path
    
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for ja, vi in data.items():
        # check \n
        if "\n" in vi:
            all_issues.append((folder, ja, vi, "contains literal \\n"))
        # check trailing/leading br
        if re.search(r"^(?:\s*<br\s*/?>)+", vi) or re.search(r"(?:<br\s*/?>\s*)+$", vi):
            all_issues.append((folder, ja, vi, "leading/trailing <br>"))
        # check multiple br
        brs = re.findall(r"<br\s*/?>", vi)
        if len(brs) > 1:
            all_issues.append((folder, ja, vi, f"{len(brs)} <br> tags"))
        # check line length > 70
        lines = re.split(r"<br\s*/?>", vi)
        for i, l in enumerate(lines):
            l_strip = re.sub(r"<[^>]+>", "", l)
            if len(l_strip) > 70:
                all_issues.append((folder, ja, vi, f"Line {i+1} len={len(l_strip)}: '{l}'"))

print(f"Total issues: {len(all_issues)}")
for folder, ja, vi, reason in all_issues:
    print(f"[{folder}] {reason}\n  JA: {ja}\n  VI: {vi}\n")
