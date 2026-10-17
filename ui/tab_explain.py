import streamlit as st
import pandas as pd
from explain import explain_pair

def render():
    st.header("Tab 3: Giải thích lý do ghép phòng")

    if "match" not in st.session_state:
        st.warning("Vui lòng nạp dữ liệu (Tab 1) và thực hiện ghép phòng (Tab 2) trước khi xem giải thích.")
        return

    students = st.session_state["students"]
    M = st.session_state["M"]
    match = st.session_state["match"]

    st.markdown("Hệ thống phân tích mức độ tương thích trên **8 tiêu chí sinh hoạt** giữa các cặp bạn cùng phòng:")
    st.info("💡 **Tiêu chí trùng khớp (≥ 80%):** Thói quen sinh hoạt tương đồng cao, giảm nguy cơ xung đột.\n\n"
            "⚠️ **Tiêu chí cần lưu ý (≤ 40%):** Điểm khác biệt lớn giữa 2 bạn, cần thảo luận quy ước phòng sớm.")

    export_rows = []
    for i, (a, b) in enumerate(match.items()):
        sa, sb = students[a], students[b]
        score_ab = round(M[a][b], 1)
        score_ba = round(M[b][a], 1)
        avg_score = round((score_ab + score_ba) / 2.0, 1)
        reason = explain_pair(sa, sb)

        with st.expander(f"Phòng {i + 1}: {sa.name} (Nhóm A) - {sb.name} (Nhóm B) | Điểm TB: {avg_score}/100", expanded=True):
            col1, col2, col3 = st.columns(3)
            col1.metric("A đánh giá B", f"{score_ab}/100")
            col2.metric("B đánh giá A", f"{score_ba}/100")
            col3.metric("Điểm hài hòa chung", f"{avg_score}/100")
            st.write(f"**Phân tích chi tiết:** {reason}")

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