'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/18 15:51
desc: TODO
'''
'''
TASK1: 采集新浪新闻数据[社会新闻]
TASK2: 采集智联招聘PYTHON岗位信息[岗位名称、薪水、招聘公司，工作地点]
    提示：如果要使用爬虫~请返回智联招聘旧版网站
TASK3: 采集电影天堂~最新发布的200部电影名称+链接
TASK4: 采集桌面壁纸
'''
from urllib import request

res = request.urlopen("http://img.netbian.com/file/2018/1017/6810f2f0bd00be83295b4b39a2344d31.jpg")

with open("1.jpg", "wb") as f:
    f.write(res.read())
'''
anonconda
miniconda:管理python环境
'''