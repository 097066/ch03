# 第七章/session_state_callback.py
import streamlit as st
# 定义回调函数
def my_callback():
    st.write('回调函数中的打印')
    st.write(st.session_state['check'])
# 设置key参数为check，onchage参数为my_callback
check_res = st.checkbox('是否同意我们的用户协议', key="check", on_change=my_callback)

if check_res:
    st.write('你选择了，同意')
