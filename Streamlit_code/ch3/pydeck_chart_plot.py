# 第三章/pydeck_chart_plot.py
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# 生成北京市的随机点，其中39.9, 116.4是北京的经纬度
# 该数据集模拟的是1000个二维平面上的坐标点,
# 其中: 纬度平均在39.9°左右,经度平均在116.4°左右,并除以50进行缩放
chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [39.9, 116.4],
    columns=['lat', 'lon'])

# 定义地图的初始视图状态。
# 具体来说:
# - pdk.ViewState() 创建一个ViewState对象。
# - latitude=39.9   指定初始视角的纬度为39.9度。
# - longitude=116.4 指定初始视角的经度为116.4度。
# - zoom=11         指定初始视图的缩放级别为11。
# - pitch=50        指定初始俯视角度为50度。

initial_view_state = pdk.ViewState(
    latitude=39.9,
    longitude=116.4,
    zoom=11,
    pitch=50,
)
# 定义一个名为`layer_hexagon`的图层对象。
# 使用`HexagonLayer`指定六边形图层类型
# HexagonLayer有以下属性:
# - data=chart_data 指定数据源。
# - get_position='[lon, lat]' 指定经纬度字段。
# - radius=200  每个六边形的半径为200。
# - elevation_scale=4  生成的六边形的海拔(高度)会是数据密度的4倍。
# - elevation_range=[0, 1000] 允许的海拔高度范围为0到1000。
# - pickable=True 允许鼠标选择六边形。
# - extruded=True 用三维方式渲染六边形。

layer_hexagon = pdk.Layer(
    'HexagonLayer',
    data=chart_data,
    get_position='[lon, lat]',
    radius=200,
    elevation_scale=4,
    elevation_range=[0, 1000],
    pickable=True,
    extruded=True,
)

# 定义一个名为`layer_Scatter`的图层对象。
# 指定图层类型为`ScatterplotLayer`,即散点图层。
# 主要属性如下:
# - data=chart_data  定义数据源。
# - get_position='[lon, lat]' 指定数据中的经纬度字段。
# - get_color='[200, 30, 0, 160]' 指定散点颜色。
# - get_radius=200 指定散点大小半径为200。

layer_Scatter = pdk.Layer(
    'ScatterplotLayer',
    data=chart_data,
    get_position='[lon, lat]',
    get_color='[200, 30, 0, 160]',
    get_radius=200,
)
# - pdk_chart 定义了一个Pydeck的Deck对象
# - 它不使用默认样式
# - 但是定义了一个初始视图状态
# - 并添加了两个不同类型的图层
# - 最终形成一个带六边形和散点的3D地图

pdk_chart = pdk.Deck(
    map_style=None,
    initial_view_state=initial_view_state,
    layers=[layer_hexagon, layer_Scatter]
)

st.subheader("展示Pydeck库的图像")
st.pydeck_chart(pdk_chart)
