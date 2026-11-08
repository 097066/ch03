# 第五章/color_picker.py
import streamlit as st

st.subheader("示例1")
color = st.color_picker('选择一个颜色')
st.write('当前的颜色值是', color)

st.subheader("示例2")
color = st.color_picker('选择一个颜色', '#0000ff')
st.write('当前的颜色值是', color)
