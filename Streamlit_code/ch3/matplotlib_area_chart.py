# 第三章/matplotlib_line_chart.py
import streamlit as st
import matplotlib.pyplot as plt

# 设置Matplotlib使用能显示中文的字体，如SimHei字体
plt.rcParams['font.family'] = ['SimHei']
# 构建3个门店每个月的销售数据
store1 = [50, 70, 80, 90, 70]
store2 = [35, 60, 90, 95, 80]
store3 = [25, 40, 70, 50, 60]

months = ['1月', '2月', '3月', '4月', '5月']
# 绘制图表
fig, ax = plt.subplots()
# 画1号门店的面积
ax.fill_between(months, store1, 0, facecolor='r',alpha=0.3, label='1号门店')
# 画2号门店的面积
ax.fill_between(months, store2, 0,facecolor='b',alpha=0.3, label='2号门店')
# 画3号门店的面积
ax.fill_between(months, store3, 0, facecolor='g',alpha=0.3,label='3号门店')

# 设置标题和坐标轴标签
ax.set_ylabel('销售额')
ax.set_title('各门店销售额面积图')

# 绘制图例在左上角
ax.legend(loc='upper left')

st.subheader('展示Matplotlib面积图')
# 显示matplotlib图表，并设置分辨率
st.pyplot(fig, dpi=300)
