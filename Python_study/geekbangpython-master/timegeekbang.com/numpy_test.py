# numpy库一般用于高性能科学计算和数据分析，是常用的高级数据分析库的基础包
# numpy库是 c语言创建的库，所以性能较快。需要引用进来则需要进行安装
# numpy库安装命令 pip install numpy

import numpy as np

# 使用numpy定义一个列表
arr1 = np.array([2, 3, 4])
print(arr1)
print(arr1.dtype)

# 定义小数的列表
arr2 = np.array([1.2, 2.3, 3.4])
print(arr2)
print(arr2.dtype)

#  进行列表累加计算
print(arr1 + arr2)

# 列表进行标量计算
print(arr2 * 10)

# 列表转换为 numpy 的二维矩阵
data = [[1, 2, 3], [4, 5, 6]]
arr3 = np.array(data)
print(arr3)
print(arr3.dtype)

# 创建一个值为 0 的 矩阵
print(np.zeros(10))
# 创建一个3行5列值全部为 0 的矩阵
print(np.zeros((3, 5)))
# 创建一个 4行6列的值全部为 1 的矩阵
print(np.ones((4, 6)))
# 创建一个三维矩阵且值为空
print(np.empty((2, 3, 2)))

# numpy 列表进行切片操作
arr4 = np.arange(10)
# 切片进行赋值
arr4[5:8] = 10
print(arr4)

# 创建一个副本
arr_slice = arr4[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
print(arr4)
