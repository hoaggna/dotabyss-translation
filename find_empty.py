import os
import glob

# Đường dẫn đến thư mục chứa các folder hmr_
folder_path = r"D:\idontknow\dotabyss-translation\translations\novels\hmr_*"

# Quét tất cả các file bên trong hmr_*
files = glob.glob(os.path.join(folder_path, "**", "*"), recursive=True)

found_files_count = 0

for file_path in files:
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                
                for idx, line in enumerate(lines):
                    # idx == 1 chính là DÒNG 2 (Python đếm từ 0 -> bỏ qua Dòng 2)
                    if idx == 1:
                        continue
                    
                    # Nếu tìm thấy "" thì in ra và THOÁT KHỎI FILE NÀY NGHUYÊN LẬP TỨC
                    if '""' in line:
                        print(f"[CÓ LỖI] {file_path} | Tìm thấy đầu tiên tại dòng {idx + 1}")
                        found_files_count += 1
                        break  # <--- Dừng quét các dòng còn lại của file này
                        
        except Exception:
            pass

print(f"\n==========================================")
print(f"Hoàn tất! Tìm thấy tổng cộng {found_files_count} file chứa '\"\"'.")