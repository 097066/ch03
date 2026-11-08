# 第六章/multiple_page_prj/pages/2_pandas_intro.py
import streamlit as st

st.title("这里是子页面")
st.write("这个页面来自😊2_pandas_intro.py文件，你可点击左侧👈的页面，导航到相应的页面")

code = '''
import pandas as pd

df = pd.DataFrame({
  'Name': ['John', 'Mary', 'Peter','Jeff'],
  'Age': [28, 32, 25, 19]
})

print(df)
print(df['Name'])
'''
st.code(code, language='python')
