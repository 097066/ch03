# 第七章/info.py
import streamlit as st

st.title("提示信息框")
# 不可以使用表情符号短代码
st.info('这是一个带有图标提示信息框', icon="🤖")
st.info('这也是一个提示信息框')
