# -*-coding:utf-8-*-
# #四舍五入
# a=123.5678
# a1=a*100
# b1=int(a1+0.5)
# ending=b1/100
# print("ending",ending)
#
# 任务一
# print("Hello Python")
#
# #任务二
# name="abc"
# level=20
# exp=500
# hp=500.0
# mp=500.00
# print(type(mp))
#
#
# #任务3
# place=input("请输入您的籍贯：")
# print("欢迎您来到%s"%(place))
#
#
# #任务4
# a=int(input("请输入：") )
# b=int(input("请输入：") )
# c=int(input("请输入：") )
# d=int(input("请输入：") )
# print(a*b*c*d)
#
#
# #任务5
# name=input("请输入姓名：")
# a=int(input("请输入语文成绩：") )
# b=int(input("请输入数学成绩：") )
# c=int(input("请输入英语成绩：") )
# d=(a+b+c)/3
# print("%s，你的总成绩为%0.1f分,平均成绩为%0.2f分"%(name,a+b+c,d))
#
#
# #任务6
# a=int(input("请输入上底：") )
# b=int(input("请输入下底：") )
# c=int(input("请输入高：") )
# d=(a+b)*c/2
# print("该梯形的面积是：",d)
#
#
# #任务7
# day=int(input("请输入天数：") )
# print("该日期是第%0.0f周,第%0.0f天" %(day/7+1,day%7))
#
#
# 任务8
# #临时变量
# a=int(input("请输入第一个数：") )
# b=int(input("请输入第二个数：") )
# c=a a=b b=c
# print(a,b)
#
#
# #异或法
# a = int(input("请输入第一个数："))
# b = int(input("请输入第二个数："))
# a = a ^ b
# b = a ^ b   # b=(a^b)^b=a
# a = a ^ b   # a=(a^b)^a=b
# print(a, b)
#
#
# #求和法
# a=int(input("请输入第一个数：") )
# b=int(input("请输入第二个数：") )
# a=a+b
# b=a-b
# a=a-b
# print(a,b)
#
#
# #任务10
# #整数abc，除以10取余为个位c，除以100取整为百位a，x-a*100-c=b
# num=int(input("please input a number:"))
# c=num%10
# a=num//100
# b=num-a*100-c
# print("%i%i%i" %(c,b/10,a))
#
#
