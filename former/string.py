# #1.
# str1=input("请输入字符串")
# print(str1.replace(" ",""))

#2.
# 方法一
# str1 = input("请输入路径：")
# tuple1 = str1.rpartition("\\")
# tuple2 = tuple1[2].rpartition(".")
# print("文件路径为：%s ， 文件名为： %s ，后缀为： .%s" % (tuple1[0], tuple2[0], tuple2[2]))

# 方法二
# str1 = input("请输入路径：")
# x = str1.rindex(".")
# print(str1[x:len(str1)])
# y = str1.rindex("\\")
# print(str1[y+1:x])
# print(str1[:y+1])

#
#
#
# #3.  UTF-8编码中汉字为三个字节，故可以用字符串长度与字节数之差求出汉字个数
# a=input(" input.....")
# x=a.encode()   #字节化
# print((len(x)-len(a))/2)
#
#
# 4.
# str1=input("请输入：")
# x=str1.encode("utf-8")
# print ("加密后：",x)
# y=x.decode("utf-8")
# print ("解密后：",y)
#
#
# #5.
# str1=input(" input.....")
# strA=str1.upper()
# strB=str1.lower()
# print("全部转换为大写：",strA)
# print("全部转换为小写：",strB)
#
#
# #6.
# 方法一 循环过多
# str1 = input("请输入字符串：")
# n=0
# tuple1=str1.split('.')
# while n<len(tuple1) :
# 	if tuple1[n].isalnum()==1 :
# 		print(tuple1[n])
# 	else :
# 		tuple2=tuple1[n].split(',')
# 		a=0
# 		while a<len(tuple2):
# 			if tuple2[a].isalnum()==1 :
# 				print(tuple2[a])
# 			else:
# 				tuple3=tuple2[a].split(';')
# 				b=0
# 				while b<len(tuple3) :
# 					print(tuple3[b])
# 					b=b+1
# 			a=a+1
# 	n=n+1

# 方法二
# str1 = input("请输入字符串：")
# list1 =[',','.',';','，','。','；','!','?','、','？']
# list2 =[]
# for a in range(len(str1)) :
#     if str1[a] in list1 :
#         list2.append(a)
# for n in range(len(list2)) :
#     b=int(list2[n])
#     if n==0 :
#         print(str1[n:b])
#         beg=b
#     else :
#         print(str1[beg+1:b])
#         beg=b
# print(str1[b+1:])

#
# 7.
# list1=["abcde bcd","123  45 1","a 1 2b"]
# for i in range(len(list1)):
#     list1[i]=list1[i].replace(" ","")
# print (list1)
#
#
# #8.
# bookName=input("请输入书名：")
# print(len(bookName))
#
#
# #9.
# game1=input("请输入游戏名：")
# game2=input("请输入游戏名：")
# if game1==game2 :
# 	print(game1)
# else :
# 	print(game1)
# 	print(game2)
#
#
# #10.
# game1=input("请输入游戏名：")
# game2=input("请输入游戏名：")
# if game1==game2 or game1.upper()==game2.upper():
# 	print(game1)
# else :
# 	print(game1)
# 	print(game2)
#
#
#11.
# date1=input("请输入日期（格式为2008/08/08）：")
# tuple1=date1.split('/')
# print("日期为：%s年-%s月-%s日" %(tuple1[0],tuple1[1].replace("0",""),tuple1[2].replace("0","")))
#
#
# 12.
# str1=input("请输入字符串：")
# list1=list(str1)
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

