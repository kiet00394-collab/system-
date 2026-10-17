import streamlit as st
import pandas as pd
from explain import explain_pair

def render():
    st.header("Tab 3: Giải thích lý do ghép phòng")

    if "match" not in st.session_state:
        st.warning("⚠️ Vui lòng nạp dữ liệu (Tab 1) và thực hiện ghép phòng (Tab 2) trước khi xem giải thích.")
        return

    students = st.session_state["students"]
    M = st.session_state["M"]
    match = st.session_state["match"]

    st.markdown("Hệ thống phân tích mức độ tương thích trên **8 tiêu chí sinh hoạt** và **tiêu chí ưu tiên (`top`)** của các cặp bạn cùng phòng:")
    st.info("💡 **Tiêu chí trùng khớp (≥ 80%):** Thói quen tương đồng cao, giảm nguy cơ xung đột.\n\n"
            "⚠️ **Tiêu chí cần lưu ý (≤ 40%):** Khác biệt rõ rệt, cần xây dựng quy ước phòng sớm.\n\n"
            "🎯 **Tiêu chí ưu tiên (`top`):** Mức độ đáp ứng nguyện vọng quan trọng nhất của từng sinh viên.")

    # Cảnh báo sinh viên chưa được ghép (do lệch sĩ số nhóm A và B)
    matched_a = set(match.keys())
    matched_b = set(match.values())
    unmatched_students = [s for s in students if (s.group == "A" and s.id not in matched_a) or (s.group == "B" and s.id not in matched_b)]

    if unmatched_students:
        st.warning(f"⚠️ **Có {len(unmatched_students)} sinh viên chưa được ghép phòng** do chênh lệch sĩ số giữa nhóm A và nhóm B:")
        unmatched_rows = [{"ID": s.id, "Tên": s.name, "Nhóm": s.group, "Trạng thái": "Chưa có phòng (chờ đợt ghép bổ sung)"} for s in unmatched_students]
        st.dataframe(pd.DataFrame(unmatched_rows), use_container_width=True)

    # Ô tìm kiếm phòng theo tên sinh viên hoặc số phòng
    col_search, _ = st.columns([2, 1])
    with col_search:
        search_query = st.text_input("🔍 Tìm kiếm theo tên sinh viên hoặc số phòng:", placeholder="Nhập tên (ví dụ: SV001) hoặc số phòng...").strip().lower()

    export_rows = []
    display_count = 0

    for i, (a, b) in enumerate(match.items()):
        sa, sb = students[a], students[b]
        score_ab = round(M[a][b], 1)
        score_ba = round(M[b][a], 1)
        avg_score = round((score_ab + score_ba) / 2.0, 1)
        reason = explain_pair(sa, sb)

        export_rows.append({
            "Phòng": i + 1,
            "ID_A": sa.id,
            "Tên_A": sa.name,
            "ID_B": sb.id,
            "Tên_B": sb.name,
            "Điểm_A_danh_gia_B": score_ab,
            "Điểm_B_danh_gia_A": score_ba,
            "Điểm_TB": avg_score,
            "Lý_do_ghep": reason
        })

        # Lọc hiển thị theo từ khóa tìm kiếm
        room_title = f"phòng {i + 1}"
        if search_query:
            if (search_query not in sa.name.lower() and 
                search_query not in sb.name.lower() and 
                search_query not in room_title and 
                search_query != str(i + 1)):
                continue

        display_count += 1
        # Mở rộng mặc định phòng đầu tiên nếu không tìm kiếm, nếu có tìm kiếm thì mở tất cả kết quả khớp
        is_expanded = True if search_query else (display_count == 1)

        with st.expander(f"🏠 Phòng {i + 1}: {sa.name} (Nhóm A) & {sb.name} (Nhóm B) — Điểm TB: {avg_score}/100", expanded=is_expanded):
            col1, col2, col3 = st.columns(3)
            col1.metric(f"{sa.name} đánh giá {sb.name}", f"{score_ab}/100")
            col2.metric(f"{sb.name} đánh giá {sa.name}", f"{score_ba}/100")
            col3.metric("Độ hài hòa trung bình", f"{avg_score}/100")
            st.write(f"**Diễn giải tương thích:** {reason}")

    if search_query and display_count == 0:
        st.info(f"Không tìm thấy phòng nào phù hợp với từ khóa '{search_query}'.")

    # Nút xuất kết quả CSV (FR-11)
    st.divider()
    df_export = pd.DataFrame(export_rows)
    csv_bytes = df_export.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")
    st.download_button(
        label="📥 Tải về kết quả ghép phòng và giải thích (CSV)",
        data=csv_bytes,
        file_name="ket_qua_ghep_phong_ktx.csv",
        mime="text/csv"
    )