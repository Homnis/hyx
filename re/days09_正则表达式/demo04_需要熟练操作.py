'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/18 14:50
desc: TODO
'''
import re
# 网页中的一段片段代码：需要图片的链接  src="........"
s = ''' <img src="./images/1.jpg"/> 
<img src="./images/2.jpg"/> 
<img src="./images/3.jpg"/> 
<img src="./images/4.jpg"/> 
<img src="./images/5.jpg"/> '''


# 定义正则表达式
reg = r'src="(.*)"'

img_path = re.findall(reg, s)

print(img_path)

#########################################

s = "<div>第一个div的内容</div><p>段落内容</p><div>第二个div的内容</div>"

# 贪婪匹配：从目标数据的外围开始匹配，如果一旦匹配到开头和结束的特征数据，直接获取。
# 尽可能多的匹配目标数据
# reg = r'<div>(.*)</div>'
# 懒惰匹配|非贪婪匹配：尽可能少的匹配数据，从头开始扫描数据，一旦符合特征直接提取
reg = r'<div>(.*?)</div>'

res = re.findall(reg, s)
print(res)
