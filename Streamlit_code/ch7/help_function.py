# 第七章/help_function.py
import streamlit as st

st.title('显示自定义函数的帮助信息')

def square_sum(num1, num2):
  """
  计算两个数的平方和

  参数:
    - num1: 第一个数
    - num2: 第二个数

  返回值:
    - num1和num2平方和的结果
  """
  # 各自计算平方
  square1 = num1 ** 2
  square2 = num2 ** 2
  # 返回两数平方和
  return square1 + square2

st.help(square_sum)
