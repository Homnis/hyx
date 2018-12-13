'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/18 15:21
desc: TODO
'''
import re
# 读取网页中的数据到程序中
with open('dy_index.html', 'r') as f:

    # 定义正则表达式
    # reg = r"<a.*?title=\"(.*?)\">" # 电影名称
    # reg = r"<a\s+href='(.*?)'.*?>" # 电影链接
    reg = r"<a\s+href='(.*?)'\s+title=\"(.*?)\">"

    # 筛选数据
    result = re.findall(reg, f.read())

    # 得到目标数据
    for i in result:
        print(">>>> http://www.dy2018.com" + i[0] , i[1])
