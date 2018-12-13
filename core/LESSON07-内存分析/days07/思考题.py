'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/16 11:47
desc: TODO
'''
'''
对象的拷贝：
    引用赋值：程序中只有一个对象、复制了对象的引用，多个引用变量指向同一个对象
    浅拷贝：程序中有多个对象，多个对象中的数据属性，指向的是相同的数据
    深拷贝：程序中有多个独立的对象

思考题：请尝试通过内存分析分析三种不同拷贝模式下的内存分配情况
'''

from memory_profiler import profile

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __repr__(self):
    #     return self.name

@profile(precision=10)
def main():
    p1 = Person('Tom', 18)
    print(p1)

    p2 = Person('Jerry', 18)
    print(p2)



if __name__ == "__main__":

     # 通过Person对象的引用赋值、浅拷贝、深拷贝，进行内存分析，形成文档。
     # p1 = Person("tom")
     # p2 = Person("tom")
     # p3 = p2
     # q1 = Person(20)
     # q2 = Person(20)
     # q1 = q2

     # c = set()
     # c.add(p1)
     # c.add(p2)
     # c.add(p3)
     # c.add(q1)
     # c.add(q2)

     # print(c)
    main()

