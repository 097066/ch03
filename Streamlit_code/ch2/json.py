# 第二章/json。py
import streamlit as st  # 导入Streamlit并用st代表它
import json  # 导入JSON模块

# 使用open()函数，读取json_data.json文件，
# 并指定编码为UTF-8（因为文件中包含中文）
with open("json_data.json", "r", encoding="utf-8") as f:
    my_obj = json.load(f)
st.subheader('来自JSON文件的数据')
st.json(my_obj)


my_string = '''[
	{"name":"王鑫","city":"临汾"},
	{"name":"Bob","city":"London"}
]'''
st.subheader('来自Python字符串')
st.json(my_string, expanded=False)