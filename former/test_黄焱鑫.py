import time
import json
import pickle
import os
import random

# 1、求100以内跨度最大的相邻的一对质数。
# def primeNum(num):
#     list1 = []
#     for i in range(num):
#         x = 0
#         for n in range(1, i):  # 用来判断i是否是质数
#             if i > 1:
#                 if n == i - 1:  # x=1说明是质数
#                     x = 1
#                 elif n > 1:
#                     if i % n == 0:  # i能被n整除
#                         break
#         if x == 1:
#             list1.append(i)
#     return list1
#
#
# def test1():
#     list1 = primeNum(100)
#     list2 = []
#     for i in range(len(list1) - 1):
#         x = list1[i + 1] - list1[i]
#         list2.append(x)
#     Max = list2[0]
#     n = 0
#     for i in range(len(list2)):
#         if list2[i] >= Max:
#             Max = list2[i]
#             n = i
#     print(list1[n], list1[n + 1])
#
#
# test1()


# 2、有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...  编写方法，求出这个数列的前20项之和。(6分)

# def mkList(num):
#     list1 = [1, 2]
#     for i in range(2, num):
#         x = list1[i - 2] + list1[i - 1]
#         list1.append(x)
#     return list1
#
#
# def test2():
#     list1 = mkList(20)
#     list2 = mkList(21)
#     list2.pop(0)
#     Sum = 0
#     for i in range(len(list1)):
#         x = list2[i] / list1[i]
#         Sum += x
#     print(Sum)
#
#
# test2()
# 3、编写方法求区间（n-m）内个位数字不是1,4,5，并且可以被3整除的所有数,并将所有数字放入合适集合中。(6分)
#
# def Num1(n, m):
#     list1 = []
#     for i in range(n, m + 1):
#         if i % 10 != 1 and i % 10 != 4 and i % 10 != 5 and i%3==0:
#             list1.append(i)
#     return list1
#
#
# def test3(n,m):
#     print(Num1(n,m))
#
# test3(0,20)
# 4、编写方法，传入字符列表，该方法将小写字母变大写，将大写字母变小写,比如[‘a’,’B’,’c’]=》[‘A’,’b’,’C’](6分)
# def change(str):
#     list1=[]
#     for i in range(len(str)):
#         if str[i].isupper()==True:
#             list1.append(str[i].lower())
#         elif str[i].islower()==True:
#             list1.append(str[i].upper())
#     return list1
#
# def test4(str1):
#     print("".join(change(str1)))
#
# test4("abcDEf")
# 5、输入一个日期，格式如：2010 10 24 ，打印输出为【2010年10月24日】，并输出这一天是这一年中的第几天，是星期几,和今天相差多少小时？。
# def test5():
#     myTime=input("请输入时间》（2010 10 24）")
#     x=time.strptime(myTime,"%Y %m %d")
#     print("%s年%s月%s日"%(x[0],x[1],x[2]))
#     print("这一天是这一年的第%s天,星期%s"%(x[7],x[6]))
#
# test5()
# 6、编写方法，接收参数n，当(n=4)显示如下图形
# n值由用户键盘输入(6分)
#
# 1
# 1  2
# 3  5  8
# 13 21 34 55

# def mkList(num):
#     list1 = [1, 1]
#     for i in range(2, num):
#         x = list1[i - 2] + list1[i - 1]
#         list1.append(x)
#     return list1
#
#
# def Show(n):
#     Sum = 0
#     for i in range(n + 1):
#         Sum += i
#     list1 = mkList(Sum)
#     print(list1)
#     x = 0
#     for i in range(1,n + 1):#i代表行数,x代表输出的第几个
#         for x in range(i):
#             a=list1[0]
#             print(a,end=" ")
#             list1.pop(0)
#             # print(list1)
#         print()
#
# def test6():
#     Show(5)
#
# test6()

