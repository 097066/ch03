# 第六章/tabs_exanple.py
import streamlit as st

st.title("选项卡简单示例")
tab1, tab2, tab3 = st.tabs(["选项卡1", "选项卡2", "选项卡3"])

with tab1:
    st.header("这是第一个选项卡")
    st.markdown("#### 第一个选项卡的内容")

with tab2:
    st.header("这是第二个选项卡")
    st.markdown("#### 第二个选项卡的内容")

with tab3:
    st.header("这是第三个选项卡")
    st.markdown("#### 第三个选项卡的内容")
