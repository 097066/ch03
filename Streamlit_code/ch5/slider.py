# 第五章/slider.py
import streamlit as st
from datetime import datetime, time

st.subheader("示例1")
age = st.slider('你今年多大', 0, 130, 25)
st.write("我今年 ", age, '岁了')

st.subheader("示例2")
values = st.slider(
    '选择一组范围',
    0.0, 100.0, (25.0, 75.0))
st.write('你选择的范围是：', values)

st.subheader("示例3")
appointment = st.slider(
    "选择会议的时间:",
    value=(time(10, 30), time(12, 45)))
st.write("会议的时间：", appointment)

st.subheader("示例4")
start_time = st.slider(
    "你什么时候开始上大学的",
    value=datetime(2021, 1, 1),
    format="YYYY年MM月DD日"
    )
st.write("开始时间日期：", start_time.strftime("%Y年%m月%d日"))
