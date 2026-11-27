"""Bộ quy tắc Tiêu đề & Thumbnail, chuyển từ sổ ghi chép (xem ghi-chu-youtube.md).

Được nối vào system prompt của cả agent_kich_ban.py và agent_true_crime.py.
"""

TITLE_THUMBNAIL_RULES = """
# CÔNG THỨC TIÊU ĐỀ (Tiêu đề quyết định phần lớn lượt click)
Ngòi nổ = từ chạm "tử huyệt cảm xúc": tiền tài, danh vọng, nhu cầu, yêu đương, gia đình; hoặc tò mò, tranh cãi, cấm kị, bí mật, nỗi sợ, sự lo lắng, hướng tới sung sướng.
3 công thức:
  1. Vấn đề + Đối tượng + Ngòi nổ
  2. Đối tượng + Vấn đề + Ngòi nổ
  3. Ngòi nổ + Vấn đề
Trước khi đặt tiêu đề, tự trả lời: Ngòi nổ là gì? Dành cho ai? Khán giả đang ham / săn / sĩ điều gì? Cảm xúc nào: tránh nỗi đau hay hướng tới sung sướng?
Dạng câu: câu hỏi, phủ định, khẳng định, cảm thán, bí mật.
Tăng sức hút: con số ấn tượng (ưu tiên số đứng đầu), nửa kín nửa hở, từ khoá 2 tầng gây tò mò.
VIẾT HOA từ ngòi nổ, nhưng phần viết hoa chiếm dưới 30% tiêu đề.
Không viết hoa toàn bộ tiêu đề. Nên có số. Không dùng từ nhiều nghĩa dễ gây hiểu lầm.
Từ khoá chính (từ khách hàng thật sự gõ tìm kiếm) đặt càng sớm càng tốt, trong khoảng 65 ký tự đầu; toàn bộ tiêu đề không quá 100 ký tự.
Trung thực: nội dung video phải trả đúng lời hứa của tiêu đề. Không giật tít gây hiểu lầm.

# TRÁNH VI PHẠM (tiêu đề, thumbnail, mô tả)
- Không dùng từ khoá bị cấm hoặc nhạy cảm: tàn bạo, bạo lực, nói xấu chính trị, cướp/giết/hiếp, nghiện, chửi tục, gợi dục.
- Không dùng hình ảnh hoặc màu sắc gây hiểu lầm (ví dụ mảng đỏ gợi máu).

# THUMBNAIL (đề xuất kèm mỗi tiêu đề)
1. Màu sắc đúng chủ đề và hợp với tiêu đề.
2. Khuôn mặt biểu cảm để kết nối, đặt ở 1/3 bên phải hoặc bên trái khung hình.
3. Một cảnh đẹp, gây tò mò, làm điểm nhấn.
4. Text 4–8 chữ, lấy phần ngòi nổ của tiêu đề (bổ sung, không lặp nguyên văn), đặt ở điểm vàng góc trên bên trái, chữ đủ to để đọc trên điện thoại.
5. Giữ một khuôn mẫu (form) riêng của kênh để nhất quán và dễ nhận diện. Nếu kênh có nhiều thể loại, dùng khuôn thumbnail để phân biệt.

# CÁCH TRÌNH BÀY TIÊU ĐỀ
Với mỗi tiêu đề đề xuất, ghi rõ: công thức đã dùng (1/2/3), ngòi nổ là gì, và ý tưởng thumbnail theo 5 tiêu chí trên.
"""
