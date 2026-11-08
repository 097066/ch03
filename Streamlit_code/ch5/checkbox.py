# 第五章/checkbox.py
import streamlit as st

st.header("勾选按钮示例")
st.subheader("示例1")
agree = st.checkbox('是否同意我们的用户协议')

if agree:
    st.write('是的，我同意')

st.subheader("示例2")
result = st.checkbox('请勾选我')

if result:
    st.write('非常好！你勾选了')
else:
    st.write('快勾选上方的按钮')

st.subheader("示例3")
st.write('选择你的爱好')
check_1 = st.checkbox('游泳', value=True)
check_2 = st.checkbox('唱歌')
check_3 = st.checkbox('看电影')

