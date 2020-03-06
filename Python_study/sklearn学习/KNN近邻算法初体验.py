#!/usr/bin/env python
# coding: utf-8

# 分类：根据数据集目标的特征或属性，划分到已有的类别中
# 常用的分类算法：k近邻(KNN)、逻辑回归、决策树、朴素贝叶斯
# 

# # Iris数据加载



# 通过sklearn 自带数据包加载inis数据
from sklearn import datasets
iris = datasets.load_iris()

#  样本数据与结果分别赋值到 “x” ，“y”
x = iris.data
y = iris.target

# 确认数据输出维度
print(x.shape)
print(y.shape)




# 模型调用
from sklearn.neighbors import KNeighborsClassifier




# 创建实例
knn = KNeighborsClassifier(n_neighbors=1)
print(knn)




# 模型训练
knn.fit(x,y)




knn.predict([[1,2,3,4]])




x_test = [[1,2,3,4],[2,4,1,2]]
knn.predict(x_test)


# # 设定一个新的K值进行KNN（近邻算法）建模



knn_5 = KNeighborsClassifier(n_neighbors=5)
knn_5.fit(x,y)
knn_5.predict(x_test)




# 确认模型结构
print(knn_5)







