# 第六章/empty.py
import streamlit as st
import time

placeholder = st.empty()

# 替换为文本元素
placeholder.text("现在是文本元素")
time.sleep(2)

# 替换为折线图元素
placeholder.line_chart({"data": [1, 5, 2, 6]})
time.sleep(2)
# 替换为含有文本元素的不可见容器
with placeholder.container():
    st.write("这是不可见容器内的文本元素")
    code = '''
    # 这是不可见容器内的代码块
    import numpy as np

    a = np.array([1, 2, 3])
    b = np.array([[1, 2, 3], [4, 5, 6]])
    '''
    st.code(code, language='python')
time.sleep(2)
with placeholder:
    for seconds in range(5,0,-1):
        st.write(f"还有{seconds}秒⏳，将清空元素")
        time.sleep(1)

# 清空所有元素
placeholder.empty()
st.write("结束了")