#
#
#
# #13.
# str1=input("请输入英文：")
# tuple1=str1.split(" ")
# num=0
# list1=list(tuple1)
# while num<len(tuple1)//2 :
# 	a=tuple1[num]
# 	list1[num]=list1[len(tuple1)-1]   #反序
# 	list1[len(tuple1)-1]=a
# 	num=num+1
# print (list1)
#
#
# #14.
# str1="http://www.163.com?userName=admin&pwd=123456"
# tuple1=str1.partition("userName=")
# str2=tuple1[2]
# tuple2=str2.partition("&pwd=")
# userName=tuple2[0]
# psw=tuple2[2]
# print("userName=%s ,psw=%s" %(userName,psw))
#
#
# #15.
# list1=["aaa","bbb","ccc","ddd","a","b","c","d","aabbccddee","aaaaabbbbbccccc"]
# list2=["1","2","3","4","5","6","7","8","9","10"]  #作者
# for n in range(len(list1)):
# 	if len(list1[n])>=10 :
# 		str1=list1[n]
# 		print(str1[0:8],"... | %s" %(list2[n]))
# 	else :
# 		print(list1[n],"... | %s" %(list2[n]))
# 	n=n+1
#
#
# #16.
# str1=input("请输入一句话：")
# i,n=0,-1
# while i<=len(str1):
#     n=str1.find("呵",n+1)
#     i+=1
#     if n==-1 :
#         break
#     else :
#         print(n)
#
#
# #17.
# str1=input("请输入一句话：")
# i,n=0,-1
# while i<=len(str1):
#     n=str1.find("呵呵",n+1)
#     i+=1
#     if n==-1 :
#         break
#     else :
#         print(n)
#
#
# #18.
# str1=input("请输入一句话：")
# print(str1.replace("邪恶","**"))
#
#
# 19.
# str1=input("请输入一句话：")
# str2=input("请输入一句话：")
# if len(str1)>=len(str2) :
# 	if str1.find(str2)==-1 :
# 		print("不是子集")
# 	else :
# 		print("是子集")
# if len(str1)<len(str2) :
# 	if str2.find(str1)==-1 :
# 		print("不是子集")
# 	else :
# 		print("是子集")
#
#
# #20.
# str1=input("请输入一句话：")
# str2=input("请输入一句话：")
# Sum,n=0,0
# if len(str1)>=len(str2) :
# 	while n<len(str2) :
# 		if str1.find(str2[n])==-1 :
# 			print (str2[n],"未出现过")
# 			Sum=Sum+1
# 			break
# 		else :
# 			n=n+1
# 			continue
# 	if Sum==0 :
# 		print("%s 的所有字符都出现过" %(str2))
# if len(str1)<len(str2) :
# 	while n<len(str1) :
# 		if str2.find(str1[n])==-1 :
# 			print (str1[n],"未出现过")
# 			Sum=Sum+1
# 			break
# 		else :
# 			n=n+1
# 			continue
# 	if Sum==0 :
# 		print("%s 的所有字符都出现过" %(str1))
#
#
#
# 21.
# 也可以每产生一个随机数，就用字符串判断语句判断其是否为字母，返回true就
# 输出，false就continue
# import random
# n=int(input("请输入字符串长度："))
# seed="abcdefdhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# a=0
# list1=[]
# while a<n :
# 	list1.append(random.choice(seed))
# 	a=a+1
# print (list1)
#
#
# 22.
# 也可以每产生一个随机数，就用字符串判断语句判断其是否为字母和数字
# ，返回true就输出，false就continue
# import random
# n=int(input("请输入字符串长度："))
# seed="0123456789abcdefdhijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# a=0
# list1=[]
# while a<n :
# 	list1.append(random.choice(seed))
# 	a=a+1
# print (list1)
#
#
# 23.
# str1=input("请输入一个字符串：")
# list1=list(str1)
# print(str1.isalnum())
# x,y,n=0,0,0
# while n<len(str1) :
# 	if list1[n].isalpha() :
# 		x=1
# 	elif list1[n].isdigit() :
# 		y=1
# 	n=n+1
# if x==1 and y==1 :
# 	print("既有数字又有字母")
# elif x==1 and y!=1 :
# 	print ("只有字母没有数字")
# elif x!=1 and y==1 :
# 	print ("只有数字没有字母")

#
# 24.
# 方法一
# str1=input("请输入一个字符串：")
# listA=list(str1)
# listA.sort(key=lambda x:x.upper())
# print(listA)

# 方法二
# 通过大写比较，交换原字符位置
# str1=input("请输入一个字符串：")
# list1=list(str1)
# n=0
# while n<len(str1) :
# 	a=0
# 	while a<len(str1)-1 :
# 		strA=list1[a]
# 		strB=list1[a+1]
# 		if strA.upper()>strB.upper() :
# 			Max=list1[a]
# 			list1[a]=list1[a+1]
# 			list1[a+1]=Max
# 		a=a+1
# 	n=n+1
# print (list1)
#
#
# #25.
# str1=input("请输入一个字符串：")
# print(str1.zfill(5))

# x=str1.rjust(3,"0")
# print(x)

