# 第二章/markdown.py
import streamlit as st  # 导入Streamlit并用st代表它

# 标题格式
st.markdown('# 一级标题')
st.markdown('## 二级标题')
st.markdown('### 三级标题')
st.markdown('#### 四级标题')
st.markdown('##### 五级标题')
st.markdown('###### 六级标题')
# 分割线
st.markdown('***')
st.markdown('普通文本')
st.markdown(':red[红色文本]')

# 字体样式
st.markdown('*斜体文本*')
st.markdown('_斜体文本_')
st.markdown('**粗体文本**')
st.markdown('__粗体文本__')
st.markdown('***粗斜体文本***')
st.markdown('___粗斜体文本___')

# 分割线
st.markdown('***')
# 无序列表
st.markdown('''- python
- java
- c''')

# 分割线
st.markdown('***')
# 有序列表
st.markdown('''1. 第一项 
2. 第二项 
3. 第三项''')

# 分割线
st.markdown('***')
# 表格
st.markdown('''
| 表头1 | 表头2 |
| :-: | :-: |
| 单元格1 | 单元格2 |
| 单元格3 | 单元格4 |''')
