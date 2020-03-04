
from urllib import request

url ='http://www.baidu.com'
# 发送get请求,设置超时时间为 1 单位为秒
response = request.urlopen(url,timeout=1)
# 读取数据，进行指定字符编码
print (response.read().decode('utf-8'))
