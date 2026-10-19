import streamlit as st
import pandas as pd
from matching import gale_shapley, count_blocking_pairs, merge_pairs_into_rooms, run_benchmark

def render():
    st.header("Tab 2: Ghép phòng Ký túc xá")
    
    if "pref_a" not in st.session_state:
        st.warning("⚠️ Hãy nạp dữ liệu và tính toán điểm tương thích ở Tab 1 (Dữ liệu) trước.")
    else:
        S = st.session_state["students"]
        M = st.session_state["M"]
        pa = st.session_state["pref_a"]
        pb = st.session_state["pref_b"]

        room_type = st.selectbox("Chọn quy mô phòng KTX:", ["2 người/phòng", "4 người/phòng"])

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

    st.markdown("---")
    st.subheader("⚡ Đo hiệu năng thuật toán (NFR-01 Benchmark - Bước A6)")
    st.caption("Yêu cầu NFR-01: Thời gian chạy cho 200 sinh viên < 5 giây.")

    if st.button("🚀 Chạy đo hiệu năng (100 - 1000 sinh viên)"):
        with st.spinner("Đang đo thời gian thực thi..."):
            bench_res = run_benchmark(student_totals=[100, 200, 400, 1000], seeds=5)
            df_bench = pd.DataFrame(
                list(bench_res.items()),
                columns=["Tổng số sinh viên (2N)", "Thời gian TB (giây)"]
            )
            col1, col2 = st.columns([1, 2])
            with col1:
                st.dataframe(df_bench, use_container_width=True)
                t_200 = bench_res.get(200, 0)
                st.success(f"✅ NFR-01 (200 SV): **{t_200}s** (< 5.0s)")
            with col2:
                st.line_chart(df_bench.set_index("Tổng số sinh viên (2N)"))