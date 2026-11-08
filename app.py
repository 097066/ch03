# C:\Users\suyu9\PycharmProjects\GPUProject\F5386-master\ch03\app.py  模型部署與推理 (Inference) 範例
# 切換到 Pillow (PIL) 是一個明智的選擇，因為它在網頁環境（如 Streamlit）中更輕巧，且與 torchvision.transforms 的相容性極佳。


import streamlit as st
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image, ImageOps
import numpy as np


# 1. 定義模型架構
class NeuralNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.base_model = nn.Sequential(
            nn.Linear(28 * 28, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        return self.base_model(x)


# 2. 載入模型
@st.cache_resource
def load_model():
    model = NeuralNet()
    model.load_state_dict(torch.load('model_weights.pth', map_location='cpu'))
    model.eval()
    return model


# 網頁標題
st.title("🔢 手寫數字辨識 (PIL 版)")

model = load_model()
uploaded_file = st.file_uploader("請上傳圖片...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # --- 使用 Pillow 處理圖片 ---
    # 讀取並轉為灰階 ('L' mode)  這一步直接將任何格式（RGB, RGBA）轉為灰階，避免了維度錯誤。
    img = Image.open(uploaded_file).convert('L')

    # 自動顏色修正：MNIST 是黑底白字
    # 如果圖片背景是白的 (平均值 > 127)，就進行反轉  這是 Pillow 內建的反轉功能。比起 255 - array，它直接作用於圖片物件，更符合物件導向邏輯。
    if np.mean(np.array(img)) > 127:
        img = ImageOps.invert(img)

    # 顯示給使用者看 (放大顯示)
    st.image(img, caption="模型看到的樣子 (28x28 黑底白字)", width=150)

    # --- 使用 torchvision.transforms 進行標準化 ---
    # 這裡的步驟取代了手動的 unsqueeze 和除以 255
    preprocess = transforms.Compose([
        transforms.Resize((28, 28)),
        transforms.ToTensor(),  # 包含轉為 Tensor 與 歸一化至 [0, 1]
        # 當你把一個 PIL Image 丟給它時，它會自動完成三件事：        #
        # 將維度從 (H, W, C) 轉為 (C, H, W)。        #
        # 將數值從 [0, 255] 縮放到 [0.0, 1.0]。        #
        # 轉換成 torch.FloatTensor。
        # 這省去了你手動除以 255 和轉換資料型態的麻煩。
        # 如果你訓練時有做 Normalize，這裡也要加上：
        # transforms.Normalize((0.1307,), (0.3081,))
    ])

    input_tensor = preprocess(img).unsqueeze(0)  # 加上 Batch 維度: (1, 1, 28, 28)

    # --- 推理 ---
    with torch.no_grad():
        output = model(input_tensor)
        prediction = torch.argmax(output, dim=1).item()
        confidence = torch.softmax(output, dim=1)[0][prediction].item()

    # --- 顯示結果 ---
    st.success(f"辨識結果：{prediction}")
    st.metric(label="信心度", value=f"{confidence:.2%}")