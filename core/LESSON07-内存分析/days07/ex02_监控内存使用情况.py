'''
author: 大牧 牟文斌
version: V1.0.0
time: 2018/10/16 9:36
desc: TODO
'''
from memory_profiler import profile


@profile
def main():
    f = open("Python-Core.pdf", 'rb')

    print(f.read())

    f.close()


if __name__ == "__main__":
    main()

'''
工具模块：每一个工具模块都有自己的使用场景
    脱离了使用场景，这个模块的使用价值和参考价值就不会很大！

如果只是监控代码执行过程中内存 处理情况，使用memory_profiler即可
    提示：也有类似的操作模块，可以自行扩展
    可以参考源代码
如果要监控程序执行过程中的总的内存消耗，请查询对应的操作模块
'''