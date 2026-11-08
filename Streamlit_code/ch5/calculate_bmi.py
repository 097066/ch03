# 第五章/calculate_bmi.py
import streamlit as st

st.header('身体质量指数计算器')

weight = st.number_input('请输入您的体重（千克)', min_value=0.0)
height = st.number_input('请输入您的身高（米）', min_value=0.0, format='%.2f')

if st.button('计算BMI'):
    bmi = weight / (height ** 2)
    st.write(f'您的BMI指数为:{bmi:.2f}')
