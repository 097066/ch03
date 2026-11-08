# 第七章/cache_data_example.py
import streamlit as st
import pandas as pd
import time

@st.cache_data
def get_big_data(path):
    """模拟获取大型数据集"""
    df = pd.read_csv(path)
    df.index.name = '索引号'
    # 模拟需要读取大数据，需要很久时间
    time.sleep(5)
    return df

st.title('缓存数据示例')
# 记录当前时间为开始时间
start = time.time()

# 第一次运行该获取数据函数时，会正常的运行，然后生成缓存数据
d1 = get_big_data('big_data1.csv')
st.write('读取完d1过了', time.time() - start, '秒')

# 由于传入的参数都是'big_data1.csv',此时将不会实际运行读取函数
# 而是直接通过哈希值查找，获取缓存的数据
# 虽然d1与d2是相同的，但是d1与d2是独立的，并不是指向同一个对象
d2 = get_big_data('big_data1.csv')
st.write('读取完d2过了', time.time() - start, '秒')

st.write('d1的内存地址',id(d1), '，d2的内存地址',id(d2))

# 由于'big_data2.csv'与'big_data1.csv'显然不同，它们产生的哈希值是不同的
# 没有对'big_data2.csv'的缓存数据，此时会正常的运行。
d3 = get_big_data('big_data2.csv')
st.write('读取完d3过了', time.time() - start, '秒')

if st.button('是否清除get_big_data()函数的缓存数据'):
    # 使用函数名.clear()进行清除
    get_big_data.clear()

