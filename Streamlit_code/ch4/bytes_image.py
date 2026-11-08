import streamlit as st

with open("大熊猫图片.jpg", "rb") as f:
    image_bytes = f.read()
st.text("使用open()函数读取为BytesIO，然后使用st.image()方法进行展示")
st.image(image_bytes)

