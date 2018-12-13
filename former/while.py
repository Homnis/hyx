# #1.
# cnGrade=int(input("请输入语文成绩："))
# mtGrade=int(input("请输入数学成绩："))
# if cnGrade>90 and mtGrade>90 :
# 	print("true")
# else :
# 	print("false")
# if cnGrade>90 or mtGrade>90 :
# 	print("true")
# else :
# 	print("false")
#
#
# #2.
# a=int(input("请输入a："))
# b=int(input("请输入b："))
# if a%b==0 or a+b>100 :
# 	print(a)
# else :
# 	print(b)
#
#
# #3.
# grade=int(input("请输入成绩："))
# if grade >=90 :
# 	print("A")
# elif 90>grade>=80 :
# 	print("B")
# elif 80>grade>=70 :
# 	print("C")
# elif 70>grade>=60 :
# 	print("D")
# elif grade<60:
# 	print("E")
#
# #4.
# userName=input("请输入用户名：")
# psw=input("请输入密码：")
# if userName=="admin" and psw=="88888" :
# 	print("正确")
# elif userName!="admin" :
# 	print("用户名不存在")
# elif userName=="admin" :
# 	print("密码错误")
#
#
#
# #5.
# a=1
# while a<=3 :
# 	userName=input("请输入用户名：")
# 	psw=input("请输入密码：")
# 	if a==3 :
# 		print("您的账户已被冻结")
# 		break
# 	if userName=="admin" and psw=="88888" :
# 		print("正确")
# 		break
# 	else :
# 		print("用户名或密码错误")
# 		a=a+1
#
#
# #6.
# a=0
# Sum=0
# while a<100 :
# 	a=a+1
# 	if a%2==1 :
# 		Sum=Sum+a
# 	else :
# 		continue
# print(Sum)
#
#
# #7.
# a=0
# Sum=0
# while a<100 :
# 	a=a+1
# 	if a%3==0 :
# 		Sum=Sum+a
# 	else :
# 		continue
# print(Sum)
#
#
# #8.
# n=int(input("请输入行数: "))
# a=1
# while a<=n :
# 	b=1
# 	Len=2*a-1
# 	while b<=Len:
# 		print("*",end="")
# 		b=b+1
# 	a=a+1
# 	print()
#
#
# #9.
# n=int(input("请输入行数: "))
# a=1
# while a<=n :
# 	b=n
# 	while b>=a:
# 		print("*",end="")
# 		b=b-1
# 	a=a+1
# 	print()
#
#
# #10.
# n = int(input("请输入行数: "))
# a = 1
# while a <= n:
# 	b=1
# 	Len=2*a-1
# 	while b<=Len:
# 		if b==1 :
# 			print(" "*(n-a) ,end="")
# 		print("*",end="")
# 		b=b+1
# 	a=a+1
# 	print()
#
#
# #11.
# n=int(input("请输入行数: "))
# a=0
# while a<n//2 :
# 	b=1
# 	Len=2*a+1
# 	while b<=Len:
# 		if b==1 :
# 			print(" "*(n-a-1) ,end="")
# 		print("*",end="")
# 		b=b+1
# 	a=a+1   #a=3
# 	print()
# while a<n :
# 	b=1
# 	Len=2*(n-a-1)+1
# 	while b<=Len :
# 		if b==1 :
# 			print(" "*a ,end="")
# 		print("*",end="")
# 		b=b+1
# 	a=a+1
# 	print()
#
#
# #12.
# chi=1
# rab=None
# while chi<=35 :
# 	rab=35-chi
# 	if chi*2+rab*4!=94 :
# 		chi=chi+1
# 	else :
# 		print ("鸡有%i只" %chi)
# 		print ("兔有%i只" %rab)
# 		break
#
#
# #13.
# import random
# money=int(input("请购买筹码: "))
# while money>=50 :
# 	bet=int(input("请选择下注数量（不小于50）: "))
# 	if bet<50 :
# 		print("下注金额过小！")
# 		continue
# 	a=input("请选择大小:（1为大，0为小） ")
# 	num=random.randint(1,6)
# 	if a=="1" :
# 		if num>=4 and num<=6 :
# 			money=money+bet
# 		elif num>=1 and num<=3:
# 			money=money-bet
# 	else :
# 		if num>=4 and num<=6 :
# 			money=money-bet
# 		elif num>=1 and num<=3:
# 			money=money+bet
# 	print ("当前还有",money)
# 	E=input("是否退出(y/n):")
# 	if E=="y" :
# 		break