# 7、编写方法，传入用户自定义的名字，若名字长度为2-7个且均为汉字返回true，反之返回false。(6分)
# def name(str):
#     if 7>=len(str)>=2 :
#         a=str.encode()
#         if len(a) == len(str)*3 :
#             return True
#         else:
#             return False
#     else:
#         return False
# def test7():
#     print(name("会哦未"))
# test7()

# 8、实现账号注册和账号登陆，需要使用json文件存储数据。账号属性为：名字，年龄，性别，邮箱，地址，密码
# def reg(age, gender, email, address, name="", psw=""):
#     dictReg = {name: [psw, age, gender, email, address]}
#     path = "reg.txt"
#     open(path, "a")
#     with open(path, "r") as isNone:  # 判断是否为空，不为空的话重新建立字典，代替原有的
#         if isNone.read() != "":
#             with open(path,"r") as f_r:
#                 y=json.load(f_r)
#         elif isNone.read() == "":
#             y = b''
#     if y != b'':
#         if y.get(name) == None:
#             y[name] = [psw, age, gender, email, address]
#             with open("reg.txt", "w") as cover:
#                 json.dump(y, cover)
#                 print("注册成功")
#         else:
#             print("已存在")
#     else:
#         with open("reg.txt", "w") as userReg:
#             json.dump(dictReg, userReg)
#             print("注册成功")
#
#
# def load(name="", psw=""):
#     path = "reg.txt"
#     open(path, "a")
#     with open(path, "r") as f_r:
#         if f_r.read() == "":
#             print("无注册信息")
#         else:
#             with open(path,"r") as f_r1:
#                 y=json.load(f_r1)
#     if y.get(name)!=None:
#         list1=y[name]
#         if psw==list1[0]:
#             return True
#         else:
#             return False
#     else:
#         return False
#
# def test8():
#     reg(10, "gender", "email", "add", "d", "123")
#     a=load("a","123")
#     print(a)
#
# test8()

# 9、有n盏灯,放在一排,从1到n依次顺序编号.有m个人也从1到m依次顺序编号.第1个人（1号）将灯全部关闭；
# 第2个人（2号）将凡是2的倍数的灯打开；第3个人（3号）将凡是3的倍数的灯作相反处理（该灯如是打开的,则将它关闭；
# 如是关闭的,则将它打开）.以后的人都和3号一样,将凡是自己编号倍数的灯作相反处理.试计算当第m个人操作后,哪几盏灯是亮的?
# def deng(n):
#     list1 = []
#     for i in range(n):
#         list1.append(True)
#     return list1
#
# def Trun(m, list1):
#     for i in range(m + 1):  # i代表第几个人
#         if i > 0:
#             for n in range(len(list1)):  # n代表第几个灯
#                 if (n+1) % i == 0:
#                     if list1[n] == True:
#                         list1[n] = False
#                     elif list1[n] == False:
#                         list1[n] = True
#     return list1
# #
#
# print(Trun(7, deng(3)))
#
# 第二部分：综合题目（40分）
# 10编写武器类，
# a)	字段:名称、攻击力、重量。字段皆为私有变量
# b)	为该类编写三个构造函数，用于初始化
# c)	为该类每个字段添加属性，对字段进行封装
# d)	为该类添加方法WeaponInfo,显示武器的所有信息，格式如下：
# 1.	宝剑的攻击力为 100，重量为1000 g
# 2.	手枪的攻击力为 500，重量为600 g
# e)	实例化5个武器，并依次执行WeaponInfo方法
# class weapon:
#     def __init__(self,name,attack,height):
#         self.Name=name
#         self.Attack=attack
#         self.Height=height
#     @property
#     def Name(self):
#         return self.__name
#     @Name.setter
#     def Name(self,name):
#         self.__name=name
#     @property
#     def Attack(self):
#         return self.__attack
#     @Attack.setter
#     def Attack(self,attack):
#         self.__attack=attack
#     @property
#     def Height(self):
#         return self.__height
#     @Height.setter
#     def Height(self,height):
#         self.__height=height
#     def WeaponInfo(self):
#         print("%s的攻击力为：%i,重量为：%i g"%(self.Name,self.Attack,self.Height))
#
# def test10():
#     a=weapon("剑1",100,1000)
#     a.WeaponInfo()
#     b=weapon("剑2",200,1100)
#     b.WeaponInfo()
#     c=weapon("剑3",300,1200)
#     c.WeaponInfo()
#     d=weapon("剑4",400,1300)
#     d.WeaponInfo()
#     e=weapon("剑5",500,1400)
#     e.WeaponInfo()
#
# test10()

