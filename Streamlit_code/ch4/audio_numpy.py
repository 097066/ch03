# 第四章/audio_numpy.py
import streamlit as st
import numpy as np

# 参数设置
sample_rate = 44100
seconds = 3

# 440Hz - A4音符
f = 440
t= np.linspace(0, seconds, int(seconds*sample_rate), False)
tone = np.sin(f * t * 2 * np.pi)

st.subheader('播放生成的音频')
# 播放音频
st.audio(tone, sample_rate=sample_rate)
