# 1.
# list1 = []
# list2 = []
# while True:
#     a = int(input("向第几个列表输入数据(1,2)："))
#     if a == 1:
#         str1 = input("请输入数据：")
#         list1.append(str1)
#     if a == 2:
#         str2 = input("请输入数据：")
#         list2.append(str2)
#     end = input("是否输入完毕(y/n)")
#     if end == "y":
#         break
# print(list1+list2)


# #2.
# list1 = [1, 2, 3, 4, "a", "b"]
# list2 = [1, 2, 3, "a"]
# if len(list1) >= len(list2):
#     a = list1
#     b = list2
# else:
#     a = list2
#     b = list1
# for n in range(len(b)):
#     if n == len(b)-1:
#         print("是子集")
#     if b[n] in a:
#         continue
#     else:
#         print("不是子集")


# # 3.
# list1 = [1, 2, 3, 4, "a", "b"]
# list1.reverse()
# print(list1)


# # 4.
# list1 = ["a", "e", "c", "B", "A"]
# list1.sort()
# print(list1)


# # 5.
# list1 = [1, 2, 3, 4, "a", "b"]
# while True:
#     a = int(input("要对列表进行什么操作（1.添加2.删除3.修改4.查找）:"))
#     if a == 1:
#         str1 = input("请输入要添加的内容：")
#         list1.append(str1)
#     elif a == 2:
#         str1 = int(input("请输入要删除的项"))
#         print("删除了：", list1.pop(str1))
#     elif a == 3:
#         str1 = int(input("请输入要修改的项"))
#         str2 = input("请输入要改为的内容：")
#         list1[str1] = str2
#         print("修改后的列表问：", list1)
#     elif a == 4:
#         str1 = int(input("请输入要查找的项"))
#         print(list1[str1])
#     else:
#         break


# # 6.
# import random
#
# list1 = []
# i = 0
# while i <= 10:
#     a = random.randint(0, 10)
#     if a not in list1:
#         list1.append(a)
#         i += 1
# print(list1)


# 7.
# tuple1 = (90, 34, -23, 18, 12)
# print(max(tuple1))
# print(min(tuple1))


# 8.
# tuple1 = (90, 34, -23, 18, 12)
# list1 = list(tuple1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)


# 9.
# list1 = []
# for a in range(9):
#     if a != 0:
#         for b in range(9):
#             for c in range(9):
#                 x = a * 100 + b * 10 + c
#                 if x == a ** 3 + b ** 3 + c ** 3:
#                     list1.append(x)
# print(list1)


# 10.
# import random
#
# dict1 = {}
# list1 = []
# list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# a = 0
# while a <= 100:
#     x = random.randint(0, 100)
#     if x not in list1:
#         list1.append(x)
#         dict1[a] = x
#         a += 1
# print(dict1)  # 以上为建立随机数字典
# # 读取字典中的value,然后通过对value位数（长度）的判断写两个if，两位时将str[0]、str[1]分别判断int值，再累加对应的list[x]
# for i in range(100):
#     str1 = str(dict1[i])  # 读取value
#     if len(str1) == 2:
#         a = int(str1[0])
#         list2[a] += 1
#         b = int(str1[1])
#         list2[b] += 1  # 累加进计数list2
#     elif len(str1) == 1:
#         a = int(str1[0])
#         list2[a] += 1
#         print(key)

# 红包
# import random
#
# Sum = float(input("请输入红包总金额："))
# Num = int(input("请输入红包个数："))
#
#     else:
#         list2[0] = list2[0] + 2
#         list2[1] = list2[1] + 1
# print(list2)  # 计数list完成
# x = list2.index(max(list2))
# print(x)

# 11.
# 字典 键为书名，值为类型即可
# dict1 = {"a": "A", "b": "A", "c": "A", "d": "B", "e": "B", "f": "C", "g": "C", "h": "D", "i": "E", "j": "E"}
# str1 = input("请输入书的类型（A-E）：")
# for key, value in dict1.items():
#     if value == str1: list1 = []
# i = 1
# n = (2 * Sum / Num) * 100
# while i <= Num:
#     x = random.randint(1, n)
#     money = x * 0.01
#     least = (Num - i) * 0.01
#     if i == Num:
#         list1.append(round(Sum,2))
#         break
#     if Sum - money >= least:  # 保证剩余的钱至少够每个红包0.01
#         Sum = Sum - money
#         list1.append(round(money,2))
#         i += 1
# print(list1)


