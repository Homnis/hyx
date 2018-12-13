import json
import pickle
import os


def reg(name="", psw=""):
    dictReg = {name: psw}
    x = pickle.dumps(dictReg)
    path = "reg.txt"
    open(path, 'a')
    if os.path.exists(path) == False:
        print("不存在")
    else:
        with open("reg.txt", "rb") as isNone:  # 判断是否为空，不为空的话重新建立字典，代替原有的
            reading = isNone.read()
        if reading != b'':
            y = pickle.loads(reading)
            y[name] = psw
            with open("reg.txt", "bw") as cover:
                pickle.dump(y, cover)
        else:
            with open("reg.txt", "bw") as userReg:
                userReg.write(x)
        print("注册成功")


def load(name="", psw=""):
    with open("reg.txt", "rb") as isTrue:
        a = pickle.load(isTrue)
        if a[name] == psw:
            return True
        else:
            return False


def add(sno="", name="", grade=60):  # {sno:[name,grade]}
    path = "students.txt"
    open(path, 'a')
    if os.path.exists(path) == False:
        print("不存在")
    else:
        with open(path, "rb") as read:
            if read.read() != b'':
                with open(path, "rb") as read:
                    dict = pickle.load(read)
                    dict[sno] = [name, grade]
                    # print(dict)
                with open(path, 'bw') as writing:
                    pickle.dump(dict, writing)
                    print("添加成功")
            else:
                with open(path, 'bw') as write:
                    dict = {sno: [name, grade]}
                    pickle.dump(dict, write)
                    print("添加成功")


def allFind():
    path = "students.txt"
    if os.path.exists(path) == False:
        print("不存在")
    else:
        with open(path, "rb") as allFind:
            dict = pickle.load(allFind)
            print(dict)


def oneFind(sno=""):
    path = "students.txt"
    if os.path.exists(path) == False:
        print("不存在1")
    else:
        with open(path, "rb") as oneFind:
            dict = pickle.load(oneFind)
            for (key, value) in dict.items():
                if key == sno:
                    print(key, "：", value)


def change(sno="", name="", grade=60):
    path = "students.txt"
    if os.path.exists(path) == False:
        print("不存在")
    else:
        with open(path, "rb") as getName:  # 找出对应项
            dict = pickle.load(getName)
            for (key, value) in dict.items():
                if key == sno:
                    dict[key] = [name, grade]
                    with open(path, "bw") as changeGrade:
                        pickle.dump(dict, changeGrade)
                        print("修改成功")


def delete(sno=""):
    path = "students.txt"
    if os.path.exists(path) == False:
        print("不存在")
    else:
        with open(path, "rb") as find:
            if find.read() == b'':
                print("不存在")
            else:
                with open(path, "rb") as delete:
                    dict = pickle.load(delete)
                    if dict.get(sno) == None:
                        print("不存在")
                    else:
                        del dict[sno]
                with open(path, "bw") as write:
                    pickle.dump(dict, write)
                    print("删除成功")


def sortPrint():
    list1 = []
    list2 = []
    areaDict = {}
    path = "students.txt"
    if os.path.exists(path) == False:
        print("不存在")
    else:
        with open(path, "rb") as find1:
            if find1.read() == b'':
                print("不存在")
            else:
                with open(path, "rb") as find2:
                    dict = pickle.load(find2)
                    areaDict = dict
                    for (key, value) in dict.items():
                        x = value[1]
                        list1.append(x)
                        list2.append(key)
    for i in range(len(list1)):
        for n in range(len(list1)):
            if i + n < len(list1):
                if list1[i] <= list1[i + n]:  # 从小至大排序
                    continue
                else:  # 交换位置
                    Min = list1[i + n]
                    list1[i + n] = list1[i]
                    list1[i] = Min
                    Min = list2[i + n]
                    list2[i + n] = list2[i]
                    list2[i] = Min
    for i in range(len(list2)):
        for (key, value) in areaDict.items():
            if key == list2[i]:
                print(key, " : ", areaDict[key])


def manage():
    while True:
        print("班级管理")
        print("*" * 30)
        wanna = int(input("请输入要进行的操作： 1.添加成绩 ， 2.查询所有 ， 3.查询一位 ，4.修改成绩 ，5.删除学员 ，6.排序显示 ，7.退出系统"))
        if wanna == 1:
            sno = input("请输入学号:")
            name = input("请输入姓名：")
            grade = int(input("请输入成绩："))
            add(sno=sno, name=name, grade=grade)
        elif wanna == 2:
            allFind()
        elif wanna == 3:
            sno = input("请输入学号:")
            oneFind(sno)
        elif wanna == 4:
            sno = input("请输入学号:")
            name = input("请输入姓名：")
            grade = int(input("请输入成绩："))
            change(sno=sno, name=name, grade=grade)
        elif wanna == 5:
            sno = input("请输入学号:")
            delete(sno)
        elif wanna == 6:
            sortPrint()
        elif wanna == 7:
            break

while True:
    wanna=int(input("请输入要进行的操作： 1. 登录 ， 2. 注册 ， 3.退出"))
    if wanna==1 :
        userName=input("请输入用户名：")
        psw=input("请输入密码：")
        if load(userName,psw)==True :
            manage()
        else :
            print("错误")
            continue
    elif wanna==2 :
        userName = input("请输入用户名：")
        psw = input("请输入密码：")
        reg(userName,psw)
        continue
    else :
        os._exit(5)
