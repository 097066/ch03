# 第三章/altair_line_chart.py
import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

# 生成0到100(不包括100)之间均匀间隔的数字数组，默认间隔为1
x = np.arange(100)
# 生成x和f(x)的数据，并转换为Altair所需的数据框类型
source = pd.DataFrame({
  'x': x,
  'f(x)': np.sin(x / 5)
})
# 给索引列加个名称
source.index.name = '索引号'
st.subheader('部分数据框展示')
st.write(source.head())

# 创建折线图对象
line_chart = alt.Chart(source).mark_line().encode(
    x='x',
    y='f(x)'
)
st.subheader('展示Altair折线图')
# 展示Altair热力图，并指定主题为原本Altaird的样式，而非"Streamlit"的主题
st.altair_chart(line_chart,use_container_width=True, theme=None)
