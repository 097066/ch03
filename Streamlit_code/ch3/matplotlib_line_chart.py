# 第三章/matplotlib_line_chart.py
import streamlit as st
import matplotlib.pyplot as plt

# 设置Matplotlib使用能显示中文的字体，如SimHei字体
plt.rcParams['font.family'] = ['SimHei']
# 构建3个门店每个月的销售数据
store1 = [100, 120, 150, 140, 150]
store2 = [95, 135, 130, 150, 135]
store3 = [105, 125, 153, 172, 160]

months = ['1月', '2月', '3月', '4月', '5月']
# 绘制图表
fig, ax = plt.subplots()
# 画1号门店的线，数据点的形状为圆点
ax.plot(months, store1, marker='o', label='1号门店')
# 画2号门店的线，数据点的形状为方块
ax.plot(months, store2, marker='s',label='2号门店')
# 画3号门店的线，数据点的形状为三角形
ax.plot(months, store3, marker='^',label='3号门店')

# 设置标题和坐标轴标签
ax.set_ylabel('销售额')
ax.set_title('各门店销售额折线图')

# 设置x轴标签倾斜
plt.xticks(rotation=45)
# 绘制图例
ax.legend()

st.subheader('展示Matplotlib折线图')
# 显示matplotlib图表，并设置分辨率
st.pyplot(fig, dpi=300)
