# 第四章/emoji.py
import streamlit as st

st.title("标题元素支持表情符号 :tada:")
st.header("章节元素支持表情表情 :apple:")
st.subheader("子章节元素支持表情符号，使用ASCII值插入\U0001F600")
st.code("代码块支持表情符号，使用ASCII值插入\U0001F602")
st.text("普通文本支持表情符号，使用ASCII值插入\U0001F601")
st.markdown("Markdown支持表情符号 :smile:")

