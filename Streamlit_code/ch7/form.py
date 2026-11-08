# 第七章/form.py
import streamlit as st

st.title("提交表单示例")
with st.form("my_form"):
   st.write("这是在表单内")
   slider_val = st.slider("表单内的数值滑块组件")
   checkbox_val = st.checkbox("表单内的勾选按钮")

   # 注意：每个表单内都需要有一个表单提交按钮
   submitted = st.form_submit_button("提交")
   if submitted:
       st.write("数值滑块组件的值", slider_val, "勾选按钮的值", checkbox_val)

st.write("这个不在表单内")
