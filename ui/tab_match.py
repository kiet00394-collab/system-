import streamlit as st
import pandas as pd
from matching import gale_shapley, count_blocking_pairs, merge_pairs_into_rooms

def render():
    st.header("Tab 2: Ghép phòng Ký túc xá")
    
    # Kiểm tra xem dữ liệu từ Tab 1 đã được nạp vào session_state chưa
    if "pref_a" not in st.session_state:
        st.warning("⚠️ Hãy nạp dữ liệu và tính toán điểm tương thích ở Tab 1 (Dữ liệu) trước.")
        return

    S = st.session_state["students"]
    M = st.session_state["M"]
    pa = st.session_state["pref_a"]
    pb = st.session_state["pref_b"]

    # Tùy chọn quy mô phòng
    room_type = st.selectbox("Chọn quy mô phòng KTX:", ["2 người/phòng", "4 người/phòng"])

    # Nút thực thi ghép phòng
    if st.button("Chạy thuật toán ghép phòng"):
        match = gale_shapley(pa, pb)
        st.session_state["match"] = match
        st.success("Đã chạy thuật toán ghép phòng thành công!")

    match = st.session_state.get("match")
    if match:
        if room_type == "2 người/phòng":
            rows = [
                {
                    "Phòng": i + 1,
                    "SV nhóm A": S[a].name,
                    "SV nhóm B": S[b].name,
                    "A đánh giá B": round(M[a][b], 1),
                    "B đánh giá A": round(M[b][a], 1)
                }
                for i, (a, b) in enumerate(match.items())
            ]
            st.dataframe(pd.DataFrame(rows), use_container_width=True)
            
            # Hiển thị chỉ số đánh giá độ ổn định NFR-02
            bp = count_blocking_pairs(match, pa, pb)
            st.metric("Số cặp chặn (Blocking Pairs - 0 là tuyệt đối ổn định)", bp)
            
        else:
            rooms_4 = merge_pairs_into_rooms(match, M, room_size=4)
            rows = [
                {
                    "Phòng": i + 1,
                    "Thành viên trong phòng": ", ".join(f"{S[uid].name} (Nhóm {S[uid].group})" for uid in r)
                }
                for i, r in enumerate(rooms_4)
            ]
            st.dataframe(pd.DataFrame(rows), use_container_width=True)
            bp = count_blocking_pairs(match, pa, pb)
            st.metric("Số cặp chặn gốc (Gale-Shapley)", bp)