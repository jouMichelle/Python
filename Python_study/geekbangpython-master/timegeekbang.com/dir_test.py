# 文件目录操作标准库
import os

# 获取当前相对路径
print(os.path.abspath('.'))
# 获取当前上级相对路径
print(os.path.abspath('..'))
# 判断文件是否存在
print(os.path.exists('C:/Users'))
# 判断是否是文件
print(os.path.isdir('C:/Users'))
# 拼接路径
print(os.path.join('/tmp/a/', 'b/c'))

from pathlib import Path
# 获取当前相对路径对应的绝对路径
p = Path('.')
print(p.resolve())
# 判断是否是目录文件
print(p.is_dir())
# 建立目录
# 指定创建文件或目录的路径
q = Path('/tmp/a/b/c')
#  parents=True 如果上级目录不存在则自动创建
Path.mkdir(q, parents=True)
