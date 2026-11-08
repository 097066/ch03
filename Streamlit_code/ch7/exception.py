# 第七章/exception.py
import streamlit as st

st.header("错误信息框")
# 捕捉零作为除数的异常
try:
    div = 1/0
except ZeroDivisionError as e:
   st.error(e)

st.header("异常信息框")

# 捕捉零作为除数的异常
try:
    div = 1/0
except ZeroDivisionError as e:
   st.exception(e)
