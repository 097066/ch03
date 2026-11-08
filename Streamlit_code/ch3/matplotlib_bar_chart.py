# 第三章/matplotlib_bar_chart.py
import streamlit as st
import matplotlib.pyplot as plt

# 设置Matplotlib使用能显示中文的字体，如SimHei字体
plt.rcParams['font.family'] = ['SimHei']

fig, ax = plt.subplots()
# 设置x轴标签
fruits = ['苹果', '蓝莓', '樱桃', '橙子']
# 设置y轴的数量
counts = [40, 100, 30, 55]
# 设置右上方水果颜色对应图例
bar_labels = ['红色', '蓝色', '_红色', '橙色']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
# 生成条形图
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
# 设置y轴标签
ax.set_ylabel('水果供应量')
# 设置图表标题
ax.set_title('水果供应按品种和颜色分类')
# 设置图例标题
ax.legend(title='水果颜色对应')


st.subheader('展示Matplotlib条形图')
# 显示matplotlib图表，并设置分辨率
st.pyplot(fig, dpi=300)
