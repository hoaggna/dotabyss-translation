#!/usr/bin/env python3
"""
Script to scan translation files in hmr_* folders for line segments (divided by <br>)
that exceed a specified character limit (default: 55 characters).
"""

import os
import glob
import json
import argparse

def main():
    parser = argparse.ArgumentParser(description="Scan translation JSONs for line segments exceeding character threshold.")
    parser.add_argument("--max-len", type=int, default=55, help="Maximum allowed characters per line segment (default: 55)")
    parser.add_argument("--pattern", type=str, default="hmr_*", help="Folder pattern inside translations/novels (default: hmr_*)")
    parser.add_argument("--save-report", action="store_true", help="Save report to reports/long_lines_report.json")

    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    novels_dir = os.path.join(base_dir, 'translations', 'novels')
    
    hmr_folders = glob.glob(os.path.join(novels_dir, args.pattern))
    print(f"🔍 Scanning {len(hmr_folders)} folders matching '{args.pattern}' (max_length = {args.max_len} chars)...\n")
    
    total_long_lines = 0
    affected_files = 0
    results = []

    for folder in sorted(hmr_folders):
        folder_name = os.path.basename(folder)
        for fname in sorted(os.listdir(folder)):
            if fname.endswith('.json'):
                fpath = os.path.join(folder, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                except Exception as e:
                    print(f"Error reading {fpath}: {e}")
                    continue

                file_long_lines = []
                for key, val in data.items():
                    if not isinstance(val, str):
                        continue
                    
                    segments = val.split('<br>')
                    for idx, seg in enumerate(segments, 1):
                        clean_seg = seg.strip()
                        if len(clean_seg) > args.max_len:
                            file_long_lines.append({
                                'key': key,
                                'val': val,
                                'seg_num': idx,
                                'total_segs': len(segments),
                                'length': len(clean_seg),
                                'segment': clean_seg
                            })
                            total_long_lines += 1

                if file_long_lines:
                    affected_files += 1
                    results.append({
                        'folder': folder_name,
                        'file': fname,
                        'rel_path': os.path.join('translations', 'novels', folder_name, fname),
                        'items': file_long_lines
                    })

    print("=" * 80)
    print(f"📊 REPORT SUMMARY:")
    print(f"   - Threshold limit : > {args.max_len} characters")
    print(f"   - Affected files  : {affected_files} / {len(hmr_folders)}")
    print(f"   - Total long lines: {total_long_lines}")
    print("=" * 80)

    for item in results:
        print(f"\n📄 {item['rel_path']} ({len(item['items'])} lines overflow)")
        for entry in item['items']:
            print(f"   Line {entry['seg_num']}/{entry['total_segs']} [{entry['length']} chars]: {entry['segment']}")

    if args.save_report:
        reports_dir = os.path.join(base_dir, 'reports')
        os.makedirs(reports_dir, exist_ok=True)
        report_file = os.path.join(reports_dir, 'long_lines_report.json')
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump({
                'max_len': args.max_len,
                'affected_files': affected_files,
                'total_long_lines': total_long_lines,
                'details': results
            }, f, ensure_ascii=False, indent=4)
        print(f"\n💾 Saved detailed JSON report to: {report_file}")

if __name__ == '__main__':
    main()
