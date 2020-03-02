# print('abc',end='\n')
# print('abc')
#
# def func (a, b, c):
#     print('a= %s' %a)
#     print('b= %s' %b)
#     print('c= %s' %c)
#
#
# func(1, c=3)


# 可变长度函数
# 取得参数的个数
# def  howlong(first, *other):
#     print( 1 + len(other))
#
# howlong()

#
# var1 = 123
#
# def func():
#   global 将变量声明为全局变量
#     global var1
#     var1 = 456
#     print(var1)
#
#
#
# func()
# print(var1)

# 迭代器
# iter() next()
# list1 =[1, 2, 3]
# it = iter(list1)
# print( next(it))
# print( next(it))
# print( next(it))
# print( next(it)) # except


#
# for i in range(10,20,0.5):
#     print(i)

# 自定义函数迭代器
# def frange(start, stop, step):
#     x = start
#     while x < stop:
#         yield x
#         x += step

# for i in frange(10,20,0.5):
#     print(i)


# Python中的lambda表达式
# def true():return True
# lambda : True


# 定义一个函数
# def add(x,y):
#     return x+y

# 函数简写
# def add(x,y): return x+y
# 函数使用lambda表达式
# lambda  x,y: x+y


# lambda  x:x<= (month, day)

# def func1(x):
#     return  x<= (month, day)

# lambda  item:item[1]

# def func2(item):
#         return item[1]


#  Python内置函数
# filter() map() reduce() zip()
# 查询函数使用说明
# help(filter)

# filter() 函数
# a = [1, 2, 3, 4, 5, 6, 7]
# b = list(filter(lambda x: x > 2, a))
# print(b)

# map() 函数
# 查询函数使用说明
# help(map)
# a = [1, 2, 3]
# b = map(lambda x: x, a)
# print(b)
# c = list(map(lambda x: x, a))
# print(c)
# d = list(map(lambda x: x + 1, a))
# print(d)
# f = [4, 5, 6]
# g = list(map(lambda x, y: x + y, a, f))
# print(g)


#  reduce() 函数
# 函数帮助查询
# help(reduce)
# reduce()函数使用需要先引入进来,此操作可以称为导包
# from functools import reduce
#
# a = reduce(lambda x, y: x + y, [2, 3, 4], 1)
# # 其执行的效果为 ((1+2)+3)+4
# print(a)


# zip()函数
# (1, 4)
# (2, 5)
# (3, 6)
# for i in zip((1,2,3),(4,5,6)):
#      print(i)


def func():
    a = 1
    b = 2
    return a + b


def sum(a):
    def add(b):
        return a + b

    return add


# add 函数名称或函数的引用
# add() 函数的调用

num1 = func()
num2 = sum(2)
print(type(num1))
print(type(num2))
print(num2(4))
# count()
