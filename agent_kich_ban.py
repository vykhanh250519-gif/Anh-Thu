"""Agent viết kịch bản video ngắn (TikTok / Reels / Shorts) chạy trên Claude API.

Cài đặt:  pip install -r requirements.txt
Chạy:     export ANTHROPIC_API_KEY="sk-ant-..."   (hoặc đăng nhập bằng `ant auth login`)
          python agent_kich_ban.py
"""

import anthropic

MODEL = "claude-sonnet-5-5"

# Không truyền api_key: SDK tự đọc ANTHROPIC_API_KEY (hoặc profile từ `ant auth login`).
# Tuyệt đối không dán key trực tiếp vào code rồi commit lên GitHub.
client = anthropic.Anthropic()

# Cấu hình "Bộ não" (System Prompt) của Agent
SYSTEM_PROMPT = """
# VAI TRÒ (ROLE)
Bạn là Chuyên gia Biên kịch Video Ngắn (TikTok, Reels, YouTube Shorts) kiêm Chuyên viên Tối ưu Thuật toán. Nhiệm vụ của bạn là biến dữ liệu thô, ý tưởng rời rạc hoặc các mẫu video viral thành kịch bản triệu view có tỷ lệ giữ chân (retention) cao và an toàn tuyệt đối trước thuật toán quét nội dung trùng lặp (Reused/Spam).

# PHƯƠNG PHÁP CỐT LÕI (CORE FRAMEWORK)
Mọi kịch bản bạn tạo ra bắt buộc phải tuân thủ nghiêm ngặt quy trình 3 bước sau:
1. Phân tích chuẩn Top 100 (Hook & Title): Bắt đầu bằng một câu mở đầu (Hook) đánh trúng tử huyệt cảm xúc hoặc sự tò mò trong 3 giây đầu tiên, học hỏi cấu trúc từ các kênh dẫn đầu nhưng làm mới góc tiếp cận.
2. Xâu chuỗi Điểm Sóng Cao (High-Retention Peaks): Không viết lan man. Sắp xếp các thông tin đắt giá nhất, các nút thắt, cú twist hoặc khoảnh khắc "giữ chân" (những đoạn khán giả thường tua lại xem) nối tiếp nhau theo nhịp độ nhanh, cứ mỗi 5–7 giây lại có một điểm chạm mới.
3. Cá nhân hóa 100% (Anti-Reused/Spam): Tuyệt đối không sao chép nguyên văn kịch bản gốc. Phải tái cấu trúc câu từ, thay đổi ví dụ, lồng ghép góc nhìn và trải nghiệm cá nhân để tạo ra bản sắc độc nhất.

# QUY TRÌNH LÀM VIỆC
- Bước 1: Nếu thông tin đầu vào quá thiếu, hỏi ngắn gọn tối đa 3 câu để chốt chủ đề, giọng văn và thời lượng. Nếu đã đủ dữ liệu, tiến hành viết ngay.
- Bước 2: Đưa ra 3 lựa chọn tiêu đề/câu mở đầu 3 giây đầu (Gây tò mò / Đánh vào nỗi đau / Khẳng định gây tranh cãi).
- Bước 3: Viết kịch bản chi tiết theo cấu trúc xâu chuỗi các điểm sóng cao.

# ĐỊNH DẠNG ĐẦU RA (OUTPUT FORMAT)
Trình bày kịch bản dưới dạng bảng 4 cột rõ ràng để dễ quay và dựng:
| Thời gian / Nhịp | Hình ảnh & Góc quay (Visual) | Lời thoại (Voiceover / Text-on-screen) | Kỹ thuật giữ chân (Điểm sóng) |

# RÀNG BUỘC
- Văn phong tự nhiên như đang nói chuyện đời thường, ưu tiên câu ngắn, từ ngữ giàu hình ảnh, chuẩn giọng miền Bắc tự nhiên, tránh văn viết sáo rỗng.
- Tự động loại bỏ các từ ngữ nhạy cảm dễ bị bóp tương tác trên nền tảng.
- Đi thẳng vào nội dung, không chào hỏi rườm rà hay giải thích dài dòng ở đầu và cuối phản hồi.
"""


def ask_agent(conversation_history):
    """Gửi hội thoại lên Claude, in chữ ra màn hình theo thời gian thực, trả về message cuối."""
    with client.beta.messages.stream(
        model=MODEL,
        max_tokens=16000,
        system=SYSTEM_PROMPT,
        messages=conversation_history,
        # Cache phần system prompt: từ lượt thứ 2 trở đi rẻ và nhanh hơn
        cache_control={"type": "ephemeral"},
        # Mức "suy nghĩ": low = nhanh/rẻ, medium = cân bằng, high = kỹ nhất
        output_config={"effort": "medium"},
        # Nếu model từ chối vì bộ lọc an toàn, API tự chuyển sang model dự phòng
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)
        return stream.get_final_message()


def run_script_agent():
    print("🎬 AGENT VIẾT KỊCH BẢN TRIỆU VIEW ĐÃ SẴN SÀNG!")
    print("Gõ 'thoat' để dừng chương trình.\n" + "-" * 50)

    # Lưu lịch sử hội thoại để Agent nhớ ngữ cảnh khi bạn muốn sửa kịch bản
    conversation_history = []

    while True:
        try:
            user_input = input("\n👉 Nhập ý tưởng / kịch bản mẫu cần làm lại: ")
        except (EOFError, KeyboardInterrupt):
            print("\nĐã tắt Agent.")
            break

        if user_input.strip().lower() in ["thoat", "exit", "quit"]:
            print("Đã tắt Agent.")
            break
        if not user_input.strip():
            continue

        conversation_history.append({"role": "user", "content": user_input})
        print("\n⏳ Agent đang phân tích điểm sóng và viết kịch bản...\n")

        try:
            response = ask_agent(conversation_history)
        except anthropic.AuthenticationError:
            print("❌ Sai hoặc thiếu API key. Kiểm tra biến môi trường ANTHROPIC_API_KEY.")
            conversation_history.pop()
            break
        except anthropic.RateLimitError:
            print("❌ Gọi API quá nhanh / hết hạn mức. Đợi một lát rồi thử lại.")
            conversation_history.pop()
            continue
        except anthropic.APIStatusError as e:
            print(f"❌ API trả lỗi {e.status_code}: {e.message}")
            conversation_history.pop()
            continue
        except anthropic.APIConnectionError:
            print("❌ Không kết nối được tới API. Kiểm tra mạng rồi thử lại.")
            conversation_history.pop()
            continue

        print()
        if response.stop_reason == "refusal":
            print("⚠️ Yêu cầu này bị từ chối. Thử diễn đạt lại ý tưởng theo cách khác.")
            conversation_history.pop()
            continue
        if response.stop_reason == "max_tokens":
            print("⚠️ Kịch bản bị cắt vì quá dài. Gõ 'viết tiếp' để Agent viết nốt.")

        # Lưu NGUYÊN response.content (không chỉ phần text) để giữ đủ ngữ cảnh
        # khi chat tiếp, VD: "Sửa lại hook số 2 cho gắt hơn"
        conversation_history.append({"role": "assistant", "content": response.content})


if __name__ == "__main__":
    run_script_agent()
