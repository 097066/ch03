# 第五章/file_loader_single.py
import streamlit as st
import pandas as pd
from io import StringIO

# 通过file_uploader组件上传一个文件,获得文件对象uploaded_file
st.header('文件上传组件示例')
uploaded_file = st.file_uploader("选择一个CSV文件", type='csv')
if uploaded_file is not None:
    # uploaded_file本身是一个二进制对象,可以通过getvalue()获得其二进制值
    bytes_data = uploaded_file.getvalue()
    # 得到字节数据bytes_data，可以直接将二进制值显示出来,
    st.subheader('直接展示字节数据')
    st.write(bytes_data)

    # 若想将其转成字符串,可以通过StringIO来辅助转换。
    # 将上传文件的二进制内容转换为字符串形式
    # 创建一个StringIO对象来操作该字符串
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # 显示stringio对象
    st.subheader('展示生成StringIO对象')
    st.write(stringio)

    # 对stringio对象调用read()方法读取文件内容,获得一个字符串
    string_data = stringio.read()
    # 显示字符串
    st.subheader('展示读取的文件字符串')
    st.write(string_data)

    # pd.read_csv()可以接受一个“类似文件”对象作为参数,Uploaded_file就是一个类似文件的对象
    # 可以直接传递uploaded_file给pd.read_csv(),pandas会自动根据文件对象读入其内容,并解析成数据框
    dataframe = pd.read_csv(uploaded_file)
    dataframe.index.name = '索引号'
    st.subheader('展示直接用pd.read_cvs()方法生成的数据框')
    st.write(dataframe)
