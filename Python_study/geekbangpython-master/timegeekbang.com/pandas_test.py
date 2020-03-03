#  pandas 是用于数据预处理和数据清洗的一个库
#  pandas 安装命令 ： pip install pandas
from pandas import Series, DataFrame
import pandas as pd

# #  pandas 创建一个一维数组
# obj = Series([4, 5, 6, -7])
# print(obj)
# # 取出数组的索引
# print(obj.index)
# # 取出数组的所有的值
# print(obj.values)


# # 自定义索引
# obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'c', 'a'])
# print(obj2)
# # 根据索引进行赋值
# obj2['c'] = 6
# print(obj2)
# # 判断索引是否存在
# print("a" in obj2)

# # 将字典转换成Series
# # 定义一个字典
# sdata = {
#     'beijing': 35000,
#     'shanghai': 71000,
#     'guangzhou': 16000,
#     'shenzhen': 5000}
# # 字典转换成 Series
# obj3 = Series(sdata)
# print(obj3)
# # 将索引修改为缩写形式
# obj3.index = ['bj', 'gz', 'sh', 'sz']
# print( obj3)


# DataFrame的使用
# # 创建一个字典
# data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
#         'year': [2016, 2017, 2018, 2017, 2018],
#         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# # 将字典转换成 DataFrame
# frame = DataFrame(data)
# # 纵坐标是字典中的 key ,横坐标是系统自动生成
# print(frame)
#
# # 数据进行排序
# frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
# print(frame2)
#
# # 提取DataFrame中的数据的两种方式
# print(frame2['city'])
# print(frame2.year)
#
# # DataFrame新增一列
# # 增加一列数据，人工赋值
# frame2['new'] = 100
# print(frame2)
#
# #  增加新的一列，通过计算得到值
# frame2['cap'] = frame2.city == 'beijing'
# print( frame2)


# # DataFrame 字典嵌套字典赋值
# pop = {'beijing': {2008: 1.5, 2009: 2.0},
#        'shanghai': {2008: 2.0, 2009: 3.6}
#        }
# # 嵌套字典转换成 DataFrame
# frame3 = DataFrame(pop)
# print(frame3)
# # 行列转置,将行索引转换成列索引，列索引转换成行索引
# print(frame3.T)


#  重新索引学习
# 创建一个新的  Series
# obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])
# # 新增一个不存在的索引
# # obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'])
# # 将空值进行填充 0
# obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
# print(obj5)
#
# # 创建一个新的  Series
# obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
# # 将空值使用邻近的值进行填充 ffill 前面   bfill 后面
# print( obj6.reindex(range(6),method='bfill'))


# 缺失值删除操作
from numpy import nan as NA

#
# data = Series([1, NA, 2])
# print(data)
# # 删除缺失值
# print(data.dropna())


# # DataFrame 缺失值删除
# data2 = DataFrame([[1., 6.5, 3], [1., NA, NA], [NA, NA, NA]
#                    ])
# # print(data2)
# # 删除缺失值,部分缺失值列保留
# print(data2.dropna(how='all'))
#
# # 全部是缺失值的一整列进行删除
# # 将一列赋值为缺失值
# data2[4] = NA
# print(data2)
# # 删除整列都是缺失值的列
# print(data2.dropna(axis=1, how='all'))
#
# # 将缺失值填充为 0
# # 这个修改的是 data2 的副本
# data2.fillna(0)
# # 增加 inplace=True 则将 data2 中的缺失值也进行修改了
# print(data2.fillna(0, inplace=True))
# print(data2)


# 索引层次化结构
import numpy as np

data3 = Series(np.random.randn(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data3)
# 提取 b 索引的内容
print(data3["b"])
# 提取多个索引
print(data3["b":"c"])
# 转换成 DataFrame
print(data3.unstack())
# 将数据转换回来
print(data3.unstack().stack())
# print ( data3['b':'c'])
