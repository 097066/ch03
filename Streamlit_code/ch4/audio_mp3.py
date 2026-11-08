# 第四章/audio_mp3.py
import streamlit as st


# 读取本地的音频
audio_file = open('背景音乐.mp3', 'rb')
audio_bytes = audio_file.read()

st.subheader('播放本地音频')
st.audio(audio_bytes)

