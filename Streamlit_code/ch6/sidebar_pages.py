# 第六章/sidebar_pages.py
import streamlit as st

page = st.sidebar.selectbox("选择页面", ["页面1", "页面2", "页面3"])

if page == "页面1":
    st.title("页面1")
    st.write("这是页面1的内容")

elif page == "页面2":
    st.title("页面2")
    st.write("这是页面2的内容")

else:
    st.title("页面3")
    st.write("这是页面3的内容")
