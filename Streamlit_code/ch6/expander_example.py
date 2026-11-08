# 第六章/expander_example.py
import streamlit as st

st.subheader("示例1")
st.bar_chart([1, 5, 2, 6, 2, 1])
with st.expander("图表说明"):
    st.write("上面的图表是由st.bar_chart()方法生成的。使用该方法可以生成条形图")

st.subheader("示例2")
with st.expander("展开状态", expanded=True):
    st.write("默认为展开状态")
