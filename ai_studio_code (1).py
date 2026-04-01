import streamlit as st

# 1. Dữ liệu tri thức về trường Đại học Đồng Tháp (Bạn có thể mở rộng thêm)
knowledge_base = {
    "địa chỉ": "Trường Đại học Đồng Tháp tọa lạc tại số 783, đường Phạm Hữu Lầu, Phường 6, TP. Cao Lãnh, Đồng Tháp.",
    "website": "Website chính thức của trường là: https://www.dthu.edu.vn/",
    "khoa": "Trường có các khoa tiêu biểu như: Khoa CNTT, Khoa Sư phạm Toán - Tin, Khoa Kinh tế, Khoa Ngoại ngữ, Khoa Nông nghiệp & Tài nguyên môi trường...",
    "tín chỉ": "Quy chế tín chỉ: Sinh viên cần tích lũy đủ số tín chỉ theo khung chương trình đào tạo của mỗi ngành. Điểm đạt là từ điểm D trở lên.",
    "học bổng": "Trường có học bổng khuyến khích học tập dựa trên kết quả học tập và rèn luyện mỗi học kỳ. Các mức: Khá, Giỏi, Xuất sắc.",
    "liên hệ": "Số điện thoại hỗ trợ: (0277) 3881518. Email: dhdt@dthu.edu.vn",
    "phòng học": "Khu A là khu hiệu bộ, Khu B và C thường là các phòng học lý thuyết. Khu thực hành CNTT nằm ở tầng 3-4 tòa nhà C.",
}

# 2. Hàm xử lý tìm câu trả lời
def get_answer(question):
    question = question.lower()
    for key in knowledge_base:
        if key in question:
            return knowledge_base[key]
    return "Xin lỗi, mình chưa có thông tin về câu hỏi này. Bạn hãy thử hỏi về 'địa chỉ', 'các khoa', 'học bổng' hoặc 'quy chế tín chỉ' nhé!"

# 3. Giao diện ứng dụng Streamlit
def main():
    st.set_page_config(page_title="DThU Smart Assistant", page_icon="🎓")
    
    # CSS để làm đẹp giao diện theo màu xanh DThU
    st.markdown("""
        <style>
        .main { background-color: #f0f2f6; }
        .stButton>button { background-color: #0056b3; color: white; }
        </style>
    """, unsafe_allow_html=True)

    st.title("🎓 Trợ lý ảo Sinh viên DThU")
    st.subheader("Hỗ trợ giải đáp thắc mắc học tập & quy chế")

    # Khởi tạo lịch sử chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Hiển thị lịch sử chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Ô nhập câu hỏi
    if prompt := st.chat_input("Bạn muốn hỏi gì về trường mình?"):
        # Lưu câu hỏi người dùng
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Xử lý trả lời
        response = get_answer(prompt)
        
        # Hiển thị câu trả lời
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()