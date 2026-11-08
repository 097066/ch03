# 第七章/cache_data_persist.py
import streamlit as st
import pandas as pd
import time

@st.cache_data(persist='disk')
def get_big_data(path):
    """模拟获取大型数据集"""
    df = pd.read_csv(path)
    df.index.name = '索引号'
    # 模拟需要读取大数据，需要很久时间
    time.sleep(5)
    return df

st.title('缓存数据persist参数')
start = time.time()
d1 = get_big_data('big_data1.csv')

st.write("时间过了", time.time() - start, "秒")
st.write(d1)
