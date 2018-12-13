import math


# 6.
# class Animal:
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food
#
#     def eat(self, name, food):
#         pass
#
#
# class Cat(Animal):
#
#     def __init__(self, name, food):
#         super().__init__(name, food)
#
#     def eat(self):
#         print("一只叫%s的猫吃了%s" % (self.name, self.food))
#
#
# class Dog(Animal):
#
#     def __init__(self, name, food):
#         self.food=food
#         self.name=name
#
#     def eat(self):
#         print("一只叫%s的狗吃了%s" % (self.name, self.food))
#
#
# a = Dog("a", "骨头")
# a.eat()


# 7.
# class Shape:
#     def __init__(self) -> None:
#         super().__init__()
#
#     def length(self):
#         pass
#
#     def area(self):
#         pass
#
#
# class Rect(Shape):
#     def __init__(self, a, b) -> None:
#         self.a = a
#         self.b = b
#
#     def length(self):
#         self.leng = self.a * 2 + self.b * 2
#
#     def area(self):
#         self.s = self.a * self.b
#
#     def getLeng(self):
#         self.length()
#         return self.leng
#
#     def getArea(self):
#         self.area()
#         return self.s
#
#
# class Circle(Shape):
#     def __init__(self, r) -> None:
#         self.r = r
#
#     def length(self):
#         self.leng = math.pi * self.r * 2
#
#     def area(self):
#         self.s = self.r * self.r * math.pi
#
#     def getLeng(self):
#         self.length()
#         return self.leng
#
#     def getArea(self):
#         self.area()
#         return self.s
#
#
# class Square(Rect):
#     def __init__(self, a):
#         self.a = a
#
#     def length(self):
#         self.leng = self.a * 4
#
#     def area(self):
#         self.s = self.a * self.a
#
#     def getLeng(self):
#         self.length()
#         return self.leng
#
#     def getArea(self):
#         self.area()
#         return self.s
#
#
# a = Square(10)
# b = Rect(5, 6)
# c = Circle(20)
# list1 = [a, b, c]
# for i in list1:
#     x = i.getLeng()
#     y = i.getArea()
#     print("周长为：", x)
#     print("面积为:", y)


# 8.
# class People:
#     _name=""
#     _age=1
#     def __init__(self) -> None:
#         super().__init__()
#
#     def GetAge(self):
#         return self._age
#
# class Employee(People):
#     def __init__(self,empno) -> None:
#         self._empno=empno
#
# class Teacher(People):
#     def __init__(self,teacherNo) -> None:
#         self.teacherNo=teacherNo


# 9.(1)
#
# class User:
#     def __init__(self, userName, psw):
#         self.__userName = userName
#         self.__psw = psw
#
#     def setUserName(self,userName):
#         self.__userName=userName
#
#     def getUserName(self):
#         return self.__userName
#
#     def setPsw(self,psw):
#         self.__psw=psw
#
#     def getPsw(self):
#         return self.__psw
#
#
# a = User("a", "123")
# print(a.getUserName())

# 9.(2)
# class student:
#     def __init__(self, userName, name, sex, birth):
#         self.userName = userName
#         self.name = name
#         self.sex = sex
#         self.birth = birth
#
#     def Display(self):
#         print(self.userName, self.name, self.sex, self.birth)
#
#     def Modify(self, name):
#         self.name = name
#
#
# a=student("abc","hyx","男","1995")
# a.Display()
#
# 9.(3)
# class Granduate(student):
#
#     def __init__(self, userName, name, sex, birth,subject,adviser):
#         super().__init__(userName, name, sex, birth)
#         self.subject = subject
#         self.adviser = adviser


#
#     def Display(self):
#         print(self.userName, self.name, self.sex, self.birth, self.subject, self.adviser)
#
# a = Granduate("abc", "hyx", "男", "1995", "subject1", "adviser1")
# a.Display()

