# 第五章/date_input.py
import streamlit as st
from datetime import datetime, timedelta

st.subheader("示例1")
# value参数默认为None，初始状态为今天
date = st.date_input("选择一个日期", value=None)
st.write("你选择的日期是:", date)

st.subheader("示例2")
# 设置value为元组，代表(start, end)，日期选择器为区间[start, end]
date_1, date_2 = st.date_input("选择一个日期区间", value=(datetime.now(), datetime.now() + timedelta(7)))
st.write("你选择的日期区间是:", date_1, "到", date_2)


st.subheader("示例3")
# 设置value为昨天
# 设置min_value为今天减去7天，max_value为今天
date = st.date_input(
    "限制日期选择区间",
    value=datetime.now() - timedelta(1),
    min_value=datetime.now() - timedelta(7),
    max_value=datetime.now())

st.write("你选择的日期是:", date)
