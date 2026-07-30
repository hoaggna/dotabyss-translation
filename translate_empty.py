"""
Script dịch tự động Nhật → Việt cho các file novel chưa dịch.
Sử dụng Ollama Local với model qwen2.5:7b.

Cách dùng:
    py translate_empty.py                   # Dịch tất cả file novel có câu trống
    py translate_empty.py --model qwen2.5:7b # Đổi tên model Ollama nếu cần
    py translate_empty.py --batch-size 5    # Số file mỗi batch
    py translate_empty.py --dry-run         # Chỉ liệt kê file, không dịch
"""

import os
import sys
import json
import glob
import time
import argparse
import urllib.request
import urllib.error

# ─── Cấu hình ───────────────────────────────────────────────────────────────

NOVELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "translations", "novels")
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"

SYSTEM_PROMPT = """Bạn là dịch giả chuyên nghiệp game visual novel Nhật → Việt.

QUY TẮC DỊCH:
1. Dịch tự nhiên, mượt mà, giữ đúng ngữ cảnh và cảm xúc nhân vật.
2. Giữ nguyên tên riêng nhân vật bằng Romaji (ví dụ: コトノ → Kotono, ルディア → Rudia, ディアーナ → Diana, ルシータ → Lucita).
3. Giữ nguyên thẻ HTML như <br>, không thêm bớt.
4. Giữ nguyên các ký tự đặc biệt: ♡, ～, ♪, ……, ！？, ―― v.v.
5. Danh xưng:
   - 旦那様 → Tướng công / Ngài
   - 司令官 → Tư lệnh / anh Chỉ huy
   - 私 / ボク → Em / tôi / tại hạ (tùy nhân vật)
6. Tiếng rên/thán từ (はぁ, んっ, あぁ...): Phiên âm tự nhiên (Hà, ưm, aa...).
7. Lời thoại trong ngoặc （）: là suy nghĩ nội tâm, giữ trong ngoặc ().

ĐỊNH DẠNG OUTPUT:
- Trả về JSON object duy nhất.
- Key = text tiếng Nhật gốc (giữ nguyên 100%).
- Value = bản dịch tiếng Việt.
- KHÔNG thêm markdown code block, KHÔNG thêm lời giải thích."""


def check_ollama(model_name):
    """Kiểm tra kết nối Ollama và model."""
    try:
        req = urllib.request.Request("http://127.0.0.1:11434/api/tags")
        with urllib.request.urlopen(req, timeout=5) as res:
            data = json.loads(res.read().decode("utf-8"))
            models = [m.get("name", "") for m in data.get("models", [])]
            
            # Kiểm tra xem model có trong danh sách không
            has_model = any(model_name in m for m in models)
            if not has_model:
                print(f"⚠️ Cảnh báo: Không tìm thấy '{model_name}' trong Ollama.")
                print(f"   Các model hiện có: {models}")
                print(f"   Vui lòng tải model: ollama run {model_name}")
                return False
            return True
    except Exception as e:
        print(f"❌ Không thể kết nối tới Ollama tại 127.0.0.1:11434 ({e})")
        print("   Vui lòng bật Ollama trước khi chạy script.")
        return False


def find_empty_files():
    """Tìm tất cả file en.json có value rỗng (bỏ qua title ở dòng 2)."""
    empty_files = []
    pattern = os.path.join(NOVELS_DIR, "hmr_*", "en.json")

    for file_path in sorted(glob.glob(pattern)):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Bỏ qua entry đầu tiên (title) ở dòng 2
            items = list(data.items())[1:]
            empty_count = sum(1 for _, v in items if v == "")
            if empty_count > 0:
                total = len(data)
                empty_files.append({
                    "path": file_path,
                    "data": data,
                    "empty_count": empty_count,
                    "total": total,
                    "folder": os.path.basename(os.path.dirname(file_path)),
                })
        except Exception as e:
            print(f"  [LỖI ĐỌC] {file_path}: {e}")

    return empty_files


def extract_empty_entries(data):
    """Lấy các entry có value rỗng (bỏ qua entry đầu tiên / title ở dòng 2)."""
    items = list(data.items())[1:]
    return {k: v for k, v in items if v == ""}


def query_ollama(model_name, prompt):
    """Gửi request tới Ollama local."""
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        "stream": False,
        "options": {
            "temperature": 0.3,
        }
    }

    req_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_URL,
        data=req_data,
        headers={"Content-Type": "application/json"}
    )

    with urllib.request.urlopen(req, timeout=120) as response:
        res_body = json.loads(response.read().decode("utf-8"))
        return res_body.get("message", {}).get("content", "").strip()