# 字典实现单链表
# 设计一个{"key1"："value1 , key0"}式的字典 是否可行
# 当用户输入为key1.next时，输出key2的值
# dict1 = {"key1": "value1,key0", "key2": "value2,key1", "key3": "value3,key2", "key4": "value4,key3"}
# str1 = input("请输入当前项：")
# if str1.find("key") != -1:
#     keys = str1.split(".")[0]  # 分离出当前项的键
#     for key, value in dict1.items():
#         if value.find(keys) != -1:  # 在值中搜寻当前项的键
#             values = value.split(",")[0]
#             print(key,":",values)


# 解析算术表达式，并计算结果
# -4*(5+6*(7-8))*9/10
# 写加减乘除的方法calculator
# 第一步，把字符串的空格删除。写循环，判断"("到最内层的括号，将所有括号的位置存入listSpace，
# 把第一步要算的括号内的字符串计算，得出结果result1，判断这个括号两侧是否有"*"、"/"，若没有，再判断+、-
#
# # 把数字分别存入list1，运算符存入list2
# import re
#
#
# def md(l, x):
#     a = l.index(x)
#     if x == '*' and l[a + 1] != '-':
#         k = float(l[a - 1]) * float(l[a + 1])
#     elif x == '/' and l[a + 1] != '-':
#         k = float(l[a - 1]) / float(l[a + 1])
#     elif x == '*' and l[a + 1] == '-':
#         k = -(float(l[a - 1]) * float(l[a + 2]))
#     elif x == '/' and l[a + 1] == '-':
#         k = -(float(l[a - 1]) / float(l[a + 2]))
#     del l[a - 1], l[a - 1], l[a - 1]
#     l.insert(a - 1, str(k))
#     return l
#
#
# def fun(s):  # 计算结果
#     l = re.findall('([\d\.]+|/|-|\+|\*)', s)
#     print(l)
#     sum = 0
#     while 1:
#         if '*' in l and '/' not in l:
#             md(l, '*')
#         elif '*' not in l and '/' in l:
#             md(l, '/')
#         elif '*' in l and '/' in l:
#             a = l.index('*')
#             b = l.index('/')
#             if a < b:
#                 md(l, '*')
#             else:
#                 md(l, '/')
#         else:
#             if l[0] == '-':
#                 l[0] = l[0] + l[1]
#                 del l[1]
#             sum += float(l[0])
#             for i in range(1, len(l), 2):
#                 if l[i] == '+' and l[i + 1] != '-':
#                     sum += float(l[i + 1])
#                 elif l[i] == '+' and l[i + 1] == '-':
#                     sum -= float(l[i + 2])
#                 elif l[i] == '-' and l[i + 1] == '-':
#                     sum += float(l[i + 2])
#                 elif l[i] == '-' and l[i + 1] != '-':
#                     sum -= float(l[i + 1])
#             break
#     return sum
#
#
# def calculator(strs):
#     ex = []
#     ans = 0
#     if '(' not in strs:
#         ans = fun(strs)  # 没有括号 直接返回结果
#         return ans
#     for i in range(len(strs)):
#         if strs[i] == '(':
#             ex.append(i)  # 把“（”的位置存入ex
#         elif strs[i] == ')':  # 14
#             sub = strs[ex[len(ex) - 1] + 1:i]  # 从此次循环所读到的）的前一个（开始输出，到此次循环的）停止，sub即为括号内的内容
#             temp = fun(sub)  # 计算括号内的结果
#             # temp=int(temp)
#             print("xxxxxx", temp)
#             strs = strs[0:ex[len(ex) - 1]] + str(temp) + strs[i + 1:len(strs) + 1]  # 将这个结果替换入原表达式，括号也被替换
#             # print("yyyyy",strs)
#             ex.pop()  # 删除此次括号记录，下次从头开始，寻找下一个紧挨着的（、）
#
#             return calculator(strs)  # 将进行过此次替换后的表达式返回，继续计算
#
# strA = '1 - 2 * ( (60-30 +(-40/5+3) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# print(1 - 2 * ((60 - 30 + (-40 / 5 + 3) * (9 - 2 * 5 / 3 + 7 / 3 * 99 / 4 * 2998 + 10 * 568 / 14)) - (-4 * 3) / (
#         16 - 3 * 2)))  # 1735397.4095238098
# strB = '3*(4+50)-((100+40)*5/2-3*2*2/4+9)*(((3+4)-4)-4)'  # 518.0
# print(3 * (4 + 50) - ((100 + 40) * 5 / 2 - 3 * 2 * 2 / 4 + 9) * (((3 + 4) - 4) - 4))
# strA = '3 + 5 - 6 * (7 + 8)'
# strB = '3 + 5 - 6 * (7 + 8)'
# print(calculator(strA))  # 1735397.4095238098
# print(calculator(strB))


# 约瑟夫环
# 用list，用下标表示人的位置，当人没有出圈时对应的值都为零，出圈后按顺序赋值，写循环令第i个出去的值为i
