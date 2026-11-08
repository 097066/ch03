# 第三章/graph.py
import streamlit as st
import graphviz

# 创建一个有向图对象
graph = graphviz.Digraph()
# 添加节点
graph.node("训练数据")
graph.node("机器学习的算法")
graph.node("模型")
graph.node("结果预测")
graph.node("新的数据")
# 添加箭头
graph.edge("训练数据", "机器学习的算法")
graph.edge("机器学习的算法", "模型")
graph.edge("模型", "结果预测")
graph.edge("新的数据", "模型")

st.subheader("通过Graphviz对象展示流程图")
st.graphviz_chart(graph)

st.subheader("通过DOT语法展示流程图")
st.graphviz_chart('''
    digraph {
        "训练数据" -> "机器学习的算法"
        "机器学习的算法" -> "模型"
        "模型" -> "结果预测"
        "新的数据" -> "模型"
    }
''')
