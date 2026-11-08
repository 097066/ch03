# 第五章/camera_input.py
import streamlit as st

picture = st.camera_input("拍张照")
if picture:
    st.image(picture)

    bytes_data = picture.getvalue()
    st.write(type(bytes_data))
