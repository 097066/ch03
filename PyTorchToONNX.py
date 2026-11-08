# C:\Users\suyu9\PycharmProjects\GPUProject\F5386-master\ch03  模型部署與推理 (Inference) 範例

import torch
import torch.nn as nn
import cv2
import numpy as np

class NeuralNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten() # 將 2D 的圖片 28X28 攤平成 1D 的 784 個數值，因為後面的 Linear 層（線性層）不接受矩陣，只接受向量。
        self.base_model = nn.Sequential(  # 從 784 降到 128 - 64 - 32，最後輸出 10（對應 0-9 數字）。
            nn.Linear(28 * 28 * 1, 128),
            nn.ReLU(),  # 激活函數，幫助模型學習非線性的特徵。
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        return self.base_model(x)


# 加載模型
model = NeuralNet()
model.load_state_dict(torch.load('model_weights.pth', map_location='cpu'))
model.eval()  # 用於將模型設置為評估模式

# 讀取和預處理圖像
image = cv2.imread('number5.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (28, 28))

# 反轉顏色（如果需要）
if np.mean(image) > 127:
    image = 255 - image

# 轉換為 tensor
tensor = torch.from_numpy(image.astype(np.float32) / 255.0)
tensor = tensor.unsqueeze(0).unsqueeze(0)  # (1, 1, 28, 28)  # 維度擴增 (Dimension Squeeze)  第一個 unsqueeze(0)：加上 Channel (1，灰階)。
                                           # 第二個 unsqueeze(0)：加上 Batch Size (1，代表只有一張圖)。即使只有一張圖片，也要偽裝成一個「批次」才能送入模型。
# 預測
with torch.no_grad():
    output = model(tensor)
    prediction = torch.argmax(output, dim=1).item()
    probability = torch.softmax(output, dim=1)[0, prediction].item()

print(f"預測數字: {prediction}")
print(f"置信度: {probability:.4f}")

# 顯示結果
display = cv2.resize(image, (200, 200))
cv2.putText(display, f'Pred: {prediction}', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
cv2.imshow('Result', display)
cv2.waitKey(0)
cv2.destroyAllWindows()