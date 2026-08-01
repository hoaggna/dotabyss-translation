#!/usr/bin/env python3
"""
Script to fix corrupted <user> tags and translated 'người dùng' / 'người sử dụng'
in translation values across all hmr_* (and optionally other novel) folders.
Also re-balances <br> line breaks so lines remain clean and bounded (max 3 lines total).
"""

import os
import glob
import json
import argparse
import re

from apply_smart_br import rebalance_br

def fix_user_tag(k: str, v: str) -> str:
    if not isinstance(v, str) or not isinstance(k, str):
        return v
    
    k_user_cnt = k.count('<user>')
    if k_user_cnt == 0:
        return v  # Japanese key doesn't have <user>, don't modify người dùng in normal text
        
    v_clean = v
    
    # 1. Temporarily remove existing <br> inside split tags like <người<br>dùng>
    v_clean = re.sub(r'<\s*người\s*<br\s*/?>\s*dùng\s*>', '<người dùng>', v_clean, flags=re.IGNORECASE)
    v_clean = re.sub(r'<\s*người\s*<br\s*/?>\s*sử\s*<br\s*/?>\s*dụng\s*>', '<người sử dụng>', v_clean, flags=re.IGNORECASE)
    v_clean = re.sub(r'người\s*<br\s*/?>\s*dùng', 'người dùng', v_clean, flags=re.IGNORECASE)
    v_clean = re.sub(r'người\s*<br\s*/?>\s*sử\s*dụng', 'người sử dụng', v_clean, flags=re.IGNORECASE)
    
    # 2. Replace translated user tags inside value
    v_clean = re.sub(r'<\s*người\s*(dùng|sử\s*dụng)\s*>', '<user>', v_clean, flags=re.IGNORECASE)
    
    # If <user> was not produced yet and 'người dùng' or 'người sử dụng' exists
    v_clean = re.sub(r'\bngười\s*(dùng|sử\s*dụng)\b', '<user>', v_clean, flags=re.IGNORECASE)
    
    # 3. Handle duplicated leading <user>
    if v_clean.strip().startswith('<user>') and v_clean.count('<user>') > k_user_cnt:
        v_clean = re.sub(r'^\s*<user>\s*', '', v_clean, count=1)
        
    # Also handle redundant double <user> <user> or <user><user>
    v_clean = re.sub(r'<user>\s*<user>', '<user>', v_clean)
    
    return v_clean

def main():
    parser = argparse.ArgumentParser(description="Fix corrupted <user> tags and translated 'người dùng' in hmr_*/en.json files.")
    parser.add_argument("--pattern", type=str, default="hmr_*", help="Folder pattern (default: hmr_*)")
    parser.add_argument("--dry-run", action="store_true", help="Perform dry run without modifying files")

    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    novels_dir = os.path.join(base_dir, 'translations', 'novels')
    
    hmr_folders = glob.glob(os.path.join(novels_dir, args.pattern))
    print(f"🚀 Processing <user> tags in {len(hmr_folders)} folders matching '{args.pattern}'...\n")
    
    total_files_modified = 0
    total_strings_modified = 0

    for folder in sorted(hmr_folders):
        fpath = os.path.join(folder, 'en.json')
        if not os.path.exists(fpath):
            continue

        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"Error reading {fpath}: {e}")
            continue

        file_changed = False
        new_data = {}
        for k, v in data.items():
            fixed_v = fix_user_tag(k, v)
            final_v = rebalance_br(fixed_v, max_lines=2, target_line_len=55)
            
            if final_v != v:
                file_changed = True
                total_strings_modified += 1
            new_data[k] = final_v

        if file_changed:
            total_files_modified += 1
            if not args.dry_run:
                with open(fpath, 'w', encoding='utf-8') as f:
                    json.dump(new_data, f, ensure_ascii=False, indent=4)
                    f.write('\n')

    status = "DRY RUN COMPLETE" if args.dry_run else "SUCCESSFULLY APPLIED"
    print("=" * 60)
    print(f"STATUS: {status}")
    print(f"  - Files modified   : {total_files_modified} / {len(hmr_folders)}")
    print(f"  - Strings fixed    : {total_strings_modified}")
    print("=" * 60)

if __name__ == '__main__':
    main()
