# 第二章/code.py
import streamlit as st   # 导入Streamlit并用st代表它

st.subheader('Python代码块')
# 创建要显示的Python代码块的内容
python_code = '''def hello():
    print("你好，Streamlit！")
'''
# 创建一个代码块，用于展示python_code的内容
# 并设置language为None，即该代码块无语法高亮
st.code(python_code, language=None)
# 创建一个代码块，用于展示python_code的内容
# language为默认，即该代码块以Python语法高亮
st.code(python_code)
# 创建一个代码块，用于展示python_code的内容
# language为默认，即该代码块以Python语法高亮
# 并设置line_numbers为True，即该代码块有行号
st.code(python_code, line_numbers=True)

st.subheader('Java代码块')
# 创建要显示的Java代码块的内容
java_code = '''public class Hello {
    public static void main(String[] args) {
        System.out.println("你好！ Streamlit!");
    }
}
'''

# 创建一个代码块，用于展示java_code的内容
# 设置language为Java，即该代码块以Java语法高亮
st.code(java_code, language='java')

st.subheader('JavaScript代码块')
# 创建要显示的JavaScript代码块的内容
javascript_code = '''<p id="demo"></p>
<script>
    document.getElementById("demo").innerHTML ="你好！ Streamlit!";
</script>
'''

# 创建一个代码块，用于展示javascript_code的内容
# 设置language为JavaScript，即该代码块以JavaScript语法高亮
st.code(javascript_code, language='javascript')
