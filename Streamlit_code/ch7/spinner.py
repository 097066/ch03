# 第七章/spinner.py
import time
import streamlit as st

st.title("旋转等待组件")
with st.spinner('请耐心等待:hourglass:'):
    time.sleep(5)
st.write("感谢你的耐心等待，任务已完成！")
