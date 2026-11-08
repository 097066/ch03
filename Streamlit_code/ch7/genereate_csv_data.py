# 第七章/generate_csv_data.py
import numpy as np
import pandas as pd
import streamlit as st

st.title('生成模拟数据')

# 生成1000行3列的随机数组
data = np.random.randint(0, 100, size=(1000, 3))

# 将数组转换为DataFrame
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

# 将DataFrame保存为CSV文件
# df.to_csv('big_data1.csv', index=False)
df.to_csv('big_data2.csv', index=False)

st.write('模拟数据已生成，可以按快捷键Ctrl + C，停止应用。')
