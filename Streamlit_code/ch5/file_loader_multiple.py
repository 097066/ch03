# 第五章/file_loader_multiple.py
import streamlit as st

st.subheader("多文件上传")
uploaded_files = st.file_uploader("选择要上传的文件", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    st.write("文件名:", uploaded_file.name, "文件大小：", uploaded_file.size, "B")
