#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/3/3 10:17 
# @Author : Michelle jou
# @Site :  
# @File : stdlib_re.py 
# @Software: PyCharm

# 使用 “re”标准库进行匹配字符
import re

p = re.compile("a")
print(p.match("a"))

# 使用“re”标准库结合正则表达式的元字符进行匹配数据

# 正则表达式中元字符使用
# “.”用于匹配任意单个字符,可使用多个但不建议使用
b = re.compile(".")
print(b.match("b"))

# “$”匹配以什么结尾的数据
c = re.compile(".jpg$")
print(c.match("ad.jpg"))

#  “ ^ ”表示以什么为开头
d = re.compile("aa^")
print(d.match("aaabb"))

# “ * ”匹配前面字符出现0次或多次
e = re.compile("ca*t")
print(e.match("ct"))

#  “ + ”匹配前面字符出现1次或多次
f = re.compile("ca+t")
print(f.match("caaaat"))

# “ ？”匹配前面字符出现 0 次或 1 次
g = re.compile("ca?t")
print(g.match("ct"))

# “ {次数} ”匹配前面字符需出现指定次数
h = re.compile("ca{4}t")
print(h.match("caaaat"))

# “ {最小次数,最大次数} ”匹配前面字符出现次数在指定范围
j = re.compile("ca{2,7}t")
print(j.match("caaat"))

#  “ [] ”匹配括号中的一个字符
k = re.compile("c[abc]t")
print(k.match("cat"))
print(k.match("cbt"))

# “ \d ”匹配数字
l = re.compile("\d+")
print(l.match("123022"))

# “ \D ”匹配不包含数字
q = re.compile("\D+")
print(q.match("aadg"))

# “\s”判断是否是纯字母字符串
w = re.compile("\s")
print(w.match("a"))

# 正则表达式分组功能实例
# 在正则表达式前加上 “ r ”表示固定字符不会被转义
e = re.compile(r"(\d+)-(\d+)-(\d+)")
print(e.match("2020-5-20"))
# 取出匹配
print(e.match("2020-03-03").group())
# 取出匹配的第几个
print(e.match("2020-03-03").group(2))
# 取出所有匹配以元组展示
print(e.match("2020-03-03").groups())

# 将取出值赋值给变量
year, month, day = e.match('2018-05-10').groups()
print(year)
print(month)
print(day)

# re标准库中的 match 函数与search 函数的区别
e = re.compile(r"(\d+)-(\d+)-(\d+)")
# 当出现出现特殊字符时，match函数就无法进行匹配进行分组功能
# print(e.match("aa2020-5-20").groups())

# 使用 search 则可以进行匹配，原因是进行搜索字符
print(e.search("aa2020-5-20"))

# re 标准库中的 “sub” 函数，“sub”函数作用是将字符串中的某个值进行替换
phone = "185982153364 # 这是一段电话号码"
phone2 = re.sub(r"#.*$", "", phone)
print(phone2)
