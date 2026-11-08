# 第七章/warning.py
import streamlit as st

st.title("警告信息框")
# 不可以使用表情符号短代码
st.warning('程序出现问题，可能导致程序错误，请注意', icon="⚠️")
st.warning('程序又出现问题，可能导致程序错误，请注意')
