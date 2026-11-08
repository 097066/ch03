# 第七章/echo.py
import streamlit as st

st.title("回显代码示例")
with st.echo(code_location='below'):
    # 在with语法缩进里的代码会回显出来
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

# 这里的代码会执行，但不会回显
st.write('代码会执行，但不会回显')
