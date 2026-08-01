#!/usr/bin/env python3
"""
Script to remove honorific suffixes (-dono, -sama, -san, -kun, -chan)
from translated names and titles in hmr_*/en.json files to reduce character count.
Also re-balances <br> line breaks so lines remain clean and bounded (max 3 lines total).
"""

import os
import glob
import json
import argparse
import re

from apply_smart_br import rebalance_br

# Match honorific suffixes attached to names/titles (e.g. Tư lệnh-dono, Kotono-san, Belisa-chan)
SUFFIX_HYPHEN_REGEX = r'(\b[\w\u00C0-\u024F]{2,})-(?:dono|sama|san|kun|chan)\b'
SUFFIX_SPACE_REGEX = r'(\b(?:Tư lệnh|Chủ nhân|Sư phụ|Thầy|Hiệp sĩ|Quân chủ|Thiếu nữ|Anh|Chị|Em|Cậu)\s+)(?:dono|sama|san|kun|chan)\b'

def clean_suffixes(text: str) -> str:
    if not isinstance(text, str):
        return text
    
    # 1. Remove hyphenated suffixes (-dono, -sama, -san, -kun, -chan)
    text = re.sub(SUFFIX_HYPHEN_REGEX, r'\1', text, flags=re.IGNORECASE)
    
    # 2. Remove space-separated suffixes after titles
    text = re.sub(SUFFIX_SPACE_REGEX, r'\1', text, flags=re.IGNORECASE)
    
    # 3. Clean potential double spaces
    text = re.sub(r' {2,}', ' ', text)
    
    return text

def main():
    parser = argparse.ArgumentParser(description="Remove honorific suffixes (-dono, -sama, -san, -kun, -chan) from hmr_*/en.json files.")
    parser.add_argument("--pattern", type=str, default="hmr_*", help="Folder pattern (default: hmr_*)")
    parser.add_argument("--dry-run", action="store_true", help="Perform dry run without modifying files")

    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    novels_dir = os.path.join(base_dir, 'translations', 'novels')
    
    hmr_folders = glob.glob(os.path.join(novels_dir, args.pattern))
    print(f"🚀 Processing suffixes in {len(hmr_folders)} folders matching '{args.pattern}'...\n")
    
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
            cleaned_v = clean_suffixes(v)
            final_v = rebalance_br(cleaned_v, max_lines=3, target_line_len=55)
            
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
    print(f"  - Strings cleaned  : {total_strings_modified}")
    print("=" * 60)

if __name__ == '__main__':
    main()
