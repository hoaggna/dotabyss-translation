# -*- coding: utf-8 -*-
import json
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

for folder in folders:
    rel_path = f"translations/novels/{folder}/en.json"
    raw_json = subprocess.check_output(["git", "show", f"4f109c0c:{rel_path}"], cwd=str(ROOT_DIR)).decode("utf-8")
    orig_data = json.loads(raw_json)
    
    file_path = ROOT_DIR / rel_path
    with open(file_path, "r", encoding="utf-8") as f:
        curr_data = json.load(f)
    
    orig_keys = set(orig_data.keys())
    curr_keys = set(curr_data.keys())
    
    missing = orig_keys - curr_keys
    extra = curr_keys - orig_keys
    print(f"[{folder}] Orig: {len(orig_keys)}, Curr: {len(curr_keys)}, Missing: {len(missing)}, Extra: {len(extra)}")
    if missing:
        for k in list(missing)[:3]:
            print(f"   Missing key: {k[:40]}...")
