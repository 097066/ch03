# 第七章/page_config.py
import streamlit as st

st.set_page_config(
    page_title="机器学习Web应用",  # 页面标题
    page_icon=":shark:",  # 页面图标
    layout="wide",   # 设置布局为整个页面
    initial_sidebar_state="expanded",   # 初始状态侧边栏
    menu_items={
        'Get Help': 'mailto:847854712@qq.com',
        'Report a Bug': None,
        'About': "# 机器学习Web应用介绍",
    }
)
st.title("修改页面设置")
# 使用with语法，创建侧边栏
with st.sidebar:
    add_radio = st.radio(
        "你喜欢Streamlit吗？",
        ("是的，很喜欢", "不，不喜欢")
    )

st.markdown("""
* 页面标题设置为“机器学习Web应用”
* 页面图标设置为“:shark:”
* 页面布局设置为“wide”
* 侧边栏显示设置为“expanded”
* 菜单栏
    * “Get Help”设置为邮箱地址
    * “Report a Bug”设置为不显示
    * “About”设置为“机器学习Web应用介绍”
""")
