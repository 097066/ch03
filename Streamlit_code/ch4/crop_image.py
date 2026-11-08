# 第四章/crop_image.py
import streamlit as st
from PIL import Image
import io

# 全域頁面設定
st.set_page_config(
    page_title="圖片剪切器",
    page_icon="🖤",
    layout="centered"
)

st.title("📷 圖片剪切器")

# 1. 上傳檔案
uploaded_file = st.file_uploader(
    "請上傳照片（JPG/PNG）",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    # 2. 讀取並顯示原圖
    image = Image.open(uploaded_file)
    st.subheader("原始圖片")
    st.image(image, use_container_width=True)
    st.write('原始圖片的圖像大小：', image.size)

    # 裁剪圖像
    crop_image = image.crop((50, 50, image.size[0]-50, image.size[1]-50))
    # 展示裁剪后的圖像
    st.title("裁剪圖像")
    st.image(crop_image)
    st.write('裁剪后的圖像大小：', crop_image.size)

