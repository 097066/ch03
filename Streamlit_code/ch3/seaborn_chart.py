# 第三章/seaborn_chart.py
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


# 使用NumPy模拟掷骰子1000次
data = np.random.randint(1, 7, size=1000)
# 利用模拟的数据，创建一个数据框，并指定列名
df = pd.DataFrame(data, columns=['点数'])
# 设置索引列的列名
df.index.name = '索引号'

st.subheader('展示部分模拟的数据')
# 使用write()函数展示数据框
st.write(df.head())
# 获取figure对象
fig = plt.gcf()
# 设置默认主题,并设置字体，以便显示中文
sns.set_theme(style='darkgrid', font='SimHei')

# 用Seaborn生成频数图
sns.countplot(data=df, x='点数', width=0.5)

st.subheader('展示Seaborn绘制的频数图')
# 使用Streamlit展示figure
st.pyplot(fig)
