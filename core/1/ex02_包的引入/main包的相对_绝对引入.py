'''
AUTHOR: DAMU 牟文斌
VERSION: V1.0.000
DESC: TODO
'''
# 1. 绝对引入：直接引入包中的模块
# pycharm开发工具：会自动搜索site-packages/PYTHONPATH/sys.path路径下查询对应的模块
# python解释器(CPython)：自动搜索[三个标准路径+当前路径]
# import modules.tools
# # 使用模块中的变量
# print(modules.tools.msg)
# # 使用模块中的函数
# modules.tools.test()
# # 使用模块中的类型
# a = modules.tools.Author()
# print(a)

# 2. 相对引入方式：包含了相对路径的操作
from .modules import tools
#使用模块中的变量
print(tools.msg)
# 使用模块中的函数
tools.test()
# 使用模块中的类型
author = tools.Author()
print(author)

'''
包的相对引入和绝对引入
    1. 相对于当前正在开发的内部项目，使用相对路径引入包进行操作
        from .modules import tools
    
    2. 相对于要发布到网络上的工具模块/在公司多个项目中使用的公共模块，使用绝对路径引入包的方式进行操作
        from modules import tools
        

'''
