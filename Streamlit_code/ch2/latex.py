# 第二章/latex.py
import streamlit as st  # 导入Streamlit并用st代表它
import sympy  # 导入SymPy


# 显示LaTeX字符串
st.subheader('显示LaTeX字符串')
st.latex(r'''\textstyle\sum_{k=0}^{n-1} cx^k =
         c \left(\frac{1-x^{n}}{1-x}\right)''')

# 显示SymPy表达式
st.subheader('显示SymPy表达式')
# 定义x为符号x
x=sympy.Symbol('x')
# expr为求x的平方根
expr = sympy.sqrt(x)
st.latex(expr)
