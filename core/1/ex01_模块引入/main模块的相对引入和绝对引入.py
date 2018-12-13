'''
AUTHOR: DAMU 牟文斌
VERSION: V1.0.000
DESC: TODO
'''
# 1，绝对引入
import utils

# 使用另外一个模块中的变量 (没有全局/局部变量的概念)
print(utils.msg)

# 使用另外一个模块的函数
utils.test()

# 使用另一个模块的类型
p = utils.Person()
print(p)


#2，相对引入：从当前文件夹/目录/路径中，查询并引入utils模块
from . import utils

# 使用模块的变量
print(utils.msg)
# 调用执行函数
utils.test()
# 使用模块中的类型
p = utils.Person()
print(p)

'''
两种使用情况
1. 如果开发应用软件：产品
    第一种引入方式使用较多，import 模块名称
    ~多人协同开发，当前模块只会在当前项目中使用。

2. 如果开发的工具软件：工具模块~pymysql/pygame
    第二种引入方式使用较多，from pygame import K_A
    ~当前开发的包，可能会被不同的项目引入使用。

'''


