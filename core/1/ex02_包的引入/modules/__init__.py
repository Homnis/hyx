'''
AUTHOR: DAMU 牟文斌
VERSION: V1.0.000
DESC: python标准包 声明文件
'''

from . import tools
import utils
# 因为之前运行过utils的同名模块的引入，所以默认能寻找到，不会报错
# 但当执行这条语句时，引入的还是正确的utils模块
from . import new
# import ...