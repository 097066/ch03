# 第六章/columns_grids.py
import streamlit as st
from PIL import Image
img = Image.open("大熊猫图片.jpg")
st.subheader("使用列容器构成栅格布局")
# 将产生4行
for _ in range(4):
    # 每一行创建宽度为1:1:1:1的列容器
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)
