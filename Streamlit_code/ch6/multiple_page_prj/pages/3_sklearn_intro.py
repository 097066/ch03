# 第六章/multiple_page_prj/pages/3_sklearn_intro.py
import streamlit as st

st.title("这里是子页面")
st.write("这个页面来自😊3_sklearn_intro.py文件，你可点击左侧👈的页面，导航到相应的页面")

code = '''
from sklearn.linear_model import LinearRegression

# 生成数据
X = [[1], [2], [3]]
y = [1, 2, 3]

# 模型训练
model = LinearRegression()
model.fit(X, y)

# 预测
print(model.predict([[4]]))
'''

st.code(code, language='python')
