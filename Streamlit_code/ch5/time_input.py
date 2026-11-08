# 第五章/time_input.py
import streamlit as st
from datetime import datetime, time

st.subheader("示例1")
w1 = st.time_input("时间1")
st.write("你选择时间1是:", w1)

st.subheader("示例2")
w2 = st.time_input("时间2", time(8, 45))
st.write("你选择时间2是:", w2)

st.subheader("示例3")
w3 = st.time_input("时间3", datetime(2019, 7, 6, 21, 15))
st.write("你选择时间3是:", w3)

st.subheader("示例4")
# 设置step为60秒，即1分钟
w3 = st.time_input("时间4", step=60)
st.write("你选择时间4是:", w3)
