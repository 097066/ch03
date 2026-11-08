# 第七章/success.py
import streamlit as st

st.title("成功信息框")
# 不可以使用表情符号短代码
st.success('这是一个带有图标的成功信息框', icon="✅")
st.success('这也是一个成功信息框')
