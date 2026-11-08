# 第七章/error.py
import streamlit as st

st.title("错误信息框")
# 不可以使用表情符号短代码
st.error('程序运行出错了', icon="🚨")
st.error('程序运行又出错了')

# 捕捉零作为除数的异常
try:
    div = 1/0
except ZeroDivisionError as e:
   st.error(e)

# 捕捉自定义抛出的异常
try:
    raise Exception("程序错了，这是一个自定义的异常")
except Exception as e:
   st.error(e)
