# 第二章/text.py
import streamlit as st   # 导入Streamlit并用st代表它

# 第一个普通文本展示元素，无工具提示
st.text("這是一個普通文字展示元素。")
# 第二个普通文本展示元素，有工具提示
st.text('這也是一個普通文字展示元素，帶有工具提示',help='這是工具提示')
# 第三个普通文本展示元素，展示一些转义字符
st.text('''讀者們，\n你們好\t！歡迎學習Streamlit''')