# 11、写一个Cube类:
# 字段：x,y,z坐标，缩放比例 scaleX，scaleY，scaleZ
# 字段为公共的访问控制
# 要求：
# 11-1.创建不同位置、不同缩放比例的Cube，创建5个并放入合适的集合（列表及其他数据结构均可）中。
# 11-2.为11-1创建的集合完成如下排序策略：
# 1.按照位置排序；
# 2.按照缩放比例排序。
# 请在主类中测试上面的要求.
# class Cube:
#     def __init__(self, x, y, z, scaleX, scaleY, scaleZ):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.scaleX = scaleX
#         self.scaleY = scaleY
#         self.scaleZ = scaleZ
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         self.__x = x
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, y):
#         self.__y = y
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, z):
#         self.__z = z
#
#
# class Main:
#     a = Cube(1, 1, 1, 2, 2, 2)
#     b = Cube(10, 10, 10, 4, 4, 4)
#     c = Cube(100, 100, 100, 1, 1, 1)
#     d = Cube(30, 30, 30, 3, 3, 3)
#     e = Cube(50, 50, 50, 2, 2, 2)
#     list1 = [a, b, c, d, e]
#     list1.sort(key=lambda x: x.x)
#     print(list1[2].x)
#     list1.sort(key=lambda x: x.scaleX)
#     print(list1[2].scaleX)
#
# Main()
# 12、有一个类：门铃报警器（DoorBellAlarm）
# 类里有一个方法：WelcomeAlarm() 用于向刚进门的客人致欢迎词。
# 编写中国银行、工商银行、交通银行、建设银行这四个类，这四个类均继承自银行类，都实现了门铃报警器接口。
# 编写一个方法实现只要传入一个银行对象，报警器就会自适应的报出：XXX银行欢迎您的到来！
# class DoorBellAlarm:
#     def __init__(self):
#         pass
#     def WelcomeAlarm(self):
#         pass
# class cnBank(DoorBellAlarm):
#
#     def __init__(self):
#         super().__init__()
#
#     def WelcomeAlarm(self):
#         print("中国银行欢迎您的到来")
# class gsBank(DoorBellAlarm):
#
#     def __init__(self):
#         super().__init__()
#
#     def WelcomeAlarm(self):
#         print("工商银行欢迎您的到来")
# class jtBank(DoorBellAlarm):
#
#     def __init__(self):
#         super().__init__()
#
#     def WelcomeAlarm(self):
#         print("交通银行欢迎您的到来")
# class jsBank(DoorBellAlarm):
#
#     def __init__(self):
#         super().__init__()
#
#     def WelcomeAlarm(self):
#         print("建设银行欢迎您的到来")
# def sing(self):
#     self.WelcomeAlarm()
# def Main():
#     a=cnBank()
#     sing(a)
# Main()
# 13、写一个学生类， 设计 6 个字段用于表示学生的信息（学号、班级、名字、语文成绩、数学成绩、英语成绩）；
# 然后定义一个集合存储一个班的学生（3人），请依次输入每个学生的成绩，输入完成后，根据学生的 3 门功课的成绩进行降序排列。
# 优先次序：数学 语文 英语
# 例：名字 语文成绩 数学成绩 英语成绩
# 王一  87  76  65
# 王二  88  76  67
# 王三  87  76  68
# 排完：
# 王二  88  76  67
# 王三  87  76  68
# 王一  87  76  65
# class student:
#     def __init__(self, sno, cno, name, cnGrade, mathGrade, enGrade):
#         self.sno = sno
#         self.name = name
#         self.cno = cno
#         self.cnGrade = cnGrade
#         self.mathGrade = mathGrade
#         self.enGrade = enGrade
#
#     def __str__(self):
#         return "%s, %i,%i,%i" % (self.name, self.cnGrade, self.mathGrade, self.enGrade)
#
#
# def printObList(list1):
#     for i in range(len(list1)):
#         print(list1[i])
#
# def test13():
#     a = student("1001", "3", "王一", 87, 76, 65)
#     b = student("1002", "3", "王二", 90, 70, 67)
#     c = student("1003", "3", "王三", 89, 76, 68)
#     d = student("1004", "4", "王四", 87, 76, 68)
#     list1 = [a, b, c,d]
#     list1.sort(key=lambda x: x.mathGrade, reverse=True)
#     for i in range(len(list1) - 1):
#         if list1[i].mathGrade == list1[i + 1].mathGrade:  # 把相同的值取出
#             math = list1[i].mathGrade
#             list2 = []
#             listDown = []
#             for i in range(len(list1)):  # 把所有含有相同取出值的项取出，建立一个新列表，并建立一个listDown列表存储其下标
#                 if list1[i].mathGrade == math:
#                     list2.append(list1[i])
#                     listDown.append(i)
#             list2.sort(key=lambda x: x.cnGrade, reverse=True)  # 在新列表list2中对数学相同的对象以语文排列
#             for i in range(len(list2) - 1):  # 对list2进行相同处理，即类似的重写一遍主循环
#                 if list2[i].cnGrade == list2[i + 1].cnGrade:
#                     cn = list2[i].cnGrade
#                     list3 = []
#                     listDown1 = []
#                     for i in range(len(list2)):
#                         if list2[i].cnGrade == cn:
#                             list3.append(list2[i])
#                             listDown1.append(i)
#                     list3.sort(key=lambda x: x.enGrade, reverse=True)
#                     for i in range(len(listDown1)):  # 根据下标列表的长度写循环，把list2中的值改写成list3中排列后的结果
#                         list2[listDown1[i]] = list3[i]
#                         list2[listDown1[i]] = list3[i]
#             for i in range(len(listDown)):  # 根据下标列表的长度写循环，把list1中的值改写成list2中排列后的结果
#                 list1[listDown[i]] = list2[i]
#                 list1[listDown[i]] = list2[i]
#     printObList(list1)
#
# test13()


