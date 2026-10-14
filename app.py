import streamlit as st
from ui import tab_data, tab_match, tab_explain, tab_compare

st.set_page_config(page_title="Hệ thống ghép phòng KTX", layout="wide")
st.title("Hệ thống ghép phòng ký túc xá")

t1, t2, t3, t4 = st.tabs(["1. Dữ liệu", "2. Ghép phòng", "3. Giải thích", "4. So sánh"])

with t1:
    tab_data.render()
with t2:
    tab_match.render()
with t3:
    tab_explain.render()
with t4:
    tab_compare.render()