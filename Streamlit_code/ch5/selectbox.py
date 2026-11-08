# 第五章/selectbox.py
import streamlit as st
# 自定义format_func函数
def my_format_func(option):
    return f'{option}市'

st.header('下拉按钮示例')
st.subheader('示例1')
city = st.selectbox('选择你的故乡：', ['北京', '太原', '临汾'],
                    format_func=my_format_func, index=2)
# 根据返回值不同，选择不同的特色回答
# 同时应注意返回值不受自定义my_format_func
if city == '北京':
    st.write('你的故乡是首都**北京**')
elif city == '太原':
    st.write('你的故乡是**太原**，它是山西的省会')
else:
    st.write('你的故乡是**临汾**，古时称“平阳”')

st.subheader('示例2')
size = st.selectbox(
    '选择尺码',
    ['S', 'M', 'L'],
    label_visibility='collapsed'
)
# 没有特色回答，可直接使用f-strings的回答
st.write(f'你选择的是{size}号')

st.subheader('示例3')
st.write('选择午饭')
# 设置标签为“hidden”
# 设置水平排列
lunch = st.selectbox(
    '你中午想吃什么菜？',
    ['糖醋里脊', '北京烤鸭', '宫保鸡丁'],
    label_visibility='hidden'
)
st.write(f'你选择的是吃{lunch}')
