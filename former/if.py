##猜拳
# import random
# userHand=int(input("0代表石头，1代表剪刀，2代表布："))
# comHand=random.randint(0,2)
# if comHand==userHand:
#    print("平局")
# elif comHand==0:
#	print ("电脑出了石头")
#    if userHand==0:
#        print("平局")
#    if userHand==1:
#        print("你输了")
#    if userHand==2:
#        print("你赢了")
# elif comHand==1:
#	print ("电脑出了剪刀")
#    if userHand==1:
#        print("平局")
#    if userHand==2:
#        print("你输了")
#    if userHand==0:
#        print("你赢了")
# elif comHand==2:
#	print ("电脑出了布")
#    if userHand==2:
#        print("平局")
#    if userHand==0:
#        print("你输了")
#    if userHand==1:
#        print("你赢了")


##1
# month=int(input("请输入月份："))
# if month in (3,4):
#    print("春季")
# elif month in (5,6,7,8):
#    print("夏季")
# elif month in (9，10):
#    print("秋季")
# elif month in (11，12，1，2):
#    print("冬季")


##2
# cnGrade=int(input("请输入小强的语文成绩："))
# mtGrade=int(input("请输入小强的数学成绩："))
# enGrade=int(input("请输入小强的英语成绩："))
# if cnGrade>85 and mtGrade>85 and enGrade>85 :
#    print("a","true")
# else:
#    print("a","false")
# if cnGrade>95 or mtGrade>95 or enGrade>95:
#    print("b","true")
# else:
#    print("b","false")
# if cnGrade>90 or enGrade>90 and mtGrade>80:
#    print("b","true")
# else:
#    print("b","false")


##3,计算器
# a=float(input("请输入一个数字:"))
# b=float(input("请输入一个数字:"))
# c=input("请输入要进行的运算:")
# if c=="+" :
#    print("%s + %s = %0.2f"  %(a,b,a+b))
# if c=="-" :
#    print("%s - %s = %0.2f"  %(a,b,a-b))
# if c=="*" :
#    print("%s * %s = %0.2f"  %(a,b,a*b))
# if c=="/" :
#    print("%s / %s = %0.2f"  %(a,b,a/b))


##4. 比大小
# a=float(input("请输入一个数字:"))
# b=float(input("请输入一个数字:"))
# if a>=b :
#    print(a)
# if a>b :
#    print(b)


##5. 判断字符串长度
# a=input("请输入字符串:")
# if len(a)<=56 :
#    print("短消息")
# elif len(a)>56 and len(a)<=128:
#    print("一般消息")
# elif len(a)>128 and len(a)<=192:
#    print("长消息")
# elif len(a)>193 and len(a)<=256:
#    print("超长消息")
# else:
#    print("长度超过可发送上限")


##6
# import random
# a=None
# while a!="n" :
#    n=random.randint(0,5)
#    a=input("继续进行请输入y，停止请输入n:")
#    if a=="n" :
#         break
#    if n==0 :
#         print("进入战斗")
#    elif n==1 :
#         print("捡到宝箱")
#    elif n==2 :
#         print("捡到武器")
#    elif n==3 :
#         print("捡到弹药")
#    elif n==4 :
#         print("踩到陷阱")
#    elif n==5 :
#         print("无事件")


##7.
# a=None
# while a!="y" :
#    a=input("这道题你会做了吗，会了输入y,否则输入n:")
#    if a=="y" :
#         break


##8.
# year=int(input("请输入年龄:"))
# if year <10 :
#    print("不允许查看")
# elif year >=18 :
#    print("允许查看")
# elif year <18 and year >=10 :
#    a=input("是否继续查看（请输入yes 或 no）")
#    if a=="yes" :
#        print("请查看")
#    else :
#        print("退出，您放弃查看")


##9.
# Higher=int(input("请输入高压:"))
# Lower=int(input("请输入低压:"))
# if Higher>=90 and Higher<=140 :
#     if Lower>=60 and Lower<=90 :
#          print("正常")
#     else  :
#          print("不正常")
# else  :
#     print("不正常")


##10.
# a=int(input("请输入购买T恤的件数:"))
# b=int(input("请输入购买裤子的件数:"))
# priceA=0
# priceB=0
# if a==1 :
#    priceA=35
# elif a==2:
#    priceA=35*0.9
# elif a>=3:
#    priceA=35*0.8
# if b==1 :
#    priceB=120
# elif b>=2:
#    priceB=120*0.9
# print("小明应该付%0.1f 元钱" %(priceA*a+priceB*b))
