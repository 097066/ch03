# 第七章/stop.py
import streamlit as st

st.title("停止执行示例")
# 将单行文本的值赋值给name变量
name = st.text_input('你的姓名：')
# 判断name变量是否为空
if not name:
    # 如果用户未输入姓名，name变量为空字符串，not name的值将为True
    # 警告用户需要输入姓名
    st.warning('请输入姓名！')
    # 停止执行
    st.stop()
# name不是空字符串，用成功信息框提示用户
st.success('非常感谢！你按要求输入了姓名')
