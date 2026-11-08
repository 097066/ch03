# 第六章/multiple_page_prj/pages/1_numpy_intro.py
import streamlit as st

st.title("这里是子页面")

st.write("这个页面来自😊1_numpy_intro.py文件，你可点击左侧👈的页面，导航到相应的页面")
code = '''
import numpy as np

arr = np.random.randn(5, 5)

print(arr)
print(arr.shape)
print(np.mean(arr))
'''
st.code(code, language='python')
