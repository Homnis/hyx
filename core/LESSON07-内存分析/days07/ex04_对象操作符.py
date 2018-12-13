'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/16 11:11
desc: TODO
'''
'''
== :用来判断符号两端的变量中存储的数据是否相同
is: 用来判断符号两端的变量中存储的是否同一个对象[内存地址是否相同]
'''
# 1. 基本数据类型
# a = 12
# b = 12
# print(a == b) # True
# print(a is b) # True
#
# a = 1000
# b = 1000
# print(a == b) # True
# print(a is b) # True[交互模式下，这个内存重新申请~False]

# 2. 对象的形式
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#
# p1 = Person("tom")
# p2 = Person("tom")
#
# print(p1 == p2) # False
# print(p1 is p2) # False

# 3. 对象的判断
class Person:

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False


if __name__ == "__main__":
    # 需求变动：认为name相同的Person对象，是同一个对象
    '''
    对象通过==符号进行比较操作时
    1. 计算对象的特征值：通过对象的__hash__()计算出来的
    2. 比较对象的特征值：通过对象的__eq__()进行比较得到结果的
    
    结论：如果要对对象进行比较关系的重写
        一定要重写__hash__()和__eq__()两个函数
        在以后的开发中，经常互相依赖使用
    '''
    p1 = Person("tom")
    p2 = Person("tom")

    print(p1 == p2) # False  True
    print(p1 is p2) # False  False
    print(p1.__hash__())
    print(p2.__hash__())