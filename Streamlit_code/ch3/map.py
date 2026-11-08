# 第三章/map.py
import streamlit as st
import pandas as pd
import numpy as np

# 生成北京市的随机点，其中39.9, 116.4是北京的经纬度
# 首先使用np.random.randn()方法生成1000行2列的符合正态分布的随机点
# 然后在第一列上除以20进行缩小，在第二列上除以50进行缩小
# 最后加上北京市的经纬度。
df = pd.DataFrame(
    np.random.randn(1000, 2) / [20, 50] + [39.9, 116.4],
    columns=['latitude', 'longitude'])
# 设置索引列的名称
df.index.name='序号'

st.subheader('展示部分需要绘制随机点的经纬度')
st.dataframe(df[1:5])

st.subheader('在北京地图上随机画点')
st.map(df)
