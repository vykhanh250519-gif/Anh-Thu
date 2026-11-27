# Mẫu kịch bản edit video Body Cam (chuẩn của kênh)

> Rút từ tài liệu mẫu "6. Kịch bản edit video Body Cam" (vụ Megan Stedman / Chris Foiles, ~25:12, thị trường US, đã có bản án).
> Agent `agent_true_crime.py` đọc file này mỗi lần chạy và viết kịch bản đúng khuôn này.

## Dòng đầu
`<Số>. Kịch bản edit video Body Cam` · Tên vụ — địa điểm (thời gian xảy ra → thời gian tuyên án) · Thời lượng dự kiến · Thị trường: US · Trạng thái pháp lý (ĐÃ CÓ BẢN ÁN / ĐANG XÉT XỬ)

## A. Thông tin tiêu đề & thumbnail
- 5 phương án tiêu đề tiếng Anh. Công thức chủ đạo là **trớ trêu kịch tính**: **[Nhân vật + "lời tự nhận" trong ngoặc kép] Has No Idea [điều cảnh sát/người khác đã biết]**. Ví dụ:
  - "Just Passing Through" Driver Has No Idea A UPS Driver Already Recognized His Repainted RV
  - Man With A Fake Name Has No Idea Officers Are Holding His Real Photo
  - Montana Man Has No Idea One Delivery Driver Just Ended A Month-Long Manhunt
- Thumbnail: chữ ngắn kiểu "FRESH PAINT. FAKE NAME." + 1 ảnh bodycam ngoại cảnh (làm mờ biển số, nhà). Ghi rõ những thứ **TUYỆT ĐỐI KHÔNG** dùng: ảnh bên trong hiện trường, cụm từ gắt (vd "from Hell"), ảnh nạn nhân.

## B. Hồ sơ vụ án (đã đối chiếu nguồn)
Bảng 3 cột: **Hạng mục | Dữ liệu | Nguồn**. Các hạng mục thường có: Nạn nhân, Bị cáo (ghi cả lỗi chính tả của phụ đề tự động), lệnh cấm tiếp xúc / tiền án, ngày xảy ra án, phát hiện, tên giả, lời thú nhận, khám xét, che giấu, nơi xét xử, tội danh, nhận tội, bản án, trước vụ án, điện thoại, gia đình tìm kiếm, video camera, bảo lãnh.
- Nguồn không khớp nhau thì ghi rõ **"NGUỒN KHÔNG KHỚP"** và nêu cả hai.
- Thông tin không được nói trong video thì ghi **KHÔNG đọc / KHÔNG nêu tên** (tên giả có thể trùng người thật, tên người nhà, tên con).
- Hộp cảnh báo ⚠ cuối mục: tình trạng bản án/kháng cáo, mâu thuẫn số liệu cần xin hồ sơ toà, các đoạn Ref **KHÔNG được phát** (bên trong hiện trường, mô tả hành vi, phi tang).

## C. Kịch bản dựng chi tiết
Bảng 8 cột: **Thời gian | Phân đoạn | Hình ảnh / Lệnh dựng | Âm thanh / SFX | Loại | Lời thuyết minh (VO) – English | Tiếng Việt | Ghi chú edit**

5 loại ô (cột "Loại"):
| Loại | Nghĩa |
|---|---|
| LỜI DẪN (ô vàng) | Phần người đọc thuyết minh, đọc theo cột English |
| AUDIO CLIP (ô trắng) | Thoại gốc, không đọc. Ghi `Ref <nguồn> <mm:ss>` và vai "Officer:", "Man:", "Officer 2:" |
| GRAPHIC (ô xám) | Đồ hoạ đè lên audio clip ngay trên, mã `G01, G02…` |
| LỆNH ANIMATION (ô xanh) | Lệnh dựng cảnh cho câu lời dẫn cùng hàng, mã `A01 · 0:00–0:07` |
| LEGAL BREAKDOWN (nền cam) | Đoạn phân tích pháp lý, dùng chung 1 template đồ hoạ |

5 phần (tỉ lệ theo mẫu 25 phút; video dài hơn thì giãn đều):
1. **THE HOOK** (~0:00–1:00): chuỗi audio clip gắt nhất (vd "Not going to lie. My name is Chris." → "You killed your girlfriend…?" → "Yeah."), rồi 3–4 câu lời dẫn, câu cuối hứa hẹn: *"By the end of this video, you'll know…"*.
2. **THE SETUP** (~1:00–1:42): ngày giờ, địa điểm, người phát hiện, cảnh sát tới.
3. **THE ESCALATION**: chia thành các **nấc** ("Nấc 1 — Chiếc xe được sơn lại"…), mỗi nấc xen kẽ audio clip ↔ lời dẫn phân tích chi tiết chứng cứ.
4. **THE CLIMAX**: lời thú nhận / bị lật tẩy, khám xét.
5. **THE AFTERMATH**: điều tra sau đó, đổi nơi xét xử, tội danh, nhận tội, bản án, các đoạn LEGAL BREAKDOWN, end card.

