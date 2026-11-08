# 第五章/radio.py
import streamlit as st
# 自定义format_func函数
def my_format_func(option):
    return f'选{option}'

st.header('单选按钮示例')
st.subheader('示例1')
city = st.radio('选择你最喜爱的城市：', ['北京', '太原', '临汾'], format_func=my_format_func,)
# 根据返回值不同，选择不同的特色回答
# 同时应注意返回值不受自定义my_format_func
if city == '北京':
    st.write('你最喜爱的城市是首都**北京**')
elif city == '太原':
    st.write('你最喜爱的城市是**太原**，它是山西的省会')
else:
    st.write('你最喜爱的城市是**临汾**，古时称“平阳”')

st.subheader('示例2')
size = st.radio(
    '选择尺码',
    ['S', 'M', 'L'],
    label_visibility='collapsed',
)
# 没有特色回答，可直接使用f-strings的回答
st.write(f'你选择的是{size}号')

st.subheader('示例3')
st.write('选择午饭')
# 设置标签为“hidden”
# 设置水平排列
lunch = st.radio(
    '你中午想吃什么？',
    ['馒头', '大米', '面条'],
    horizontal=True,
    label_visibility='hidden'
)
st.write(f'你选择的是吃{lunch}')
