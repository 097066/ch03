# 第六章/sidebar_travel.py
import streamlit as st

st.title('山西旅游助手')

cities = ['太原', '大同', '临汾', '朔州', '忻州']
# 生成城市下拉按钮
selected_city = st.sidebar.selectbox('选择城市', cities)
# 各城市旅游景点数据
spots = {'太原': ['双塔寺', '碑林公园', '晋祠'],
         '大同': ['云冈石窟', '悬空寺', '善化寺'],
         '临汾': ['壶口瀑布', '华门', '尧帝古居', '尧庙'],
         '朔州':['应县木塔', '净土寺', '广武城'],
         '忻州': ['五台山', '雁门关', '芦芽山']
        }
# 根据城市下拉按钮的选项，动态生成景点下拉按钮
selected_spot = st.sidebar.selectbox('选择景点', spots[selected_city])

# 判断是否点击了查询按钮
if st.sidebar.button('查询'):
    # 呈现用户的选择了哪个城市的哪个景点。
    st.write(f'您选择的景点是:{selected_city} - {selected_spot}')

st.write('查询结果和景点详情将显示在这里...')
