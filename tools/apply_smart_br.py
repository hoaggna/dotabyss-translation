#!/usr/bin/env python3
"""
Script to automatically format and re-balance <br> line breaks in hmr_*/en.json files.

Rules enforced:
1. Maximum 3 lines total per entry (at most 2 <br> tags).
2. Cleans unnecessary or broken <br> tags first (preventing broken words or tiny 4th lines).
3. Automatically determines target number of lines (1, 2, or 3) based on total length.
4. Splits lines evenly around punctuation (, . ! ? … ~ ♪ ♡ : ;) or word boundaries.
5. Only applies to translation values (v), preserving Japanese keys (k) intact.
"""

import os
import glob
import json
import argparse
import re

PUNCTUATION_MARKS = (',', '.', '!', '?', '…', '~', '♪', '♡', ':', ';', '.”', '!”', '?”')

def find_best_word_split(words: list, target_char_pos: int) -> int:
    """Find the word index after which to split to get as close to target_char_pos as possible."""
    if len(words) <= 1:
        return len(words)
        
    current_char_count = 0
    word_positions = []
    for i, w in enumerate(words):
        current_char_count += len(w) + (1 if i > 0 else 0)
        word_positions.append((i, current_char_count, w))
        
    best_word_idx = 0
    best_score = float('inf')
    
    # Don't split after the last word
    for i, char_pos, w in word_positions[:-1]:
        dist = abs(char_pos - target_char_pos)
        score = dist
        # Punctuation bonus: if the word ends with punctuation, prefer splitting here
        if w and w[-1] in PUNCTUATION_MARKS:
            score -= 8
            
        if score < best_score:
            best_score = score
            best_word_idx = i
            
    return best_word_idx + 1

def rebalance_br(text: str, max_lines: int = 2, target_line_len: int = 55) -> str:
    if not isinstance(text, str) or not text.strip():
        return text
    
    # 1. Clean existing <br> tags and normalize spaces
    clean = re.sub(r'\s*<br\s*/?>\s*', ' ', text, flags=re.IGNORECASE)
    clean = re.sub(r' {2,}', ' ', clean).strip()
    
    total_len = len(clean)
    
    # 2. Determine target line count (Max 2 lines = Max 1 <br>)
    if total_len <= target_line_len:
        num_lines = 1
    else:
        num_lines = min(2, max_lines)
        
    if num_lines == 1:
        return clean
        
    words = clean.split(' ')
    if len(words) <= 1:
        return clean

    if num_lines == 2:
        split1 = find_best_word_split(words, total_len // 2)
        line1 = ' '.join(words[:split1])
        line2 = ' '.join(words[split1:])
        return f"{line1}<br>{line2}"
        
    else: # num_lines == 3
        target1 = total_len // 3
        split1 = find_best_word_split(words, target1)
        
        line1_words = words[:split1]
        remaining_words = words[split1:]
        
        remaining_len = len(' '.join(remaining_words))
        target2 = remaining_len // 2
        split2 = find_best_word_split(remaining_words, target2)
        
        line1 = ' '.join(line1_words)
        line2 = ' '.join(remaining_words[:split2])
        line3 = ' '.join(remaining_words[split2:])
        return f"{line1}<br>{line2}<br>{line3}"

def main():
    parser = argparse.ArgumentParser(description="Re-balance <br> line breaks in hmr_*/en.json files (Max 3 lines total).")
    parser.add_argument("--max-len", type=int, default=55, help="Target line length threshold (default: 55)")
    parser.add_argument("--pattern", type=str, default="hmr_*", help="Folder pattern (default: hmr_*)")
    parser.add_argument("--dry-run", action="store_true", help="Perform dry run without modifying files")

    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    novels_dir = os.path.join(base_dir, 'translations', 'novels')
    
    hmr_folders = glob.glob(os.path.join(novels_dir, args.pattern))
    print(f"🚀 Processing {len(hmr_folders)} folders matching '{args.pattern}' (max 3 lines / max 2 <br> per entry)...\n")
    
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
            new_v = rebalance_br(v, max_lines=3, target_line_len=args.max_len)
            if new_v != v:
                file_changed = True
                total_strings_modified += 1
            new_data[k] = new_v

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
    print(f"  - Strings formatted: {total_strings_modified}")
    print("=" * 60)

if __name__ == '__main__':
    main()
