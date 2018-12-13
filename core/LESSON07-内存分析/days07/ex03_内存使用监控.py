# coding:gbk
'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/16 9:42
desc: TODO
'''
import memory_profiler

@memory_profiler.profile
def test(a):
    a.append(10)

@memory_profiler.profile
def test2(b):
    b = 20

@memory_profiler.profile
def main():
    x = [100]
    y = 200

    test(x)
    test2(y)

    print(x, y)


if __name__ == "__main__":
    main()

'''
内存处理的监控使用
1. 将可运行的代码，全部封装成函数
    公司标准规则：程序执行的入口：一个函数的调用

2. 模块的使用入门教程
    ERROR：查看官方手册、查看百度结果、查看各种资料，得到一整套使用流程，然后再去使用这个技术
    --> 查询对应的官方操作手册[备用]、
        --> 入门手册[1~2页]
    --> 查看搜索到的操作代码[通读]
        --> 核心：操作的代码部分
'''
