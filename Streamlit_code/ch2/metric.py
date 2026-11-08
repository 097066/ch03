import streamlit as st  # 导入Streamlit并用st代表它


st.subheader('收入情况')
st.metric(label="当日收入", value="1500", delta="100")

st.subheader('天气情况')
# 定义列布局，分成3列
c1, c2, c3 = st.columns(3)
c1.metric(label="温度", value="32℃", delta="-1.5℃")
c2.metric(label="湿度", value="76%", delta="6%")
c3.metric(label="风速", value=None, delta="0", delta_color="off")

st.subheader('员工情况')
st.metric(label="员工人数", value="320", delta="10", label_visibility='hidden')