# Python发送http请求
# request用于发起数据,parse处理post请求数据
from urllib import parse
from urllib import request

# 发送get请求
# response2 = request.urlopen('http://httpbin.org/get', timeout=1)
# print(response2.read().decode('utf-8'))


# 发送post请求
# 封装post请求数据
# data = bytes(parse.urlencode({'word': 'hello'}), encoding='utf8')
# print(data)
# response = request.urlopen('http://httpbin.org/post', data=data)
# print(response.read().decode('utf-8'))

# response3 = request.urlopen('http://httpbin.org/get', timeout=0.1)

import urllib
import socket

# 模拟发送http请求超时,并捕获
try:
    response3 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
