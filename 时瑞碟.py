import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
from matplotlib.font_manager import FontProperties
data = pd.read_excel("C:/Users/79403/Desktop/pcr.xlsx")
new_names = dict("a","b","c","d")
mean_cols = {'DIR', 'SPEED', 'GUST', 'TEMP_F', 'TEMP_C', 'MONTH', 'TEMP_C', 'MONTH'}
data = data.rename(columns=mean_cols)



font = FontProperties(fname='/Library/Fonts/Songti.ttc')

def draw():
    # 定义热图的横纵坐标
    xLabel = ['A', 'B', 'C', 'D', 'E']
    yLabel = ['1', '2', '3', '4', '5']

    # 准备数据阶段，利用random生成二维数据（5*5）
    data = []
    for i in range(5):
        temp = []
        for j in range(5):
            k = random.randint(0, 100)
            temp.append(k)
        data.append(temp)

    # 作图阶段
    fig = plt.figure()
    # 定义画布为1*1个划分，并在第1个位置上进行作图
    ax = fig.add_subplot(111)
    # 定义横纵坐标的刻度
    ax.set_yticks(range(len(yLabel)))
    ax.set_yticklabels(yLabel, fontproperties=font)
    ax.set_xticks(range(len(xLabel)))
    ax.set_xticklabels(xLabel)
    # 作图并选择热图的颜色填充风格，这里选择hot
    im = ax.imshow(data, cmap=plt.cm.hot_r)
    # 增加右侧的颜色刻度条
    plt.colorbar(im)
    # 增加标题
    plt.title("This is a title", fontproperties=font)
    # show
    plt.show()


d = draw()