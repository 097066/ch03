# 第七章/help_class_obj.py
import streamlit as st


# 定义Person
class Person:
    """一个简单的描述人的类"""

    def __init__(self, name, age):
        """Pesrson类的初始化方法

        参数:
            name (str): 名字
            age (int): 年龄
        """
        self.name = name
        self.age = age

    def walk(self):
        """散步的方法

        打印一个字符串，包含该对象的名字
        """
        print(f'{self.name}正在散步')


st.title('显示自定义类和对象的帮助信息')
# 根据Person类创建两个对象
p_1 = Person('王鑫', 27)
p_2 = Person('Bob', 26)

st.subheader("显示Person类的帮助信息")
st.help(Person)
st.subheader("显示p_1对象的帮助信息")
st.help(p_1)
st.subheader("显示p_2对象的帮助信息")
st.help(p_2)
