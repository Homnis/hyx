import os

allFile = []


def getAllFile(path):
    if os.path.isdir(path):
        pathList = os.listdir(path)
        if len(pathList) != 0:
            for i in pathList:
                newPath = os.path.join(path, i)
                allFile.append(newPath)
                getAllFile(newPath)
    return allFile

# 1.
# import os
#
# path = os.getcwd()
# os.mkdir("py")
# for i in range(1, 11):
#     fileName = path + "\py\\" + str(i)
#     print(fileName)
#     os.mkdir(fileName)

# 2.
# import os
#
# path = "E:\hyx\py"
# allFile = os.listdir(path)
# for i in allFile:
#     if int(i) % 2 == 0:
#         aPath = os.path.join(path, i)
#         os.mkdir(aPath+"\\end")


# 3.
# path = "E:\hyx\py"
# allPath=getAllFile(path)
# for i in range(len(allPath)) :
#     if "end" in allPath[i] :
#         x=allPath[i][-5]
#         if x=="2" or x=="4" or x=="8":
#             os.rename(allPath[i],allPath[i]+x)


# 4.
# os.rmdir(r"E:\hyx\py\2\end2")
# os.rmdir(r"E:\hyx\py\2")


# 5.
# print(getAllFile(r"E:\hyx\py"))

# 6.
# def delAllFile(path):
#     if os.path.isdir(path):
#         pathList = os.listdir(path)
#         print(pathList)
#     if len(pathList) != 0:
#         for i in pathList:
#             newPath = os.path.join(path, i)
#             delAllFile(newPath)
#             os.rmdir(newPath)
#
# delAllFile(r"E:\hyx\py")


# # 7.
# import math
#
# a = 20.73
# upA=math.ceil(a)
# downA=math.floor(a)
# sinA=math.sin(a)
# print(upA,downA,sinA)


# 8.
# import math
#
# def degree(a=math.pi/2):
#     degree=180*a/math.pi
#     return degree
#
# print(degree(math.pi/4))
# print(degree(math.pi / 2))
