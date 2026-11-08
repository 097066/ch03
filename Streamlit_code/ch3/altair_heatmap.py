# 第三章/altair_heatmap.py
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

# 利用两个一维数组生成2D网格点
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
# z 为一个二维数组，其中z[i, j]的值为x[i, j]的平方加上y[i,j]的平方
z = x ** 2 + y ** 2

# 将此网格点的数据，转换为Altair所需的数据框类型
source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

# 给索引列加个名称
source.index.name = '索引号'
st.subheader('部分数据框展示')
st.write(source.head())
# 创建热力图对象
heatmap = alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q'
)
st.subheader('展示Altair热力图')
# 展示Altair热力图，并指定主题为原本Altaird的样式，而非"Streamlit"的主题
st.altair_chart(heatmap, theme=None)
