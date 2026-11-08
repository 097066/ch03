# quick_test.py
import torch
import torch.nn as nn
import cv2
import numpy as np

class ConvBN(nn.Module):
    def __init__(self, cin, cout):
        super().__init__()
        self.conv = nn.Conv2d(cin, cout, kernel_size=3, padding='same')
        self.bn = nn.BatchNorm2d(num_features=cout)
        self.act = nn.ReLU()
    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        return self.act(x)

class CNN(nn.Module):
    def __init__(self, kernel_size=3):
        super().__init__()
        self.encoder = nn.Sequential(
            ConvBN(3, 16),
            ConvBN(16, 16),
            nn.MaxPool2d(kernel_size=2),

            ConvBN(16, 32),
            ConvBN(32, 32),
            nn.MaxPool2d(kernel_size=2),

            ConvBN(32, 64),
            ConvBN(64, 64),
            nn.MaxPool2d(kernel_size=2),
        )
        self.flatten = nn.Flatten() # (64, 32, 32) -> (64*32*32)
        self.classifier = nn.Sequential(
            nn.Dropout(0.3),
            nn.Linear(64*32*32, 256),
            nn.Dropout(0.3),
            nn.ReLU(),
            nn.Linear(256, 3),
        )
    def forward(self, x):
        x = self.encoder(x)
        x = self.flatten(x)
        x = self.classifier(x)
        return x

# Build a model and move to GPU device
device = "cuda" if torch.cuda.is_available() else "cpu"
model = CNN(kernel_size=7).to(device)


# 加載模型

model.load_state_dict(torch.load('best2.pth', map_location='cpu'))
model.eval()  # 用於將模型設置為評估模式

# --- 修正後的區塊 ---

# 1. 讀取與 Resize (OpenCV 格式: H, W, C -> 256, 256, 3)
# image = cv2.imread(r'C:\Users\suyu9\Desktop\pneumonia\train\pneumonia\person325_virus_665.jpeg') #2
# image = cv2.imread(r'C:\Users\suyu9\Desktop\pneumonia\train\pneumonia\person342_virus_701.jpeg') #2
# image = cv2.imread(r'C:\Users\suyu9\Desktop\pneumonia\train\pneumonia\person354_bacteria_1635.jpeg') #1
# image = cv2.imread(r'C:\Users\suyu9\Desktop\pneumonia\train\pneumonia\person466_bacteria_1984.jpeg') #1
image = cv2.imread(r'C:\Users\suyu9\Desktop\pneumonia\train\normal\IM-0164-0001.jpeg') #0
image1 = cv2.resize(image, (256, 256))

# 2. 轉換為 Tensor 並正規化
tensor = torch.from_numpy(image1.astype(np.float32) / 255.0)

# 3. 調整維度順序：從 (H, W, C) 改為 (C, H, W)
# Permute 把 index 2 (Channel) 放到最前面
tensor = tensor.permute(2, 0, 1)

# 4. 增加 Batch 維度：從 (C, H, W) 改為 (1, C, H, W)
tensor = tensor.unsqueeze(0)

# 5. 【重要】將 Tensor 移動到與模型相同的設備 (GPU/CPU)
tensor = tensor.to(device)
# 預測
with torch.no_grad():
    output = model(tensor)
    prediction = torch.argmax(output, dim=1).item()
    probability = torch.softmax(output, dim=1)[0, prediction].item()

print(f"預測數字: {prediction}")
print(f"置信度: {probability:.4f}")
dict1 = {0:('normal',(0,255,0)), 1:('bacteria',(0,0,255)), 2:('virus',(255,0,0))}
# 顯示結果
# display = cv2.resize(image, (200, 200))
cv2.putText(image, f'Pred: {dict1[prediction][0]}', (10, 60),
            cv2.FONT_HERSHEY_SIMPLEX, 2, dict1[prediction][1], 3)
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()