# 第五章/button.py
import streamlit as st

st.subheader("简单的普通按钮示例")
if st.button('点击这里'):
    st.write('按钮被点击了！')

st.button('另一个按钮')
