# 将小说的主要人物记录在文件中
# 创建一个文件且以可写入方式打开
file1 = open('name.txt', 'w')
# 往文件写入数据
file1.write('诸葛亮')
# 关闭文件且保存（文件在当前执行程序目录下）
file1.close()

# 以只读形式打开文件
file2 = open('name.txt')
# 读取文件内容且打印出来
print(file2.read())
# 关闭文件
file2.close()

# 打开原有文件,在文件末尾进行追加写入
file3 = open('name.txt', 'a')
# 写入内容
file3.write('刘备')
# 关闭文件
file3.close()

# 以只读方式打开文件
file4 = open('name.txt')
# 只读一行方式读取
print (file4.readline())


# 读取文件逐行进行处理,只读方式打开
file5 = open('name.txt')
# 循环遍历出行
for line in file5.readlines():
    print(line)
    print('=====')


# 将文件逐行读取，读取完后指针回到首行
# 只读方式打开
file6 = open('name.txt')
print('当前文件指针的位置 %s' % file6.tell())
print('当前读取到了一个字符，字符的内容是 %s' % file6.read(1))
print('当前文件指针的位置 %s' % file6.tell())
# 第一个参数代表偏移位置，第二个参数  0 表示从文件开头偏移  1表示从当前位置偏移，   2 从文件结尾
file6.seek(5, 0)
print('我们进行了seek操作')
print('当前文件指针的位置 %s' % file6.tell())
print('当前读取到了一个字符，字符的内容是 %s' % file6.read(1))
print('当前文件指针的位置 %s' % file6.tell())
file6.close()
