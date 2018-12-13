# 转换成元类实现单例模式
# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#             print(cls._instance)
#         return cls._instance


class MyClass(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            obj = super(MyClass, cls)
            cls._instance = obj.__new__(cls, *args, **kwargs)
            print(cls._instance)
        return cls._instance
    # def __init__(self):
    #     print("**************************")
    #     print(self._instance)

# 主要起作用的是new方法中的return语句，将每个MyClass对象都变成了第一次创建的对象
# class MyClass2(object):
#     def __new__(cls, *args, **kwargs):
#         pass
print("+++++++++++++++++++")
print(MyClass())
# a1 = MyClass()
print("+++++++++++++++++++")
# print(a1)
print(MyClass())
# a2 = MyClass2()
# print(a2)


# 装饰器实现单例模式
# def Singleton(cls):
#     _instance = {}
#     print(cls)
#     print(_instance)
#
#     def _singleton(*args, **kargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kargs)
#             print(_instance)
#         return _instance[cls]
#
#     return _singleton
#
#
# @Singleton
# class A(object):
#
#     def __init__(self, x=0):
#         self.x = x
#
#
# a1 = A(2)
# print(a1.x)
# a2 = A(30)
# print(a2.x)
