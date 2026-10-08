import streamlit as st
import pandas as pd
from models import Student
from data_io import load_students_csv, generate_students, students_to_dataframe, HOBBIES
from scoring import compute_score_matrix, build_pref_lists

def render():
    st.subheader("1. Quản lý & Nạp dữ liệu sinh viên")

    mode = st.radio("Nguồn dữ liệu", ["Sinh dữ liệu giả lập", "Tải file CSV"], horizontal=True)
    students = None

    if mode == "Sinh dữ liệu giả lập":
        col1, col2 = st.columns(2)
        with col1:
            n = st.slider("Số sinh viên (phải chia đều nhóm A và B)", 10, 200, 40, step=2)
        with col2:
            seed = st.number_input("Seed ngẫu nhiên", value=42, step=1)

        if st.button("Sinh dữ liệu giả lập", type="primary"):
            students = generate_students(n, int(seed))
            st.success(f"Đã sinh {len(students)} sinh viên giả lập thành công!")
    else:
        f = st.file_uploader("Chọn file CSV dữ liệu sinh viên", type="csv")
        if f is not None:
            try:
                students = load_students_csv(f)
                st.success(f"Đã nạp {len(students)} sinh viên từ file CSV!")
            except Exception as e:
                # NFR-04: Xử lý ngoại lệ file sai không làm sập ứng dụng
                st.error(f"File không hợp lệ: {e}")

    if students:
        st.session_state["students"] = students
        M = compute_score_matrix(students)
        st.session_state["M"] = M
        st.session_state["pref_a"], st.session_state["pref_b"] = build_pref_lists(M, students)
        st.session_state.pop("match", None)

    # Hiển thị dữ liệu hiện tại trong session_state
    if "students" in st.session_state:
        current_students = st.session_state["students"]
        st.markdown("### Danh sách sinh viên hiện tại")
        df = students_to_dataframe(current_students)
        st.dataframe(df, use_container_width=True)
        st.info(f"Đã nạp **{len(current_students)}** sinh viên và tính sẵn ma trận điểm tương thích.")

        # FR-01: Form thêm thủ công 1 sinh viên
        with st.expander("➕ Thêm thủ công 1 sinh viên mới (FR-01)"):
            with st.form("add_student_form", clear_on_submit=True):
                c1, c2, c3 = st.columns(3)
                with c1:
                    new_name = st.text_input("Tên sinh viên", value=f"SV{len(current_students):03d}")
                    new_group = st.selectbox("Nhóm", ["A", "B"])
                    new_sleep = st.number_input("Giờ đi ngủ (21h - 26h)", 21.0, 26.0, 23.0, 0.5)
                with c2:
                    new_wake = st.number_input("Giờ thức dậy (5h - 10h)", 5.0, 10.0, 7.0, 0.5)
                    new_tidy = st.slider("Mức gọn gàng (1-5)", 1, 5, 3)
                    new_study = st.selectbox("Thói quen học", ["phong", "thuvien", "it"])
                with c3:
                    new_noise = st.slider("Mức chịu ồn (1-5)", 1, 5, 3)
                    new_smoke = st.selectbox("Hút thuốc", [0, 1], format_func=lambda x: "Có" if x == 1 else "Không")
                    new_guests = st.slider("Hay có khách (1-5)", 1, 5, 2)

                new_hobbies = st.multiselect("Sở thích", HOBBIES, default=["game", "nhac"])
                new_top = st.selectbox("Tiêu chí quan trọng nhất", ["sleep", "tidy", "noise", "study", "smoke"])

                submitted = st.form_submit_button("Thêm sinh viên")
                if submitted:
                    new_id = len(current_students)
                    new_student = Student(
                        id=new_id,
                        name=new_name,
                        group=new_group,
                        sleep=new_sleep,
                        wake=new_wake,
                        tidy=new_tidy,
                        study=new_study,
                        noise=new_noise,
                        smoke=new_smoke,
                        guests=new_guests,
                        hobbies=set(new_hobbies),
                        top=new_top
                    )
                    current_students.append(new_student)
                    st.session_state["students"] = current_students
                    M = compute_score_matrix(current_students)
                    st.session_state["M"] = M
                    st.session_state["pref_a"], st.session_state["pref_b"] = build_pref_lists(M, current_students)
                    st.session_state.pop("match", None)
                    st.success(f"Đã thêm sinh viên {new_name} (ID: {new_id}) thành công!")
                    st.rerun()
