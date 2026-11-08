# 第六章/columns_example.py
import streamlit as st

st.title("列容器")

# 创建三个列容器，宽度比为3:1:2
col1, col2, col3 = st.columns([3, 1, 2])

# 使用点号语法
col1.subheader("第一列")
col1.image('大熊猫图片.jpg')

# 使用with语法
with col2:
    st.subheader("第二列")
    st.image('大熊猫图片.jpg')

# 使用with语法
with col3:
    st.subheader("第三列")
    st.image('大熊猫图片.jpg')
