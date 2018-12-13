import math


# 1.
# class Circle:
#     pi = math.pi
#
#     def __init__(self, r):
#         self.r = r
#     def s(self):
#         return self.r*self.r*self.pi
#     def c(self):
#         return self.r*2*self.pi

# 2.
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def s(self):
#         return self.height * self.width
#
#     def c(self):
#         return self.width * 2 + self.height * 2

# 3.
# class worker:
#     def __init__(self, name, num):
#         self.name = name
#         self.num = num
#
#     def feed(self, animal, food):
#         animal.beFeed(self, food)
#
#
# class animal:
#
#     def __init__(self, sort, age):
#         self.sort = sort
#         self.age = age
#
#     def beFeed(self, worker, food):
#         print("一只%i岁大的%s被工号为%i的%s喂食了%s" % (self.age, self.sort, worker.num, worker.name, food.food))
#
#
# class food:
#     def __init__(self, food):
#         self.food = food
#
#
# zFood = food("竹子")
# workerA = worker("张三", 123456)
# animalA = animal("熊猫", 5)
# workerA.feed(animalA,zFood)


# 4.
# class Account:
#     def __init__(self, id, password, name, personId, email, balance):
#         self.id = id
#         self.password = password
#         self.name = name
#         self.personId = personId
#         self.email = email
#         self.balance = balance
#
#     def deposit(self, money):  # 存款
#         self.balance += money
#         print("%s的剩余金额为%i" % (self.name, self.balance))
#
#     def withdraw(self, money):  # 取款
#         self.balance-=money
#         print("%s的剩余金额为%i" % (self.name, self.balance))
#
# accountA=Account("abc","159357","张三","123456789","xjp@gov.com",100)
# accountA.deposit(50)


# 5.
# class student:
#     def __init__(self, name, sno, grade):
#         self.name = name
#         self.sno = sno
#         self.grade = grade
#
#     def getGrade(self):
#         return self.grade
#
#
# a = student("a", 1, 60)
# b = student("b", 2, 70)
# c = student("c", 3, 50)
# d = student("d", 4, 90)
# e = student("e", 5, 40)
# list1 = [a, b, c, d, e]
# print(list1)
# Sum, Max, Min = 0, 0, 0
# for i in range(len(list1)):
#     Sum += list1[i].getGrade()
#     if i == 0:
#         Max = list1[i].getGrade()
#         Min = list1[i].getGrade()
#     else:
#         if list1[i].getGrade() > Max:
#             Max = list1[i].getGrade()
#         elif list1[i].getGrade() < Min:
#             Min = list1[i].getGrade()
# Ave = Sum / len(list1)
# print(Sum, Min, Max, Ave)

# 1.
# class student():
#     def __init__(self, cnGrade, mathGrade, enGrade):
#         self.cnGrade = cnGrade
#         self.mathGrade = mathGrade
#         self.enGrade = enGrade
#
#     def getGrade(self):
#         return [self.cnGrade,self.mathGrade,self.enGrade]
#
#
# def level(grade):
#     if 100 >= grade >= 90:
#         return "A"
#     elif 89 >= grade >= 80:
#         return "B"
#     elif 79 >= grade >= 70:
#         return "C"
#     elif 69 >= grade >= 60:
#         return "D"
#     elif grade < 60:
#         return "E"
#     else:
#         print("输入错误")
#
#
# list1 = []
# for i in range(3):
#     cnGrade = int(input("请输入第%i个学生的语文成绩:" % (i+1)))
#     cnLevel = level(cnGrade)
#     mathGrade = int(input("请输入第%i个学生的数学成绩:" % (i+1)))
#     mathLevel = level(mathGrade)
#     enGrade = int(input("请输入第%i个学生的英语成绩:" % (i+1)))
#     enLevel = level(enGrade)
#     a = student(cnGrade=cnLevel, mathGrade=mathLevel, enGrade=enLevel)
#     list1.append(a)
# for i in list1:
#     print(i.getGrade())


# 2.
# class student():
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def getGrade(self):
#         return self.grade
#
# a=student("a",60)
# b=student("b",61)
# c=student("c",62)
# d=student("d",63)
# e=student("e",64)
# list1=[a,b,c,d,e]
# Sum=0
# for i in list1:
#     Sum+=i.getGrade()
# print("总分为：",Sum)
# print("平均分为：",Sum/5)


# 3.
# class player():
#     def __init__(self, name, attack, hp, mp, now):
#         self.attack = attack
#         self.name = name
#         self.hp = hp
#         self.mp = mp
#         self.now = now
#
#     def hit(self, beAttP):
#         beAttP.hp -= self.attack
#         print("%s受到了%i点伤害，还有%i点血量:" % (beAttP.name, self.attack, beAttP.hp))
#
#
# a = player("a", attack=50, hp=100, mp=100, now="good")
# b = player("b", attack=10, hp=100, mp=100, now="good")
# a.hit(b)
