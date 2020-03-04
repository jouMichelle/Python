# 获取一个网站的图片,使用正则进行匹配
import requests
import re
content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text

# print(content)


# < div class ="grid-item work-thumbnail" >
# < a href="(.*?)".*?title">(.*?)</div>
# < div class ="author" > LynnWei < / div >

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
# print(results)


for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))