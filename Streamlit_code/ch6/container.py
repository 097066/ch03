import streamlit as st

st.write("第一个外部文本")
container = st.container()

# 使用点语法添加元素
container.write("第一个内部文本")
# 使用with语法添加元素
with container:
    st.image('大熊猫图片.jpg',width=400)
    st.button("内部按钮")

st.write("第二个外部文本")
st.button("外部按钮")
