import torch
import torch.nn as nn

# 示例：展示 Dropout 在訓練和評估模式下的差異
class TestModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = nn.Dropout(0.5)  # 50% 的神經元會被關閉

    def forward(self, x):
        return self.dropout(x)


model = TestModel()
input_tensor = torch.ones(1, 5)

print("=== Dropout 層行為 ===")
# 訓練模式
model.train()
print("訓練模式 (model.train()):")
for i in range(3):
    output = model(input_tensor)
    print(f"第 {i + 1} 次: {output}")
    # 每次輸出可能不同，因為隨機關閉神經元

# 評估模式
model.eval()
print("\n評估模式 (model.eval()):")
for i in range(3):
    output = model(input_tensor)
    print(f"第 {i + 1} 次: {output}")
    # 每次輸出相同，所有神經元都參與計算