# 第五章/select_slider.py
import streamlit as st


st.subheader("示例1")
# 水果名与表情符号对照的字典
fruit_dict = {
    '苹果': ':apple:',
    '香蕉': ':banana:',
    '柠檬': ':lemon:',
    '菠萝': ":pineapple:"
}
# 选项为上边字典的键
options = fruit_dict.keys()

fruit = st.select_slider('选择一个水果', options=options)
st.write('你选择的水果是', fruit, fruit_dict[fruit])

st.subheader("示例2")
my_range = range(1, 21)

numbers = st.select_slider('选择你的心动值', options=my_range, value=5)
st.write('你选择了 %s 个心动' % numbers, numbers * ":hearts:")

st.subheader("示例3")
start_color, end_color = st.select_slider(
    '选择波长的颜色范围',
    options=['红色', '橙色', '黄色', '绿色', '蓝色', '靛色', '紫色'],
    value=('橙色', '蓝色'))
st.write('你选择的波长介于', start_color, '和', end_color, '之间')
