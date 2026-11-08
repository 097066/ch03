# 第三章/plotly_chart.py
import streamlit as st
import numpy as np
import plotly.figure_factory as ff

# 创建直方图所用的数据
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2
x4 = np.random.randn(200) + 4

# 将数据组合到一个列表中
hist_data = [x1, x2, x3, x4]
# 每组的名称
group_labels = ['第一组', '第二组', '第三组', '第四组']
# 指定对应每个组的组距
bin_size = [.1, .25, .5, .75]

# 根据上方的数据，创建直方图
fig = ff.create_distplot(hist_data, group_labels, bin_size=bin_size)

st.subheader('展示Plotly直方图')
# 使用Streamlit绘制出直方图
st.plotly_chart(fig)
