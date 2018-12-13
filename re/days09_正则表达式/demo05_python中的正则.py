'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/18 14:59
desc: python中正则操作函数
'''
import re
'''
['I', 'S', 
'compile',  'findall', 'finditer', 'match', 'search',
  'split', 'sub', 'subn']
'''

target = "hello regular expression"
# 创建正则表达式：2种创建方式

# 1. 快捷操作方式
# reg = r'l' # <class 'str'>
# print(type(reg))
#
# res = re.findall(reg, target)
# print(res)

# 2. 正则表达式对象
# reg2 = re.compile(r'l') # <class 're.Pattern'>
# print(type(reg2))
#
# res = reg2.findall(target)
# print(res)
'''
公司项目中，两种正则表达式的操作都有使用【同一个项目组一般只会要求一种(代码质量检测)】
'''

# 正则表达式的操作函数
'''
match(): 默认从目标数据开头位置开始匹配[可以指定开始匹配位置]->得到一个re.Match对象
search()
findall()
finditer()
split()
sub()
subn()
'''
# r1 = r'he(ll)o'
# res = re.match(r1, target) # 必须从目标字符串的开头位置[指定位置]开始查询
# print(res)
# print(res.group())
# print(res.group(1))

# r2 = r'e(ll)o'
# res = re.search(r2, target) # 扫描整个字符串，得到第一个匹配的结果
# print(res)
# print(res.group())


r3 = r'l'
res = re.findall(r3, target) # 扫描整个字符串，将匹配的结果存储到列表中
print(res)

r4 = r'l'
res = re.finditer(r4, target) # 扫描整个字符串，将匹配到的结果存储到生成器中
print(res)
print(next(res).group())