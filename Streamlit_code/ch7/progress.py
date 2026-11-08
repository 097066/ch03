# 第七章/progress.py
import streamlit as st
import time

st.header("进度条示例")
# 设置初始状态
progress_text_1 = "程序正在处理中，请稍等"
my_bar = st.progress(0, text=progress_text_1)
time.sleep(0.5)

# 第一个过程，时间间隔为0.1秒，进度较慢
for percent in range(80):
    time.sleep(0.1)
    my_bar.progress(percent + 1, text=f'{progress_text_1}，当前进度{percent}%:hourglass:')

# 第二个过程，时间间隔为0.05秒，进度较快
for percent in range(80,100):
    time.sleep(0.05)
    my_bar.progress(percent + 1, text=f'程序马上就要完成了，当前进度{percent}%:laughing:')
