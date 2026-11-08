# 第三章/bokeh_chart.py
import streamlit as st
import numpy as np
from bokeh.plotting import figure

# 生成x轴数据，使用np.linspace()函数生成-6到6之间500个均匀分布的数值
x = np.linspace(-6, 6, 500)
# 计算对应的y轴坐标，为一个波形
y = 8*np.sin(x)*np.sinc(x)
# 定义一个Bokeh的figure对象，宽高分别设为800和300像素
# 设置横纵比相符，防止变形
p = figure(width=800, height=300, match_aspect=True)
# 绘制线条
p.line(x, y, color="navy", alpha=0.7, line_width=4)
# 设置背景颜色
p.background_fill_color = "#efefef"
# 设置坐标轴
p.xaxis.fixed_location = 0
p.yaxis.fixed_location = 0

st.subheader('展示Bokeh图表')
# 使用Streamlit展示Bokeh图表
st.bokeh_chart(p, use_container_width=True)
