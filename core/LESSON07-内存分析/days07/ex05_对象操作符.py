'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/16 11:22
desc: TODO
'''
'''
set 集合：可以存放不重复的对象数据
    首先得到要添加对象的特征数据/特征值：hash值
    其次和集合中的数据进行比较运算：False->添加；True->无操作
'''
class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False

    def __hash__(self):
        return self.name.__hash__()


if __name__ == "__main__":
    # 项目需要，用户数据临时存储到集合中[剔重]
    p1 = Person("tom")
    p2 = Person("tom")
    p3 = Person("jerry")
    p4 = Person("shuke")

    customers = set()
    customers.add(p1)
    customers.add(p2)
    customers.add(p3)
    customers.add(p4)

    print(customers)