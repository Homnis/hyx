'''
AUTHOR: DAMU 牟文斌
VERSION: V1.0.000
DESC: TODO
'''
# 1. 直接引入包: 使用包中的模块~必须在当前包的__init__.py文件中主动引入【不推荐】
# import modules

# print(modules.tools.msg)
# print(modules.utils.msg)
# modules.tools.test()

# 2. 直接引入包->模块【推荐：代码可读性较高】
# import modules.tools #可以这样引入
# print(modules.tools.msg)
#
# import modules.tools as t # 【店家推荐：**】
# print(t.msg)
#
# # 熟练
# from modules import tools # 【店家推荐：***】
# print(tools.msg)
#
# # 3. 包的引入第三种方式【不推荐】
# from modules.tools import msg, test, Author
#
# # 原因：可读性很差[变量的定义造成了误读：分辨不清这个变量是当前模块还是其他模块]
# print(msg)
#
# msg = "hello"
#
# print(msg)


import modules

print(modules.utils.msg)
print(modules.new.msg)
'''
操作过程中，项目开发会有很多规范
    1. 公司项目组规范
    2. 行业规范
    3. 标注规范
'''