# 14、编写小游戏
# a)游戏中有一个玩家和3个AI（机器人）
# b)玩家和每个机器人都有自己的生命值和攻击力；
# c)玩家默认生命值600，机器人默认生命值为100；
# d)玩家攻击力15，敌人攻击力为5；
# e)游戏采用轮询方式；
# f)每轮会一枚骰子，点数（1~6）；
# g)所有参与者（玩家和每个AI）依次猜大小，无论是玩家还是机器人只要猜对就可以发动攻击
# i.如果猜大，4~6是赢，1~3是输
# ii.如果猜小，1~3是赢，4~6是输
# h)只要玩家才对，那么玩家永远先手；如果猜不对，则才对的机器人按顺序执行；
# i)战斗结束有以下几种情况：
# i.玩家死亡
# ii.敌人全部死亡
# j)显示每一轮猜数的结果和答案，并显示每一轮过后玩家和AI的信息，显示最后的胜利是机器人一方还是玩家一方。

# class any:
#     def __init__(self, hp, attack):
#         self.hp = hp
#         self.attack = attack
#
#     def Attack(self, p):
#         p.hp -= self.attack
#
#     def guess(self, num, guess):
#         if guess == "大":
#             if 6 >= num >= 4:
#                 return True
#             else:
#                 return False
#         elif guess == "小":
#             if 3 >= num >= 1:
#                 return True
#             else:
#                 return False
#
#
# class player(any):
#     def death(self):
#         print("玩家死亡")
#
#
# class robot(any):
#     def death(self):
#         print("机器人死亡")
#
#
# def num():
#     a = random.randint(1, 6)
#     return a
#
#
# def Guess(playerA, robotA, robotB, robotC):
#     ranNum = num()
#     x = input("大还是小：")
#     pGuess = None
#     if x == "大":
#         pGuess = playerA.guess(ranNum, "大")
#     elif x == "小":
#         pGuess = playerA.guess(ranNum, "小")
#     if pGuess == True:
#         a = input("请输入要攻击的对象:(A B or C)")
#         if a == "A":
#             playerA.Attack(robotA)
#         elif a == "B":
#             playerA.Attack(robotB)
#         elif a == "C":
#             playerA.Attack(robotC)
#         else:
#             print("输入有误")
#         rGuess = None
#         print("robotA:")
#         x = input("大还是小：")
#         if x == "大":
#             rGuess = robotA.guess(ranNum, "大")
#         elif x == "小":
#             rGuess = robotA.guess(ranNum, "小")
#         if rGuess == True:
#             robotA.Attack(playerA)
#         rGuess = None
#         print("robotB:")
#         x = input("大还是小：")
#         if x == "大":
#             rGuess = robotB.guess(ranNum, "大")
#         elif x == "小":
#             rGuess = robotB.guess(ranNum, "小")
#         if rGuess == True:
#             robotB.Attack(playerA)
#         rGuess = None
#         print("robotC:")
#         x = input("大还是小：")
#         if x == "大":
#             rGuess = robotC.guess(ranNum, "大")
#         elif x == "小":
#             rGuess = robotC.guess(ranNum, "小")
#         if rGuess == True:
#             robotC.Attack(playerA)
#     if pGuess == False:
#         rGuess = None
#         print("robotA:")
#         x = input("大还是小：")
#         if x == "大":
#             rGuess = robotA.guess(ranNum, "大")
#         elif x == "小":
#             rGuess = robotA.guess(ranNum, "小")
#         if rGuess == True:
#             robotA.Attack(playerA)
#         rGuess = None
#         print("robotB:")
#         x = input("大还是小：")
#         if x == "大":
#             rGuess = robotB.guess(ranNum, "大")
#         elif x == "小":
#             rGuess = robotB.guess(ranNum, "小")
#         if rGuess == True:
#             robotB.Attack(playerA)
#         rGuess = None
#         print("robotC:")
#         x = input("大还是小：")
#         if x == "大":
#             rGuess = robotC.guess(ranNum, "大")
#         elif x == "小":
#             rGuess = robotC.guess(ranNum, "小")
#         if rGuess == True:
#             robotC.Attack(playerA)
#
#
# def test14():
#     playerA = player(700, 20)
#     robotA = robot(100, 10)
#     robotB = robot(200, 10)
#     robotC = robot(400, 5)
#     while True:
#         print("playerA当前还有%i血量，攻击力为%i" % (playerA.hp, playerA.attack))
#         print("robotA当前还有%i血量，攻击力为%i" % (robotA.hp, robotA.attack))
#         print("robotB当前还有%i血量，攻击力为%i" % (robotB.hp, robotB.attack))
#         print("robotC当前还有%i血量，攻击力为%i" % (robotC.hp, robotC.attack))
#         if playerA.hp <= 0:
#             playerA.death()
#         elif robotA.hp <= 0:
#             robotA.death()
#         elif robotB.hp <= 0:
#             robotB.death()
#         elif robotC.hp <= 0:
#             robotC.death()
#
#         Guess(playerA, robotA, robotB, robotC)
#
# test14()
