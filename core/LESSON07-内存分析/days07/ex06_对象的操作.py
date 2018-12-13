'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/16 11:29
desc: TODO
'''
'''
内存中的对象：可以被多个变量同时指向
    好处：可以灵活的通过多个不同的变量在不同的地方操作同一个对象

程序中的对象：可以有一份对象多个引用变量，可以有多份相同的对象
    对象和对象之间怎么操作？
        多个变量怎么指向同一个对象？
        同一个对象，怎么扩展复制出来多个相同对象？
    目标：为了让对象在程序中操作更加灵活。
    
内存中的对象拷贝：
    1. 对象的引用赋值
    2. 对象的浅拷贝
    3. 对象的深拷贝
'''
class Person:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


if __name__ == "__main__":
    p1 = Person("tom")
    p2 = Person("tom")
    p3 = p2

    c = set()
    c.add(p1)
    c.add(p2)
    c.add(p3)

    print(c)
