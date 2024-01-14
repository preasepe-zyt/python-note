import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import ElasticNet
from sklearn.datasets import make_regression

plt.figure(figsize=(12, 6))

# 生成模拟数据
X, y = make_regression(n_features=10, n_samples=1000, noise=10)

# 初始化弹性网络回归
enet = ElasticNet(alpha=0.5, l1_ratio=0.5)

# 模型拟合
enet.fit(X, y)

# 预测
y_pred = enet.predict(X)

# 绘制预测值与真实值的比较图
plt.scatter(y_pred, y, color='red')
plt.plot(np.arange(-400, 400), np.arange(-400, 400), color='blue')

plt.title("Elastic Net Regression")
plt.xlabel("Predicted Values")
plt.ylabel("True Values")
plt.show()