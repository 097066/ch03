# 第六章/tabs_matchine_learn.py
import streamlit as st

st.title("机器学习项目大致流程")
# 创建选项卡
tab1, tab2, tab3 = st.tabs(["数据处理", "模型训练", "模型评估"])
# 在第一个选项卡中添加内容
with tab1:
    st.header("数据处理")
    st.text("1. 收集数据")
    st.text("2. 数据预处理")
    st.text("3. 特征工程")
    st.code("""
# 示例代码
import pandas as pd
# 读取数据
df = pd.read_csv('data.csv')
# 数据预处理
df = clean_data(df)
# 特征工程
df = feature_engineering(df)
X, y = preprocess(df)
    """, language='python')

# 在第二个选项卡中添加内容
with tab2:
    st.header("模型训练")
    st.text("1. 选择模型")
    st.text("2. 训练模型")
    st.text("3. 优化模型")
    st.text("4. 保存模型")
    st.code("""from sklearn.ensemble import RandomForestClassifier
# 选择模型
model = RandomForestClassifier()
# 训练模型
model.fit(X_train, y_train)
# 优化模型
model = optimize_model(model)
# 保存模型
pickle.dump(model, open('rf_model.pkl', 'wb'))
    """, language='python')

# 在第三个选项卡中添加内容
with tab3:
    st.header("模型评估")
    st.text("1. 分割训练集和测试集")
    st.text("2. 模型评估指标")
    st.text("3. 错误分析")
    st.text("4. 模型可解释性")
    st.code("""
from sklearn.metrics import accuracy_score, precision_score, recall_score

# 分割训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y)
# 评估指标
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
# 错误分析
errors = y_test != y_pred
error_analysis(errors)
# 模型可解释性
feature_importances = model.feature_importances_
""", language='python')