def translate_file(model_name, file_info):
    """Dịch một file bằng Ollama (chia nhỏ thành các chunk 10 câu)."""
    empty_entries = extract_empty_entries(file_info["data"])
    if not empty_entries:
        return None

    items = list(empty_entries.items())
    chunk_size = 10  # Dịch 10 câu mỗi lần cho Qwen 7b mượt và chuẩn
    all_translated = {}

    for i in range(0, len(items), chunk_size):
        chunk = dict(items[i:i + chunk_size])
        input_json = json.dumps(chunk, ensure_ascii=False, indent=2)

        prompt = f"""Dịch các value rỗng ("") trong JSON sau sang tiếng Việt:

{input_json}"""

        for attempt in range(1, 3):
            try:
                response_text = query_ollama(model_name, prompt)

                # Làm sạch response nếu có markdown code block ```json ... ```
                if response_text.startswith("```"):
                    lines = response_text.split("\n")
                    start = 1
                    end = len(lines) - 1
                    if lines[end].strip() == "```":
                        response_text = "\n".join(lines[start:end])

                # Tìm vị trí { và } cuối cùng để trích xuất JSON
                start_idx = response_text.find("{")
                end_idx = response_text.rfind("}")
                if start_idx != -1 and end_idx != -1:
                    json_str = response_text[start_idx:end_idx + 1]
                    translated_chunk = json.loads(json_str)
                    all_translated.update(translated_chunk)
                    break

            except Exception as e:
                print(f"\n    [LỖI CHUNK {i//chunk_size + 1}] {e}")
                time.sleep(2)

    return all_translated if all_translated else None


def merge_and_save(file_info, translated):
    """Merge bản dịch vào file gốc và lưu."""
    data = file_info["data"].copy()
    merged_count = 0

    for key, value in translated.items():
        if key in data and data[key] == "" and value and value != "":
            data[key] = value
            merged_count += 1

    # Lưu file
    with open(file_info["path"], "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return merged_count


def main():
    parser = argparse.ArgumentParser(description="Dịch tự động novel Nhật → Việt bằng Ollama local (qwen2.5:7b)")
    parser.add_argument("--model", type=str, default="qwen2.5:7b", help="Model Ollama (mặc định: qwen2.5:7b)")
    parser.add_argument("--batch-size", type=int, default=10, help="Số file mỗi batch (mặc định: 10)")
    parser.add_argument("--dry-run", action="store_true", help="Chỉ liệt kê file, không dịch")
    args = parser.parse_args()

    print("=" * 60)
    print("  DỊCH TỰ ĐỘNG NOVEL NHẬT → VIỆT (OLLAMA LOCAL)")
    print("=" * 60)

    # ─── Kiểm tra Ollama ─────────────────────────────────────────────────
    if not args.dry_run:
        print(f"\nĐang kết nối Ollama local (Model: {args.model})...")
        if not check_ollama(args.model):
            return
        print("✅ Kết nối Ollama thành công!")

    # ─── Tìm file cần dịch ───────────────────────────────────────────────
    print(f"\nĐang quét thư mục: {NOVELS_DIR}")
    empty_files = find_empty_files()

    if not empty_files:
        print("\n✅ Không tìm thấy file nào cần dịch!")
        return

    total_empty = sum(f["empty_count"] for f in empty_files)
    print(f"\nTìm thấy {len(empty_files)} file cần dịch ({total_empty} câu trống)")
    print("-" * 60)

    for i, f in enumerate(empty_files, 1):
        print(f"  {i:3d}. {f['folder']}/en.json  ({f['empty_count']}/{f['total']} câu trống)")

    if args.dry_run:
        print("\n[DRY RUN] Chỉ liệt kê, không dịch.")
        return

    # ─── Dịch từng file ───────────────────────────────────────────────────
    batch_size = args.batch_size
    total_files = len(empty_files)
    total_translated = 0
    total_failed = 0

    start_time = time.time()

    for i, file_info in enumerate(empty_files, 1):
        folder = file_info["folder"]
        empty_count = file_info["empty_count"]

        print(f"\n  [{i}/{total_files}] {folder}/en.json ({empty_count} câu trống)...", end="", flush=True)

        translated = translate_file(args.model, file_info)

        if translated:
            merged = merge_and_save(file_info, translated)
            print(f" ✅ Đã dịch {merged}/{empty_count} câu")
            total_translated += merged
        else:
            print(f" ❌ Thất bại")
            total_failed += 1

    elapsed = time.time() - start_time

    # ─── Tổng kết ────────────────────────────────────────────────────────
    print(f"\n{'=' * 60}")
    print(f"  HOÀN TẤT!")
    print(f"  ✅ Đã dịch: {total_translated} câu")
    print(f"  ❌ Thất bại: {total_failed} file")
    print(f"  📁 Tổng file xử lý: {total_files}")
    print(f"  ⏱️  Thời gian: {elapsed:.1f} giây")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