# 10.
# class Person:
#     def __init__(self, age, name, gender):
#         self.age = age
#         self.name = name
#         self.gender = gender
#
#     def Display(self):
#         print(self.name, ": ", "Person")
#
#
# class Employee(Person):
#
#     def __init__(self, age, name, gender,number):
#         super().__init__(age, name, gender)
#         self.number=number


#
#     def Display(self):
#         print(self.name, ": ", "Employee")
#
#
# class Executive(Employee):
#     def __init__(self, age, name, gender, number):
#         super().__init__(age, name, gender, number)
#
#     def Display(self):
#         print(self.name, ": ", "Executive")
#
#
# def Main():
#     a1 = Executive(18, "a1", "nan", "111")
#     a2 = Executive(19, "a2", "nan", "222")
#     a3 = Executive(20, "a3", "nan", "333")
#     a4 = Executive(21, "a4", "nv", "444")
#     a5 = Executive(22, "a5", "nan", "555")
#     list1 = [a1, a2, a3, a4, a5]
#     b1 = Employee(18, "b1", "男", "11")
#     b2 = Employee(19, "b2", "男", "22")
#     b3 = Employee(20, "b3", "女", "33")
#     b4 = Employee(21, "b4", "男", "44")
#     b5 = Employee(22, "b5", "男", "55")
#     list2 = [b1, b2, b3, b4, b5]
#     for i in list2:
#         i.Display()
#     for i in list1:
#         i.Display()
#
# Main()


# 11.
class Book:
    def __init__(self, name, author):
        self.Name=name
        self.__author = author


    @property
    def Name(self):
        return  self.__name
    @Name.setter
    def Name(self,name):
        self.__name=name

    # def setName(self, name):
    #     self.__name = name
    #
    # def getName(self):
    #     return self.__name
    #
    # def setAuthor(self, author):
    #     self.__author = author
    #
    # def getAuthor(self):
    #     return self.__author


class AudioBook(Book):
    def __init__(self, name, author,speaker):
        super().__init__(name, author)
        self.__speaker=speaker


    def setSpeaker(self,speaker):
        self.__speaker=speaker
    def getSpeaker(self):
        return self.__speaker

# a=AudioBook("如何割韭菜","a","维尼")
# print(a.getName(),a.getAuthor(),a.getSpeaker())
# a.setAuthor("b")
# print(a.getName(),a.getAuthor(),a.getSpeaker())
b=Book("a","张三")
# b.Name="b"
print(b.Name)

# 12.
# class Employee:
#     def __init__(self, name, num, level,money):#money为基本工资,Pay()为工资总额
#         self._name = name
#         self._num = num
#         self._level=level
#         self._money=money
#     def Pay(self):
#         days=int(input("请输入请假天数："))
#         return 1000*self._level+self._money-days*100
#
# class Technician(Employee):
#
#     def __init__(self, name, num, level, money,add_per_hour,time,factor):
#         super().__init__(name, num, level, money)
#         self._addMoney=add_per_hour
#         self._time=time
#         self._factor=factor
#         self._yjPay=add_per_hour*factor*time
#
#     def Pay(self):
#         return 1000*self._level+self._money+self._yjPay
#
# class Salesman(Employee):
#
#     def __init__(self, name, num, level, money,sale,saleRate):
#         super().__init__(name, num, level, money)
#         self._sale=sale
#         self._saleRate=saleRate
#         self._yjPay=saleRate*sale
#
#     def Pay(self):
#         return 1000*self._level+self._money+self._yjPay
#
# class Manager(Employee):
#     def __init__(self, name, num, level, money,bonus,rate):
#         super().__init__(name, num, level, money)
#         self._bonus=bonus
#         self._rate=rate
#         self._yjPay=bonus*rate
#
#     def Pay(self):
#         return 1000*self._level+self._money+self._yjPay
#
# a=Manager("a","123456",5,5000,2000,0.5)
# print(a.Pay())

