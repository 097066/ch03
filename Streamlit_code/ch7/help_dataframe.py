# 第七章/help_dataframe.py
import streamlit as st
import pandas as pd
import numpy as np

st.title('显示数据框的帮助信息')

df = pd.DataFrame(
   np.random.randn(3, 4),
   columns=('列%d' % i for i in range(4)))
st.help(df)
