# 第六章/expander_numpy.py
import streamlit as st

st.title("介绍NumPy库的基本使用")
with st.expander("创建数组", expanded=True):
    code = '''
  import numpy as np

  a = np.array([1, 2, 3])
  b = np.array([[1, 2, 3], [4, 5, 6]])
  '''
    st.code(code, language='python')

with st.expander("数组操作"):
    code = '''
  import numpy as np

  a = np.array([1,2,3])
  b = np.array([4,5,6])

  print(a + b) # 数组相加
  print(a - b) # 数组相减
  print(a * b) # 数组相乘
  '''
    st.code(code, language='python')

with st.expander("数学函数"):
    code = '''
  import numpy as np

  a = np.array([1, 2, 3])

  print(np.sin(a)) # 正弦函数
  print(np.log(a)) # 对数函数
  print(np.sum(a)) # 求和
  '''

    st.code(code, language='python')
