# 第五章/download_button.py
import streamlit as st
import pandas as pd
import numpy as np

# 将字符串作为文件，通过下载按钮进行下载
text_contents = '''这是Python的字符串'''
# 未设置file_name参数，将自动生成文件名
st.download_button('下载字符串', text_contents)
# 设置file_name参数，指定下载的文件名
st.download_button('下载字符串，指定文件名', text_contents, file_name='字符串.txt')

# 定义binary_contents为二进制数据
binary_contents = b'example content'
# 因为没有设置mime参数，默认为None
# 又因为binary_contents变量为二进制数据
# 所以mime会自动设置为'application/octet-stream'
st.download_button('下载二进制数据', binary_contents)

# 生成100行3列的随机数
df = pd.DataFrame(np.random.randn(100, 3), columns=['a', 'b', 'c'])
# 转换为csv格式
csv_data = df.to_csv(index=False)

# 将csv_data传给data参数，生成下载按钮
st.download_button(
    label="下载CSV文件",
    data=csv_data,
    file_name='data.csv',
    mime='text/csv', # 指定mime类型
)

# 读取图片的内容，然后将内容传给data参数，生成下载按钮
with open("鱼.jpg", "rb") as file:
    st.download_button(
            label="下载图片",
            data=file,
            file_name="小鱼图片.jpg",
            mime="image/jpeg"
    )