Cách viết lệnh animation (ô xanh): mỗi cảnh ghi đủ **Nền / Nhân vật / Máy quay / Động tác / Chữ / Nối**, dùng mã bối cảnh và nhân vật ở mục G, từ khoá chuyển động viết hoa (HIỆN DẦN, TRƯỢT, ĐẨY MÁY, VẼ NÉT, ĐẬP, ĐẾM, ĐI), động tác khớp với **từ** trong lời đọc ("khi đọc 'painted'"). Ví dụ:
> A03 · 0:08–0:16 · Nền: giữ [RV-DAY], khung thân xe. Nhân vật: không có. Máy quay: đẩy nhẹ vào sọc. Động tác: sọc đỏ được quét phủ thành xanh khi đọc "painted". Chữ: vùng TL, "RED → BLUE". Nối: chữ mờ hết, hoà mờ ra footage.

Ghi chú footage: "Footage gốc theo Ref ở cột Loại. Làm mờ biển số, che logo <kênh nguồn>."

## D. Bảng tra cứu pháp lý (cho text card)
Bảng **Vấn đề | Điều luật / Án lệ | Nội dung hiển thị**. Điều đã đối chiếu đánh ✓; chưa đối chiếu ghi rõ "(chưa đối chiếu)".

## E. Checklist trước khi xuất bản
Phụ đề (nghe lại các mốc Ref nghi lỗi), số liệu pháp lý cần xin hồ sơ, hình ảnh (không khung hiện trường, làm mờ người ngoài cuộc, biển số, số nhà, màn hình điện thoại; che logo nguồn), âm thanh (mute đoạn nhạy cảm, bleep từ tục, cân nhắc bleep "killed"), nạn nhân (không ảnh nếu chưa có phép gia đình), kiếm tiền (chủ đề dễ bị giới hạn), bản quyền (không dùng lại phần dựng / giọng đọc của kênh nguồn, xin footage gốc từ sở cảnh sát), những điều không được nhắc, end card đường dây nóng (vd National DV Hotline 1-800-799-7233) hiển thị đủ 5 giây.

## F. Nguồn
Danh sách: Tên báo — tiêu đề bài (ngày): URL. Nguồn bị chặn chỉ đọc được tiêu đề thì ghi rõ.

## G. Lệnh cho Claude khi dựng hình ảnh
- **G1. Cách đọc một cảnh:** mã file · mốc giây (ước tính 2,5 từ/giây; có file thu âm thì canh theo từ).
- **G2. Bảng nhân vật:** 2D phẳng, cao 7 đầu, **không vẽ mắt mũi miệng**, mã [SUSPECT], [VICTIM], [OFFICER], [DETECTIVE], [JUDGE]… kèm màu da, tóc, trang phục (mã hex), tư thế được dùng. Không vẽ hành vi gây án, thi thể, thương tích, vũ khí, máu.
- **G3. Bối cảnh:** dựng một lần, dùng lại ([DARK] nền #0F1626, [LEGAL] thanh vàng #FFD54A, [PHONE], [CALENDAR], [INTERVIEW], [COURT]… và bối cảnh riêng của vụ). Không biển số, không số nhà, không logo.
- **G4. Bản đồ:** chỉ nguồn được phép (Natural Earth, Landsat/USGS, NAIP, TIGER/Line; OSM/Sentinel phải ghi công). Cấm chụp Google Maps. Bảng mã [M1]… với khung đầu/cuối, toạ độ, nhãn.
- **G5. Vùng chữ:** T, TL/TR, C, BL/BR, S (S chỉ cho phụ đề). Tối đa 2 khối chữ mỗi lúc, 7 từ/dòng, 3 dòng/khối. Font Inter/Arial đậm, ≥36 px; trắng, nhấn vàng #FFD54A, đỏ #E5484D chỉ cho dấu/nét.
- **G6. Chuyển động:** định nghĩa từ khoá (HIỆN DẦN 0,4 s; TRƯỢT 0,6 s; ĐẬP 112→100% 0,35 s; ĐẨY MÁY 100→108%; VẼ NÉT 0,8 s…), nối cảnh liền mạch, 1920×1080, đặt tên A01.mp4 / G01.mov.
- **G7. Kiểm tra bắt buộc trước khi xuất:** va chạm chữ, khung trùng, màu nhân vật, bản đồ, nội dung cấm. Không chắc thì dừng và hỏi.

## Cảnh sóng âm (skill `cold-open-waveform`)
Khi kịch bản có câu thoại gốc then chốt mà băng chỉ có tiếng, hình kém hoặc cần nhấn mạnh (cold open luôn là cường độ 5), ghi ở cột Hình ảnh: `WAVE · tc-coldopen-wave` (hoặc `tc-wave-2`…), mỗi cảnh ≤ 15 s, kèm vai người nói (police/suspect) và mốc Ref để dựng bằng skill sóng âm.
