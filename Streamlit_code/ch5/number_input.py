# 第五章/number_input.py
import streamlit as st

st.subheader('示例1')
num_1 = st.number_input("请输入一个数字")
st.write('你输入的是：', num_1)

st.subheader('示例2')
age = st.number_input("请输入你的年龄", min_value=1, max_value=130, value=10)
st.write('你的年龄是:', age)

st.subheader('示例3')
price = st.number_input("请输入你的报价", min_value=1000.00, step=5.0)
st.write('你的报价是: ', price)
