# Chiến lược xây kênh True Crime (khán giả Mỹ)

> Nghiên cứu ngày 27/11/2026 qua tìm kiếm web. Trang YouTube của 3 kênh tham khảo không đọc được bằng công cụ tự động (chỉ trả về khung trang trống), nên số liệu của File 187, Dr Insanity, DOCS 187 cần bạn tự kiểm tra (xem mục 6).

## 1. Bản đồ đối thủ

| Kênh | Định dạng | Bài học |
|---|---|---|
| **Dr Insanity** | Ghép bodycam / footage vụ việc thành phim tài liệu kể trọn vụ án | Một bài tổng hợp năm 2026 cho rằng kênh có lượt xem mỗi video mới cao nhất ngách. Format "kể trọn một vụ" vẫn hút. |
| **EWU – Explore With Us** | Series Bodycam & Interrogation, nhiều video dài hơn 2 giờ | **Bị tắt kiếm tiền (Dexerto, 30/10/2026)** với lý do nội dung lặp lại / chung chung. Đây là cảnh báo lớn nhất của ngách. |
| **JCS – Criminal Psychology** | Phân tích tâm lý video thẩm vấn, rất kỹ | Một nguồn ghi khoảng 500 triệu view chỉ với khoảng 25 video. Nguồn này cũng nói kênh không đăng từ 12/2025 (một nguồn khác bảo đăng không đều). Chất lượng phân tích thắng số lượng. |
| **Law&Crime Interrogations** | Footage thẩm vấn thô + lời bình chuyên gia | Phiên bản "công nghiệp" của ngách, cạnh tranh trực tiếp về tốc độ ra vụ mới. |
| File 187, DOCS 187 | Chưa xác minh được | Cùng hệ đặt tên "187", là mã cảnh sát California cho tội giết người. |

## 2. Khoảng trống để chen vào

- Khán giả của JCS có thể đang thiếu nội dung mới: kiểu **phân tích thẩm vấn sâu như JCS**, nhưng có **lịch đăng đều**.
- Mô hình "ghép footage dài" đang bị YouTube siết. **Kênh mới phải là kênh phân tích, không phải kênh tổng hợp footage.**

→ **Định vị đề xuất:** kênh *phân tích tâm lý và lời nói dối* trong các vụ án mạng có thật. Footage cảnh sát chỉ là bằng chứng minh hoạ cho lời dẫn.

## 3. Ba trụ nội dung

| Trụ | Thời lượng | Tỷ lệ | Vai trò |
|---|---|---|---|
| **Interrogation Breakdown**: phân tích thẩm vấn, mổ xẻ từng lời nói dối | 35–40 phút | 60% | Trụ chính, RPM cao, thời gian xem dài |
| **Full Case Documentary**: bodycam → điều tra → thẩm vấn → toà | 35–40 phút | 30% | Thu hút người xem mới, dễ được đề xuất |
| **Shorts**: 1 khoảnh khắc lật tẩy, 45–60 giây | Ngắn | 3–5 Shorts / video dài | Kéo người xem về video dài (dùng `agent_kich_ban.py`) |

## 4. Quy tắc sống còn (rút từ vụ EWU)

1. **Lời dẫn và phân tích phủ kín video.** Footage thô không chạy quá 60–90 giây liền.
2. **Mỗi video có thứ người khác không có:** dòng thời gian, bản đồ, bảng "lời khai vs bằng chứng", chú thích ngôn ngữ cơ thể.
3. **Không làm hàng loạt bằng một khuôn y hệt.** Thay đổi cấu trúc, góc nhìn và mở đầu giữa các video. Nếu dùng giọng AI, kịch bản càng phải có cá tính.
4. **Không có hình ảnh gây sốc:** làm mờ thi thể và máu, tắt tiếng chửi thề. Một số hướng dẫn thứ cấp nói đầu năm 2026 YouTube nới kiếm tiền cho chủ đề nhạy cảm *không có hình ảnh gây sốc*. Bạn nên kiểm tra lại trên trang chính sách chính thức.
5. **Footage lấy từ nguồn gốc:** kênh chính thức của sở cảnh sát, yêu cầu hồ sơ công khai (FOIA), hồ sơ toà án. Không tải lại từ kênh đối thủ.

## 5. Quy trình sản xuất 1 video / tuần

Theo nguyên tắc 20/80 trong sổ tay: bạn tự làm 20% quan trọng nhất, phần còn lại thuê.

| Ngày | Việc | Ai làm |
|---|---|---|
| T2 | Chọn vụ án (đã có bản án, có video thẩm vấn công khai, động cơ tiền bạc / gia đình / bí mật), gom tài liệu | **Bạn** |
| T3 | Chạy `agent_true_crime.py` → kịch bản; tự kiểm tra mọi chỗ `[VERIFY]` | **Bạn** + agent |
| T4 | Thu âm lời dẫn | Tự đọc / thuê giọng / giọng AI |
| T4–T6 | Dựng: footage, đồ hoạ, làm mờ, tắt tiếng | Thuê editor |
| T6 | Tiêu đề + thumbnail theo công thức ngòi nổ (đã có trong agent), làm 2 bản để A/B test | **Bạn** |
| T7 | Đăng, cắt 3–5 Shorts | Editor + agent |
| CN | Xem Analytics: CTR, thời lượng xem trung bình, điểm người xem rời đi → ghi lại để sửa video sau | **Bạn** |

## 6. Việc bạn làm với Gmail mới (thay cho bước "xem bằng Chrome")

1. Mở từng kênh: File 187, Dr Insanity, DOCS 187, JCS, Law&Crime → tab **Videos → Phổ biến nhất**.
2. Chép **18 tiêu đề nhiều view nhất** mỗi kênh (theo phương pháp Dream 100 trong sổ tay), kèm số view và thời lượng.
3. Chụp màn hình lưới thumbnail.
4. Gửi lại cho Claude → phân tích ra: ngòi nổ lặp lại, công thức tiêu đề, bảng màu và bố cục thumbnail, độ dài video tối ưu. Kết quả cập nhật vào `title_rules.py`.

## 7. Mục tiêu 90 ngày đầu

- 12 video dài + 40–60 Shorts.
- Video 1–3: chọn vụ có "lời nói dối bị lật tẩy" rõ nhất, vì đây là thứ khán giả ngách thích xem lại.
- Sau mỗi 4 video, so sánh Analytics để giữ trụ nội dung nào chạy tốt nhất và nhân đôi trụ đó.

## Nguồn

- [Dexerto – EWU bị tắt kiếm tiền](https://www.dexerto.com/youtube/true-crime-channel-ewu-slams-youtubes-extreme-censorship-after-losing-monetization-3423385/)
- [10 Best True Crime YouTube Channels 2026 – Vidpros](https://vidpros.com/best-true-crime-youtube-channels/)
- [35 Best True Crime YouTube Channels 2026 – Mystery Tribune](https://mysterytribune.com/35-best-true-crime-youtube-channels-in-2026/)
- [29 Best True Crime YouTubers 2026 – ThoughtLeaders](https://www.thoughtleaders.io/blog/best-true-crime-youtubers)
- [Law&Crime Interrogations – Jellysmack](https://blog.jellysmack.com/new-youtube-channel-lawcrime-interrogations/)
- [YouTube Reused Content Policy 2026](https://channelterminated.com/demonetized/reused-content/)
- [YouTube Monetization Policy Updates 2026 – ScaleLab](https://scalelab.com/en/youtube-monetization-policy-updates)
