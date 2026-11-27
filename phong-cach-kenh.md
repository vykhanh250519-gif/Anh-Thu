# Phong cách kênh: "Hồ sơ mật"

> File này **ghi đè** màu, chữ, chuyển cảnh và cách xuất file trong mục G của `mau-kich-ban-bodycam.md`, để video của kênh khác hẳn mẫu gốc.
> Bạn đã chọn: **tông màu Hồ sơ mật** + **chuyển cảnh Lật hồ sơ**. Phần chữ và xuất file bạn để mặc định, nên mình chọn phương án hợp với phong cách này. Muốn đổi thì sửa trực tiếp file này; agent đọc lại mỗi lần chạy.

## 1. Bảng màu

| Vai trò | Mã | Dùng cho |
|---|---|---|
| Giấy hồ sơ (nền chính) | `#E9DFC7` | Nền các cảnh đồ hoạ, thẻ thông tin, LEGAL |
| Giấy cũ (nền phụ) | `#D6C7A1` | Trang lót phía sau, mép giấy, bóng giấy chồng lên nhau |
| Than đen (chữ, nền tối) | `#1E1C1A` | Chữ chính trên giấy; nền tối thay cho `#0F1626` |
| Mực xanh đen (nét tay) | `#2B3A55` | Nét khoanh, gạch chân, ghi chú viết tay |
| Đỏ tem (nhấn) | `#B3261E` | Tem "CONFIDENTIAL", "CASE CLOSED", dấu ✕, chữ nhấn quan trọng; tối đa 1 điểm đỏ mỗi khung |
| Vàng kẹp giấy (phụ) | `#C9A227` | Kẹp giấy, băng dính, ghim bản đồ |

- Footage bodycam giữ màu gốc. Chỉ thêm viền giấy mỏng hoặc góc ảnh bị kẹp khi footage nằm "trên bàn hồ sơ".
- Phụ đề thoại: chữ trắng trên băng than đen 70%. Điều tra viên gạch đầu dòng xanh `#3A7BD5`, nghi phạm gạch đầu dòng đỏ tem `#B3261E`.

## 2. Bối cảnh thay thế (ghi đè G3)

| Mã | Mô tả mới |
|---|---|
| [DESK] | Mặt bàn gỗ tối nhìn từ trên xuống, ánh đèn bàn vàng ấm từ góc trên trái. Là "sân khấu" chung của toàn video |
| [FOLDER] | Bìa hồ sơ manila `#D6C7A1` có tab tên vụ, tem đỏ "CONFIDENTIAL" nghiêng 8° |
| [DARK] | Nền than `#1E1C1A`, vân giấy rất mờ 6%, vùng sáng tròn kiểu đèn bàn |
| [LEGAL] | Trang giấy `#E9DFC7` kẻ dòng, tiêu đề đánh máy, cán cân đóng dấu mực đỏ ở góc trên trái; thẻ án lệ là tờ giấy nhỏ ghim kẹp vàng |
| [CALENDAR] | Tờ lịch bàn giấy ngả màu, ngày được khoanh bằng mực xanh đen |
| [PHONE] | Giữ như mẫu (điện thoại phẳng không thương hiệu), đặt trên [DESK] |

Nhân vật 2D (G2) giữ nguyên quy tắc không vẽ mặt, nhưng đổ bóng như đang là hình cắt dán trên giấy (viền trắng 4 px kiểu ảnh cắt).

## 3. Chữ (mặc định, đổi được)

| Loại | Font | Hiệu ứng |
|---|---|---|
| Nhãn ngày giờ, địa điểm, tên | **Courier Prime** đậm (Google Fonts, miễn phí) | GÕ MÁY: hiện từng ký tự, 28 ký tự/giây, kèm tiếng máy chữ nhẹ |
| Tiêu đề lớn, số lớn, quote card | **Oswald** đậm (Google Fonts, miễn phí) | ĐÓNG DẤU: phóng 120% → 100% trong 0,25 s, mép mực hơi loang |
| Ghi chú tay, nét khoanh | **Caveat** (Google Fonts, miễn phí) | VIẾT TAY: nét hiện theo đường đi 0,8 s |

- Vùng chữ (G5) giữ nguyên: T, TL/TR, C, BL/BR, S; S chỉ cho phụ đề.
- Cỡ tối thiểu: 38 px chữ chính, 26 px chữ nhỏ.

## 4. Chuyển cảnh "Lật hồ sơ" (ghi đè G6)

| Từ khoá | Thực hiện | Dùng khi |
|---|---|---|
| LẬT TRANG | Trang hiện tại cong góc phải dưới và lật sang trái trong 0,6 s, ease-in-out; trang sau đã nằm sẵn bên dưới | Chuyển giữa 2 cảnh đồ hoạ trong cùng một phần |
| RÚT ẢNH | Ảnh/footage được kéo ra khỏi bìa hồ sơ theo hướng lên trên, 0,5 s, kèm bóng đổ dịch theo | Từ đồ hoạ vào footage bodycam |
| ĐẶT ẢNH | Footage thu nhỏ còn 70%, xoay nhẹ 3°, rơi xuống [DESK] như ảnh in, 0,5 s | Từ footage ra đồ hoạ |
| ĐÓNG DẤU | Tem đỏ đập xuống giữa khung (ĐẬP 120%→100%, 0,25 s), giữ 0,6 s | Chuyển phần lớn (HOOK→SETUP…), câu chốt, bản án |
| ĐÓNG HỒ SƠ | Bìa manila gập lại, tab tên vụ còn nhìn thấy, 0,8 s | Kết video, trước end card |
| KẸP GHIM | Thẻ chữ trượt vào rồi một kẹp giấy vàng bấm xuống mép thẻ, 0,4 s | Thay cho TRƯỢT của thẻ thông tin |

- Giữ các từ khoá cũ HIỆN DẦN, ĐẨY MÁY, VẼ NÉT, ĐẾM, ĐI cho chuyển động bên trong một cảnh.
- **Không lặp một kiểu chuyển cảnh quá 3 lần liên tiếp.** Xen kẽ LẬT TRANG / RÚT ẢNH / ĐẶT ẢNH.
- Chuyển vào cảnh sóng âm (skill `cold-open-waveform`): dùng RÚT ẢNH như rút cuộn băng ghi âm ra khỏi bìa, thay cho glitch/flash.

**Gợi ý SFX đi kèm** (không bắt buộc, chỉnh theo tai): lật giấy, tiếng đóng dấu nặng, máy chữ, kẹp ghim, ngăn kéo tủ hồ sơ khi đóng hồ sơ.

## 5. Xuất file (mặc định, đổi được)

- Mỗi vụ một thư mục: `<MÃVỤ>/` (ví dụ `STEDMAN/`).
- Tên file có tiền tố vụ và phần: `STEDMAN_P1_A01.mp4`, `STEDMAN_P3_G04.mov` (P1 = HOOK … P5 = AFTERMATH). Graphic đè clip vẫn là `.mov` có kênh alpha.
- Xuất **2 lượt**:
  1. **Nháp 720p** (`_draft`) để duyệt nhanh nhịp và chữ;
  2. **Bản cuối 1920×1080**, H.264 ≥ 12 Mbps (hoặc 4K nếu footage gốc đủ nét).
- Kịch bản xuất thành file `.md` (hoặc Google Docs nếu bạn yêu cầu) đặt cùng thư mục vụ, tên `<MÃVỤ>_kich-ban.md`.
