#  matplotlib 绘图库
#  matplotlib 安装 ： pip install matplotlib
import matplotlib.pyplot as plt

# # 绘制简单的曲线
# plt.plot([1, 3, 5], [4, 8, 10])
# # 显示所画的图
# plt.show()

#  matplotlib 绘制 numpy数据
import numpy as np

# # x轴的定义域为 -3.14~3.14，中间间隔100个元素
# x = np.linspace(-np.pi, np.pi, 100)
# # 绘制坐标图形
# plt.plot(x, np.sin(x))
# # 显示所画的图
# plt.show()

# # 绘制多条曲线
# # 定义域为： -2pi 到 2pi
# x = np.linspace(-np.pi * 2, np.pi * 2, 100)
# # 创建图表1,dpi为设置图片的精度,精度越高图片越详细,图片体积越大。
# plt.figure(1, dpi=50)
# # 画四条线
# for i in range(1, 5):
#         plt.plot(x, np.sin(x / i))
# plt.show()


# # 生成一个直方图
# # 创建图表1，dpi代表图片精细度，dpi越大文件越大，杂志要300以上
# plt.figure(1, dpi=50)
# data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
# # 只要传入数据，直方图就会统计数据出现的次数
# plt.hist(data)
# # 显示所画的图
# plt.show()


# # 生成散点图
# x = np.arange(1, 10)
# y = x
# fig = plt.figure()
# # c = 'r'表示散点的颜色为红色，marker 表示指定三点多形状为圆形
# plt.scatter(x, y, c='r', marker='o')
# # 显示所画的图
# plt.show()


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# iris = pd.read_csv("./iris_training.csv")
# # 显示前五行信息
# print(iris.head())
# # 绘制散点图
# iris.plot(kind="scatter", x="120", y="4")
# # 没啥用，只是让pandas 的plot() 方法在pyCharm上显示
# plt.show()


# seaborn绘图使用
#  seaborn 安装 ： pip install seaborn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# iris = pd.read_csv("./iris_training.csv")
# # 设置样式
# sns.set(style="white", color_codes=True)
# # 设置绘制格式为散点图
# sns.jointplot(x="120", y="4", data=iris, size=5)
# # distplot绘制曲线
# sns.distplot(iris['120'])
# # 没啥用，只是让pandas 的plot() 方法在pyCharm上显示
# plt.show()


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")
iris = pd.read_csv("./iris_training.csv")
sns.set(style="white", color_codes=True)
# FacetGrid 一般绘图函数
# hue 彩色显示分类0/1/2
# plt.scatter 绘制散点图
# add_legend() 显示分类的描述信息
sns.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, "120", "4").add_legend()
sns.FacetGrid(iris, hue="virginica", size=5).map(plt.scatter, "setosa",
"versicolor").add_legend()
# 没啥用，只是让pandas 的plot() 方法在pyCharm上显示
plt.show()
