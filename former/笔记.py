# def createGenerator() :
#     mylist = range(3)
#     for i in mylist :
#         yield i*i
#
# mygenerator = createGenerator() # create a generator
# print(mygenerator) # mygenerator is an object!
# for i in mygenerator:
#     print(i)

# 选择排序练一遍
# 把最小的放在第一位，以位置为标准，挨个排列。
# list1 = [1, 3, 7, 4, 2, 5]
# for i in range(len(list1)):
#     for n in range(len(list1)):
#         if i + n < len(list1):
#             if list1[i] <= list1[i + n]:  # 从小至大排序
#                 continue
#             else:  # 交换位置
#                 Min = list1[i + n]
#                 list1[i + n] = list1[i]
#                 list1[i] = Min
#         print(list1)
# print(list1)

#
# 冒泡练一遍
# list1 = [1, 3, 7, 4, 2, 5]
# for i in range(len(list1)):
#     for n in range(len(list1)-1):
#         if list1[n] > list1[n + 1]:  # 从小至大排序
#             Max = list1[n]
#             list1[n]=list1[n+1]
#             list1[n+1]=Max
# print(list1)

# 输入算术表达式，进行计算
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


# import re
#
# line = "Cats are smarter You are dogs "
#
# matchObj = re.match(r'(.*?) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
#     # print("matchObj.group(3) : ", matchObj.group(3))
#     # print("matchObj.group(4) : ", matchObj.group(4))
# else:
#     print("No match!!")
#
# str1="QQQ"
# num="###"
# format="%s%d"%(str1,num)
# print(format)
