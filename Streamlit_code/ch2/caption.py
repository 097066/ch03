# 第二章/caption.py
import streamlit as st

st.header('这是一个章节展示元素')
st.subheader('这是一个子章节展示元素')
st.text('这是普通文本展示元素')

python_code = '''def hello():
    print("你好，Streamlit！")
'''
# 默认说明文字样式
st.caption('代码块1：Python代码')
# 斜体说明文字样式
st.caption('<i>代码块1：Python代码</i>', unsafe_allow_html=True)
# 居中对齐的说明文字样式
st.caption('<center>代码块1：Python代码</center>',unsafe_allow_html=True)
st.code(python_code)

