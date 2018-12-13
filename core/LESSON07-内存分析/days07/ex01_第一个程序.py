'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/16 9:22
desc: TODO
'''
# a = 12
# b = 15
#
# z = a + b
# print(z)
#
# m = 27
'''
重点：程序执行过程
    具体发生了什么操作？
        声明变量：分配内存，内存中存储数据
        运算过程：CPU从内存中提取数据，进行运算
        运算结果：CPU将运算结果在内存中申请空间，存放数据
        m=27：PYTHON中为了提高处理效率，内存中[静态区]存放了重要的不可变的一部分数据，用于重复利用
    计算机怎么执行文本源代码？
        通过python解释器，申请内存空间，在内存中加载了程序数据执行了运算。

操作：怎么查看具体的内存分配，具体的执行过程
    目的：通过实际操作过程，可以详细控制执行中的内存操作
    模块：通过第三方模块[memory_profiler]监控程序执行过程中的内存处理情况
    安装：pip install memory_profiler
    操作：这个模块的主要核心，是监控程序执行过程中的[函数/方法]为单元的执行过程
    [python的最小执行单元：代码块]
    memory_profiler模块，监控的内存操作最小执行单元：函数/方法
'''
import memory_profiler


@memory_profiler.profile
def main():
    a = 12
    b = 15

    z = a + b
    print(z)

    m = 27

if __name__ == "__main__":
    main()