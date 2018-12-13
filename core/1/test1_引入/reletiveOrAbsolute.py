# 1. 绝对引入，要设置路径为所用包，即右键所用包，选择Mark Directory as sources root
#    从.site-packages/  pythonpath sys.path 当前路径下查询是否有所用模块
# import beUsed
#
# print(beUsed.msg)
# beUsed.test()
# p=beUsed.Person()
# print(p)

# 从当前路径下，查询指定的模块【一般是相对于父级文件夹】
# from . import beUsed
#
# beUsed.test()
# print(beUsed.msg)


# 3.
# from beUsed import test
#
# test()