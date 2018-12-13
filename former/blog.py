import json
import pickle
import os
import io


def reg(name="", psw=""):
    dictReg = {name: psw}
    x = pickle.dumps(dictReg)
    with open(r"E:\hyx\reg.txt", "rb") as isNone:  # 判断是否为空，不为空的话重新建立字典，代替原有的
        reading = isNone.read()
    if reading != "b''":
        y = pickle.loads(reading)
        y[name] = psw
        y = pickle.dumps(y)
        with open(r"E:\hyx\reg.txt", "bw") as cover:
            cover.write(y)
    else:
        with open(r"E:\hyx\reg.txt", "bw") as userReg:
            userReg.write(x)
    print("注册成功")


def load(name="", psw=""):
    with open(r"E:\hyx\reg.txt", "rb") as isTrue:
        a = pickle.load(isTrue)
        if a[name] == psw:
            return True
        else:
            return False


def writer(title="", author="", time="", str="", userName=""):
    dictWrite = {str: title, title: author, time: str}
    x = pickle.dumps(dictWrite)
    path = "E:\hyx\write%s.txt" % (userName)
    open(path, 'a')
    with open(path, 'bw') as writing:
        writing.write(x)


def toFind(userName="", author=""):
    path = "E:\hyx\write%s.txt" % (userName)
    if os.path.exists(path) == False:
        print("不存在")
    else:
        with open(path, 'rb') as find:
            x = find.read()
        findDict = pickle.loads(x)
        for (key, value) in findDict.items():
            if value == author:
                print("题目是：", key)
                title = key
        for (key, value) in findDict.items():
            if value == title:
                str = key
        for (key, value) in findDict.items():
            if value == str:
                print("时间是：", key)


def look(userName="", title=""):
    path = "E:\hyx\write%s.txt" % (userName)
    if os.path.exists(path) == False:
        print("不存在")
    else:
        with open(path, 'rb') as find:
            x = find.read()
        findDict = pickle.loads(x)
        for (key, value) in findDict.items():
            if value == title:
                print(key)


def delete(userName="", title=""):
    path = "E:\hyx\write%s.txt" % (userName)
    if os.path.exists(path) == False:
        print("不存在")
    else:
        with open(path, 'rb') as find:
            x = find.read()
        findDict = pickle.loads(x)
        for (key, value) in findDict.items():
            if value == title:
                str = key
        for (key, value) in findDict.items():
            if value == str:
                time = key
        findDict.pop(str)
        findDict.pop(time)


def change(userName="", title="", str=""):  # str:title , title:author , time:str
    path = "E:\hyx\write%s.txt" % (userName)
    if os.path.exists(path) == False:
        print("不存在")
    else:
        with open(path, 'rb') as find:
            x = find.read()
        findDict = pickle.loads(x)
        for (key, value) in findDict.items():
            if value == title:
                x = key
        findDict[str] = findDict.pop(x)
        for (key, value) in findDict.items():
            if value == x:
                time = key
        findDict[time] = str

isUsers=input("是否已注册：(y/n)")
userName = input("请输入用户名：")
psw=input("请输入密码：")
loading=0
if isUsers=="y" :
    if load(userName,psw):
        loading=1
        print("登陆成功")
    else :
        print("登录失败")
elif isUsers=="n":
    reg(userName,psw)
wanna=int(input("你想做什么：1.写文章 ，2.查文章 ，3.删除文章 ，4.修改文章 ，5. 退出"))
if wanna==1 : # title="", author="", time="", str="", userName=""
    title=input("标题为：")
    author=input("作者为：")
    time=input("时间为：")
    str=input("请输入内容：")
    writer(title=title,author=author,time=time,str=str,userName=userName)
elif wanna==2:
    title = input("标题为：")
    look(userName=userName,title=title)
elif wanna==3:
    title = input("标题为：")
    delete(userName=userName,title=title)
elif wanna==4:
    title = input("标题为：")
    str = input("请输入内容：")
    change(userName=userName,title=title,str=str)
else :
    os._exit(5)

