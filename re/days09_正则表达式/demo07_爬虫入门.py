'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/18 15:42
desc: TODO
'''
from urllib import request

response = request.urlopen("http://www.sina.com.cn")

html = response.read()

print(html.decode("utf-8"))

with open("sina.html", 'wb') as f:
    f.write(html)
