'''
AUTHOR: DAMU 牟文斌
VERSION: V1.0.000
DESC: 测试包和模块的操作
'''
# 直接引入一个模块
# import utils

# 从一个包中引入一个模块
from models import Users # site-packages/PYTHONPATH/sys.path


# print(utils.msg)
print(Users.msg)

'''
1. from models import Users
    import xxx
    绝对路径引入：绝对引入~ 
        引入模块：从项目根路径引入
        引入包：直接通过包名称引入[__init__.py文件]
2. from .models import Users
    相对路径引入：
        引入模块
        引入包
    注意父级路径
'''