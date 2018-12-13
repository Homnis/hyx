# # 1.
# def printList(list1=[]):
#     print(list1)
#
#
# list1 = [1, 2, 3, 4]
# printList(list1)


# # 2.
# def sumList(list1=[]):
#     Sum = 0
#     for i in range(len(list1)):
#         Sum = Sum + list1[i]
#     return Sum
#
#
# list1 = [1, 2, 3, 4]
# print(sumList(list1))


# #3.
# def sumList(list1=[]):
#     Sum = 0
#     for i in range(len(list1)):
#         if i%2==1:
#             Sum = Sum + list1[i]
#     return Sum
#
# list1 = [1, 2, 3, 4]
# print(sumList(list1))


# 4.
# def sumList(list1=[]):
#     Sum = 0
#     for i in range(len(list1)):
#         if i%2==0:
#             Sum = Sum + list1[i]
#     return Sum
#
# list1 = [1, 2, 3, 4]
# print(sumList(list1))


# 5.
# def Sum(a=0,b=0):
#     return a+b
#
# print(Sum(10,20))


# # 6.
# def Divide(a=0, b=1):
#     if b == 0:
#         print("something wrong happened")
#     return a / b
#
#
# print(Divide(10, 20))


# 7.
# def add1s(day=0, hour=0, minute=0, second=0):
#     seconds = day * 3600 * 60 + hour * 3600 + minute * 60 + second
#     return seconds
#
#
# print(add1s(1, 1, 1, 1))


# 8.
# def exchange(list1=[], pos1=0, pos2=1):
#     x = list1[pos1]
#     list1[pos1] = list1[pos2]
#     list1[pos2] = x
#
#
# listA = [1, 2, 3, 4]
# exchange(listA, 1, 3)
# print(listA)


# 9.
# def divide3(list1=[]):
#     count = 0
#     for i in range(len(list1)):
#         if list1[i] % 3 == 0:
#             count += 1
#     return count
#
#
# list1 = [1, 2, 3, 4, 5, 6]
# print(divide3(list1))


# 10.
# def change(num=0, char="*", length=1):
#     str1 = str(num)
#     if len(str1) > length:
#         return str1[:length]
#     elif len(str1) < length:
#         return str1.rjust(length, char)
#
#
# print(change(27, '0', 8))


# 11.
# def maxMin(list1=[], isMax=True):
#     if isMax == True:
#         return max(list1)
#     elif isMax == False:
#         return min(list1)
#
#
# list1 = [1, 2, 3, 4, 5]
# print(maxMin(list1, True))


12.
# def primeNum(num=0):
#     for i in range(2,num):
#         if i < num - 1:
#             if num % i == 0:
#                 return False
#                 break
#             elif num % i != 0:
#                 continue
#         elif i == num - 1:
#             return True
#
#
# print(primeNum(12))


# 13.
# def seconds(seconds=0):
#     days,hours,minutes=0,0,0
#     while seconds >= 0:
#         if seconds >= 216000:
#             days = seconds // 216000
#             seconds = seconds % 216000
#         elif 3600 <= seconds < 216000:
#             hours = seconds // 3600
#             seconds = seconds % 3600
#         elif 60 <= seconds < 3600:
#             minutes = seconds // 60
#             seconds = seconds % 60
#         elif seconds < 60:
#             break
#     print("%i天，%i小时,%i分钟,%i秒" %(days,hours,minutes,seconds))
#
#
# seconds(7894624)


# 14.
# import random
#
#
# def r(list1=[],num=1):
#     i = 0
#     while i < num:
#         x = random.randint(0, num)
#         if x not in list1:
#             list1.append(x)
#             i += 1
#         else:
#             continue
#
# list1=[]
# r(list1,5)
# print(list1)


# 15.
# def duiChen(list1=[]):
#     for i in range(len(list1)):
#         if list1[i] == list1[len(list1) - i - 1]:
#             if i >= len(list1) / 2:
#                 return True
#             continue
#         else:
#             return False
#
#
# list1 = [3, 1, 2, 1,]
# print(duiChen(list1))


# 16.
# def printTuple(tuple1=()):
#     for i in range(len(tuple1)):
#         print(tuple1[i], end=" ")
#
#
# tuple1 = (1, 2, 3, 4, 5)
# printTuple(tuple1)


# # 17.
# def inTuple(tuple1=(), a=0):
#     for i in range(len(tuple1)):
#         if a == tuple1[i]:
#             return i
#         else:
#             if i == len(tuple1) - 1:
#                 return -1
#
#
# tuple1 = (1, 2, 3, 4, 5)
# print(inTuple(tuple1, 3))


# 18.
# def Unti(list1=[]):
#     for i in range(len(list1)):
#         if i >= len(list1) / 2:
#             break
#         x = list1[i]
#         list1[i] = list1[len(list1) - 1 - i]
#         list1[len(list1) - 1 - i] = x
#
#
# list1 = [1, 2, 3, 4,5]
# Unti(list1)
# print(list1)


# 19.
# list1 = [1, 2, 3, 4, 5]
# print(max(list1))

# 20.
# list1 = [1, 2, 3, 4, 5]
# print(min(list1))


# 21.
# def inSert(list1=[], pos=0, str1=" "):
#     list1.insert(pos - 1, str1)
#
#
# list1 = [1, 2, 3]
# inSert(list1, 1, "a")
# print(list1)


# 22.
# def delete(list1=[], pos=0):
#     del list1[pos]
#
#
# list1 = [1, 2, 3]
# delete(list1, 1)
# print(list1)


# 23.
# import random
#
#
# def guess(ans=0, a=0):
#     num = int(input("请输入你的答案："))
#     for i in range(a):
#         if num == ans:
#             print("您的答案正确")
#             print("你一共猜了%i次" % (i + 1))
#             break
#         elif num > ans:
#             num = int(input("大了，继续猜："))
#         elif num < ans:
#             num = int(input("小了，继续猜："))
#
#
# ans = random.randint(0, 100)
# guess(ans, 5)
# print("答案为：", ans)
