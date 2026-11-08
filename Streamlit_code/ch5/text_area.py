# 第五章/text_area.py
import streamlit as st

st.subheader("示例1")
st.text_area(label='建议或意见：', placeholder='请输入您的建议或意见')


st.subheader("示例2")
init_text = "真的猛士，敢于直面惨淡的人生，敢于正视淋漓的鲜血。这是怎样的哀痛者和" \
            "幸福者？然而造化又常常为庸人设计，以时间的流驶，来洗涤旧迹，仅使留下" \
            "淡红的血色和微漠的悲哀。在这淡红的血色和微漠的悲哀中，又给人暂得偷生" \
            "，维持着这似人非人的世界。我不知道这样的世界何时是一个尽头"
st.text_area(label='输入需要进行情感分析的文本：', value=init_text,
            height=200, max_chars=200)

