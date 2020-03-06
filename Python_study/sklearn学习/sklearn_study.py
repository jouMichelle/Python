#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/3/6 14:45 
# @Author : Michelle jou
# @Site :  
# @File : sklearn_study.py 
# @Software: PyCharm
from sklearn import datasets
#  引入Iris数据
iris = datasets.load_iris()
# 打印数据对应列的名称
print(iris.feature_names)

print(iris.data)
# 输出结果
print(iris.target)
# 结果含义
print(iris.target_names)



