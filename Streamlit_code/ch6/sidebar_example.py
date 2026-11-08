# 第六章/sidebar_example.py
import streamlit as st

# 使用点号语法
add_selectbox = st.sidebar.selectbox(
    "你最喜欢什么颜色？",
    ("红色", "蓝色", "绿色")
)

# 使用with语法
with st.sidebar:
    add_radio = st.radio(
        "你最喜欢哪个学科",
        ("数学", "语文", "英语")
    )

st.title("侧边栏示例")
