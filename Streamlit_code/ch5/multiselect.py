# 第五章/multiselect.py
import streamlit as st

st.header('多选下拉按钮示例')
st.subheader('示例1')
# 自定义format_func函数
def my_format_func(option):
    return f'{option}市'

options_1 = st.multiselect(
    '选择你去过的城市',
    ['北京', '太原', '临汾', '南京', '杭州', '西安'],
    ['北京', '临汾'],
    format_func=my_format_func,
    )
st.write('你去过的城市是:', options_1)

st.subheader('示例2')
options_2 = st.multiselect(
    '选择你喜欢的颜色',
    ['红色', '绿色', '蓝色', '黑色', '粉色'],
    ['红色'],
    max_selections=2)
st.write('你喜欢的颜色是:', options_2)

st.subheader('示例3')
st.multiselect(
    '选择你喜欢的运动',
    ['游泳', '网球', '篮球'],
    ['游泳'],
    disabled=True)
