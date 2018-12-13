'''
AUTHOR: DAMU 牟文斌
VERSION: V1.0.000
DESC: TODO
'''
# 1. 引入方式：直接一个模块[店家推荐]
import utils

# 使用过程中，必须通过 模块名称.变量名称/函数名称/类型名称 使用
print(utils.msg)
utils.test()
p = utils.Person()


# 2. 引入方式：通过模块，引入模块中的变量/函数/类型
from utils import msg, test, Person # 不推荐：代码的可读性较低

# n行代码

# 分辨不清msg/test/Person 是当前模块的数据，还是其他模块的数据
print(msg)
test()
p = Person()
