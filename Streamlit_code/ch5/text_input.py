# 第五章/text_input.py
import streamlit as st

st.subheader('示例1')
song = st.text_input('歌曲名称：', '歌唱祖国')
st.write('你输入的歌曲名称是：', song)

st.subheader('示例2')
name = st.text_input('姓名', autocomplete='name')
st.write('你的姓名是：', name)

st.subheader('示例3')
st.text_input('占位字符串展示', placeholder='这是一个占位字符串')

st.subheader('示例4')
st.text_input('密码', value='123456', type='password')
