# 第四章/video.py
import streamlit as st
# 读取视频数据
video_file = open('小红花视频.mp4', 'rb')
video_bytes = video_file.read()

# 显示视频
st.subheader("展示视频")
st.video(video_bytes)
