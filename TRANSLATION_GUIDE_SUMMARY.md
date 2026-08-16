# 📖 TỔNG HỢP TOÀN BỘ QUY TẮC & CHÚ Ý KHI DỊCH (DOTABYSS)

> Tài liệu tóm tắt đầy đủ tất cả các quy chuẩn xưng hô, thán từ, thuật ngữ H-scene, **giới hạn độ dài / độ rộng khung thoại (Text Width & `<br>`)**, kỹ thuật và đối chiếu Nhật - Trung - Việt cho dự án **DotAbyss Translation**.

---

## 📌 MỤC LỤC
1. [Giới Hạn Độ Dài & Độ Rộng Khung Thoại (Text Width & Line Break)](#1-giới-hạn-độ-dài--độ-rộng-khung-thoại-text-width--line-break) ⚠️ **RẤT QUAN TRỌNG**
2. [Danh Xưng & Đại Từ Nhân Xưng](#2-danh-xưng--đại-từ-nhân-xưng)
3. [Thán Từ & Biến Âm Rên Rỉ (Romaji / Onomatopoeia)](#3-thán-từ--biến-âm-rên-rỉ)
4. [Quy Tắc Thuật Ngữ H-Scene (18+ / Visual Novel)](#4-quy-tắc-thuật-ngữ-h-scene-18)
5. [Phân Biệt Nữ Lên Đỉnh vs Nam Xuất Tinh](#5-phân-biệt-nữ-lên-đỉnh-vs-nam-xuất-tinh)
6. [Tên Riêng & Giọng Điệu Nhân Vật Đặc Thù](#6-tên-riêng--giọng-điệu-nhân-vật)
7. [Quy Chuẩn Kỹ Thuật & Thẻ Game (HTML / Ruby Tags)](#7-quy-chuẩn-kỹ-thuật--thẻ-game)
8. [Kinh Nghiệm Dịch: Kết Hợp Trung (ZH) & Nhật (JA)](#8-kinh-nghiệm-dịch-kết-hợp-zh--ja)

---

## 1. GIỚI HẠN ĐỘ DÀI & ĐỘ RỘNG KHUNG THOẠI (TEXT WIDTH & LINE BREAK)

> ⚠️ **ĐẶC THÙ NGÔN NGỮ**: Tiếng Nhật (JA) và tiếng Trung (ZH) có mật độ thông tin ký tự rất cao (1-2 chữ Hán bằng 3-5 từ tiếng Việt). Khi dịch sang tiếng Việt (chữ Latinh + khoảng trắng), độ dài văn bản thường **dài hơn gấp 1.5 đến 2.5 lần**. Nếu không kiểm soát, chữ sẽ bị **tràn khung thoại (overflow), che khuất nhân vật hoặc bị cắt cụt mất chữ**.

### 📏 Các giới hạn kích thước cần tuân thủ:

| Yếu tố | Giới hạn chuẩn | Hậu quả nếu vi phạm |
| :--- | :--- | :--- |
| **Độ dài mỗi dòng (Line Width)** | **Lên đến 70 ký tự / dòng** | Tràn ra ngoài rìa khung thoại (vỡ layout). |
| **Số dòng tối đa / 1 hộp thoại** | **Tối đa 1 thẻ `<br>`** *(tối đa 2 dòng văn bản)* | Chữ tràn xuống đáy màn hình, bị cắt mất dòng cuối. |
| **Thẻ chữ phóng to `<size=48>`** | **Dưới 20 ký tự** *(câu cực ngắn)* | Chữ to quá khổ tràn hẳn ra ngoài màn hình. |

---

### ✂️ Quy tắc ngắt dòng chủ động bằng `<br>`:

1. **Ngắt dòng cân đối giữa các câu**:
   - Tránh để dòng 1 quá dài còn dòng 2 quá ngắn (hoặc ngược lại).
   - *Ví dụ xấu*:
     ```json
     "Lờ đi Belisa đang hoảng loạn, tôi dồn hết sức đẩy mạnh thanh thịt căng cứng vào trong.<br>Cô ấy rên rỉ."
     ```
   - *Ví dụ chuẩn*:
     ```json
     "Lờ đi Belisa đang hoảng loạn,<br>tôi ấn mạnh thanh thịt căng phồng vào sâu bên trong."
     ```

2. **Vị trí ngắt dòng tự nhiên**:
   - Ngắt ngay sau các dấu ngắt câu: dấu phẩy `,`, dấu chấm `.`, gạch nối `――`, dấu chấm lửng `...`, thán từ rên rỉ `♡`, `!`.
   - Ngắt theo cụm chủ vị / vế câu có nghĩa. Tuyệt đối **không ngắt đôi từ ghép** (ví dụ: `dương<br>vật`, `Tư<br>lệnh`).

3. **Kỹ thuật dịch cô đọng, súc tích (Conciseness)**:
   - Cắt bỏ các từ đệm rườm rà không cần thiết (`thì là mà`, `một cách vô cùng`, `ở tại nơi này`).
   - Ưu tiên dùng từ Hán-Việt ngắn gọn, giàu hình ảnh thay vì giải nghĩa lê thê.
   - *Gốc (ZH)*: `「听到这个让人高兴的消息，我心中的喜悦简直无法用言语来形容」`
   - *Dịch dài (dễ tràn)*: `Nghe được cái tin tức khiến cho người ta vui vẻ này, sự vui mừng ở trong lòng tôi thực sự không thể nào dùng ngôn ngữ để mà miêu tả được.` (140 ký tự ❌)
   - *Dịch gọn (vừa vặn)*: `Nghe tin vui ấy, cõi lòng tôi rộn rã niềm vui khó tả.` (50 ký tự ✅)

4. **🚫 TUYỆT ĐỐI KHÔNG để `<br>` ở cuối hoặc đầu câu dịch**:
   - Nếu câu dịch có `<br>` ở cuối (ví dụ: `"Dòng 1...<br>Dòng 2...<br>"`), engine game sẽ hiểu là có **dòng thứ 3 (dòng trống)**.
   - **Hậu quả**: Khung thoại bị tràn vượt quá 2 dòng, gây đẩy lệch vị trí hiển thị, làm dòng trên cùng bị cắt mất chữ hoặc icon con trỏ (Next click) bị rớt xuống dòng trống bên dưới viền khung thoại.
   - Thẻ `<br>` **chỉ được nằm ở giữa câu** để phân chia dòng 1 và dòng 2.

---

## 2. DANH XƯNG & ĐẠI TỪ NHÂN XƯNG

| Tiếng Nhật (JA) | Tiếng Trung (ZH) | Dịch Chuẩn Tiếng Việt (VI) | ❌ Lỗi Dịch Máy Cần Tránh |
| :--- | :--- | :--- | :--- |
| **`旦那様` / `旦那さま` / `ご主人様` / `ご主人さま` / `ご主人`** | 主人 / 丈夫 / 先生 | **Chủ nhân** | ❌ Chồng, chồng bạn, thưa ngài, ông xã, Chủ nhân điện hạ |
| **`司令官`** | 司令官 | **Tư lệnh** / **anh Tư lệnh** | ❌ Chỉ huy, ngài chỉ huy |
| **`おにーさん` / `お兄さん`** *(Belisa gọi khi không cùng huyết thống)* | 大哥哥 / 哥哥 | **Oni-san** | ❌ Onii, Tekaonii, một onii, anh trai tôi |
| **`私` / `あたし` / `ボク` / `我`** | 我 | **Em** / **tôi** / **tại hạ** / **ta** *(tùy nhân vật)* | ❌ Bạn, người ấy |
| **`お前` / `君` / `貴様` / `其方`** | 你 / 汝 | **Anh** / **em** / **ngươi** *(tùy ngữ cảnh)* | ❌ Bạn, khách hàng |
| **`お客様`** *(trong bối cảnh kỹ viện)* | 客人 | **Vị khách** / **quý khách** | ❌ Khách hàng |

> 💡 **Lưu ý xưng hô tình cảm**: Trong các cảnh hẹn hò/tình cảm nam - nữ, tuyệt đối không dùng cặp từ thô cứng `bạn - tôi`. Hãy linh hoạt đổi thành `anh - em` hoặc `ta - em`.

---

## 3. THÁN TỪ & BIẾN ÂM RÊN RỈ

| Tiếng Nhật (JA) | Dịch Chuẩn Tiếng Việt | ❌ Lỗi Cần Tránh | Giải thích |
| :--- | :--- | :--- | :--- |
| **`え！？` / `え？` / `え……`** | **`Eh!?`** / **`Eh?`** / **`Eh……`** | ❌ Hình ảnh!?, bức tranh | Google Translate nhận nhầm `え` thành chữ Hán `絵` (tranh). Giữ nguyên Romaji. |
| **`ん？`** *(đầu câu hỏi)* | **`Hm?`** / **`Hửm?`** | ❌ Vâng?, đúng? | Dịch máy nhầm `ん` thành câu đồng ý `うん` (vâng). |
| **`らめ` / `らめぇ`** | **`K-Không được`** / **`Đừng mà`** | ❌ Rame, Rameee | Đây là biến âm nói đớt của `ダメ` (dame). |
| **`イグの` / `イグゥ`** | **`ra`** / **`ra với...`** | ❌ Iguno | Đây là biến âm nói đớt của `イク` (iku - lên đỉnh). |
| **`きもひいい`** | **`S-Sướng quá`** / **`Thích quá`** | ❌ Kimohiii | Nói đớt của `気持ちいい` (kimochi ii). |

---

## 4. QUY TẮC THUẬT NGỮ H-SCENE (18+)

Tuân thủ văn phong Visual Novel / Sắc hiệp / Dâm văn tiếng Việt:

| Thuật ngữ gốc (JA / ZH) | Dịch Chuẩn Tiếng Việt | ❌ Cụm từ thô cần tránh |
| :--- | :--- | :--- |
| 肉棒 / おちんぽ / 阴茎 / 大鸡鸡 | **dương vật** / **thanh thịt** | ❌ con gà trống, gà trống, cặc |
| 秘所 / 蜜穴 / 小穴 | **nơi thầm kín** / **môi dưới** | ❌ đôi môi riêng tư, đôi môi bí mật |
| 鈴口 / 尿道口 | **lỗ sáo** | ❌ từ Suzuguchi, lỗ sáo Suzuguchi |
| 愛液 / 淫液 / 蜜汁 | **dâm dịch** | ❌ nước ép tình yêu, dịch dâm |
| 精液 / 精子 / 白浊 | **tinh dịch** / **dòng tinh dịch** | ❌ con tinh trùng, chất tinh dịch |
| 膣内 / 膣壁 | **lòng âm đạo** / **thành âm đạo** | ❌ trong âm đạo |
| オナニー / 自慰 | **tự sướng** / **thủ dâm** | ❌ công việc thủ công |
| 挿入 / 挿れる / 插入 | **đút vào** / **cắm vào** / **tiến vào** | ❌ phần chèn, chèn |
| セックス / エッチ / 性行为 | **làm chuyện ấy** / **màn làm tình** / **mây mưa** | ❌ quan hệ tình dục, hành vi tình dục |
| 娼館 / 娼妓 | **kỹ viện** / **kỹ nữ** | ❌ nhà chứa, nhà thổ, gái mại dâm |

---

## 5. PHÂN BIỆT NỮ LÊN ĐỈNH VS NAM XUẤT TINH

Đây là lỗi dịch máy phổ biến và nghiêm trọng nhất cần đặc biệt lưu ý:

### 🚺 Nhân vật NỮ lên đỉnh (`イク` / `イグ` / `絶頂` / `高潮`):
- **TUYỆT ĐỐI KHÔNG DÙNG**: `bắn tinh`, `xuất tinh`, `Iguno`.
- **DỊCH ĐÚNG**: 
  - `イク、イクッ！` ➔ **"Em ra, em ra đâyyy!"** / **"Lên đỉnh rồi!"**
  - `イッちゃう` ➔ **"Sắp ra rồi!"** / **"Sắp lên đỉnh rồi!"**
  - `シャオレイもイク` ➔ **"Tiểu Lôi cũng ra đây!"**

### 🚹 Nhân vật NAM xuất tinh (`射精` / `出す` / `中出し` / `内射`):
- **DỊCH ĐÚNG**: 
  - `中にいっぱい出して` ➔ **"Bắn đầy vào bên trong em đi!"** / **"Hãy bắn vào trong em!"**
  - `射精する` ➔ **"phóng thích tinh dịch"** / **"bắn tinh vào sâu bên trong"**.

---

## 6. TÊN RIÊNG & GIỌNG ĐIỆU NHÂN VẬT

### 🏷️ Tên nhân vật (Giữ nguyên phiên âm Latinh):
có thể tham khảo từ file: `D:\idontknow\dotabyss-translation\translations\names\en.json`
- `ホノカ` (穗香) ➔ **Honoka**
- `ヘイリー` (海莉) ➔ **Hayley**
- `ベリサ` (贝丽莎) ➔ **Belisa**
- `エレクトラ` (厄勒克特拉) ➔ **Electra**
- `クルル` (克鲁鲁) ➔ **Kururu**
- `ルディア` (露迪亚) ➔ **Lydia** / **Rudia**
- `<user>` ➔ **`<user>`** *(Giữ nguyên tag)*

### 🎭 Giọng điệu (Persona) của từng nhân vật:
1. **Hayley (Chuunibyou - Hội chứng tuổi teen / Kỳ ảo)**:
   - Xưng: `Ta` (`吾`) - Gọi người khác: `Ngươi / Kẻ hèn mọn` (`汝 / 其方`).
   - Gọi Tư lệnh: **`Tư lệnh của ta`** (`吾之司令官 / 我がマスター`).
   - Giọng điệu: Kiếm hiệp, huyền huyễn, dùng từ Hán-Việt cổ phong (trừ lúc bị đâm sướng quá rớt vai về giọng nữ sinh hoảng loạn).
2. **Honoka (Năng động, ngây thơ nhưng dâm ngầm)**:
   - Xưng: `Em` hoặc gọi tên `Honoka`.
   - Giọng điệu: Tinh nghịch, hay rên nũng nịu (`汪呼` ➔ tiếng kêu cún con `Wafun♪ / Gâu♪`).
3. **Electra (Robot Sexaloid)**:
   - Xưng: `Electra`, gọi `Chủ nhân`.
   - Giọng điệu: Trang trọng, báo cáo thông số logic pha lẫn khoái cảm quá tải hệ thống.

---

## 7. QUY CHUẨN KỸ THUẬT & THẺ GAME

- **Thẻ Game & Placeholder**: Giữ nguyên vẹn 100% không làm mất hay sai chính tả:
  - `<user>` *(Tên người chơi)*
  - `<br>` *(Xuống dòng - không viết thành `<br/>` hay `<<br>br>`)*
  - `<size=48>...</size>`, `<color=yellow>...</color>`
  - `<ruby=マスター>司令官</>` ➔ bỏ thẻ ruby dịch thẳng nội dung tiếng việt vào vị trí của `司令官`.
- **Quy cách file JSON**:
  - Mã hóa: **UTF-8 (No BOM)**.
  - Định dạng: `indent=4`, `ensure_ascii=False`.
  - Kết thúc file có 1 dòng trống `\n`.

---

## 8. KINH NGHIỆM DỊCH: KẾT HỢP ZH & JA

Khi dịch các chương novel mới (`hmr_*`):
1. **Dùng bản Trung (ZH) làm sườn văn phong**: Tiếng Trung chuyển ngữ H-scene sang tiếng Việt cực kỳ tự nhiên, mượt mà, đầy đủ chủ ngữ vị ngữ.
2. **Đối chiếu bản Nhật (JA) để kiểm tra**:
   - Khôi phục tên Latinh (`Honoka`, `Hayley`).
   - Khôi phục thán từ Romaji (`Eh!?`, `Hm?`).
   - Chuẩn hóa đại từ xưng hô (`Tư lệnh`, `Chủ nhân`).
3. **Kiểm tra độ dài & ngắt dòng `<br>`**: Đảm bảo mỗi dòng dài **lên đến 70 ký tự** và **tối đa 1 thẻ `<br>`** (tối đa 2 dòng/hộp thoại).
4. **Chạy script kiểm tra tự động**:
   ```powershell
   # Quét kiểm tra lỗi:
   python tools/fix_hmr_translations.py --check

   # Tự động sửa lỗi hàng loạt:
   python tools/fix_hmr_translations.py --fix
   ```

---
*Tài liệu được cập nhật tự động đồng bộ cùng kịch bản `tools/fix_hmr_translations.py`.*
