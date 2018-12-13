# !/usr/bin/env python3

# _*_ coding:utf-8 _*_

'''
    关闭前清空client文件
    thread无法访问属性
'''
from tkinter import *
import time, asynchat, asyncore, pickle
import chatClient, threading_local

'''

定义消息发送函数：

1、在<消息列表分区>的文本控件中实时添加时间；

2、获取<发送消息分区>的文本内容，添加到列表分区的文本中；

3、将<发送消息分区>的文本内容清空。

'''


class end():
    # 通过写方法来调用回收
    def __init__(self, name):
        self.name = name

    def __del__(self):
        with open(r"E:\hyx\core\聊天软件的实现\client.txt", "rb") as isNone:  # 用文件保存用户名
            reading = isNone.read()
            names = pickle.loads(reading)
            print(names)
            print(self.name)
            names.remove(self.name)
            names = pickle.dumps(names)
        with open(r"E:\hyx\core\聊天软件的实现\client.txt", "wb") as d:
            d.write(names)


def ending():
    end(nowClient)


def getNowClient():
    open(r"E:\hyx\core\聊天软件的实现\nowClient.txt", 'a')
    with open(r"E:\hyx\core\聊天软件的实现\nowClient.txt", "r") as isNone:  # 用文件保存用户名为列表
        reading = isNone.read()
        if reading != '':
            # print(reading, 1)
            with open(r"E:\hyx\core\聊天软件的实现\nowClient.txt", "w") as dClient:
                dClient.truncate()
            return reading


def msgsend():
    msg = '我' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'

    txt_msglist.insert(END, msg, 'green')  # 添加时间

    txt_msglist.insert(END, txt_msgsend.get('0.0', END))  # 获取发送消息，添加文本到消息列表

    txt_msgsend.delete('0.0', END)  # 清空发送消息


'''定义取消发送 消息 函数'''


def cancel():
    txt_msgsend.delete('0.0', END)  # 取消发送消息，即清空发送消息


'''绑定up键'''


def msgsendEvent(event):
    if event.keysym == 'Up':
        msgsend()


now_clients = set()
nowClient=None

# 重置server.txt

def resetServer():
    with open(r"E:\hyx\core\聊天软件的实现\server.txt", "w") as cover:
        cover.truncate()


def changeLabel(label):
    global users, now_clients,nowClient
    if nowClient==None:
        nowClient=getNowClient()
    while True:
        labelSet = labelName()
        # 如果labelSet比原来少了怎么减少显示
        if labelSet is not None:
            for i in labelSet:
                if i not in now_clients:
                    users.set(users.get() + i + '\n')
                    now_clients.add(i)
        # print("label")
        try:
            label.update()
        except Exception as e:
            print(e)
            break
    # label.config(textvariable=users)


def labelName():
    # 获得label要显示的用户名
    with open(r"E:\hyx\core\聊天软件的实现\client.txt", "rb") as isNone:  # 用文件保存用户名
        reading = isNone.read()
        if reading != b'':
            names = pickle.loads(reading)
            return names


if __name__ == '__main__':
    HOST = '192.168.11.206'
    PORT = 10000
    tk = Tk()

    tk.title('聊天窗口')

    '''创建分区'''

    f_msglist = Frame(height=300, width=300)  # 创建<消息列表分区 >

    f_msgsend = Frame(height=300, width=300)  # 创建<发送消息分区 >

    f_floor = Frame(height=100, width=300)  # 创建<按钮分区>

    f_right = Frame(height=700, width=100)  # 创建<当前用户列表分区>

    '''创建控件'''

    txt_msglist = Text(f_msglist)  # 消息列表分区中创建文本控件

    txt_msglist.tag_config('green', foreground='blue')  # 消息列表分区中创建标签

    txt_msgsend = Text(f_msgsend)  # 发送消息分区中创建文本控件

    txt_msgsend.bind('<KeyPress-Up>', msgsendEvent)  # 发送消息分区中，绑定‘UP’键与消息发送。

    '''txt_right = Text(f_right) #图片显示分区创建文本控件'''

    button_send = Button(f_floor, text='Send', command=msgsend)  # 按钮分区中创建按钮并绑定发送消息函数

    button_cancel = Button(f_floor, text='Cancel', command=cancel)  # 分区中创建取消按钮并绑定取消函数
    button_resetServer = Button(f_floor, text='ResetServer', command=resetServer)  # 分区中创建取消按钮并绑定取消函数
    users = StringVar()
    # print(getName())
    users.set("users:" + '\n')
    label = Label(f_right, textvariable=users)  # 右侧分区中添加列表

    '''分区布局'''

    f_msglist.grid(row=0, column=0)  # 消息列表分区

    f_msgsend.grid(row=1, column=0)  # 发送消息分区

    f_floor.grid(row=2, column=0)  # 按钮分区

    f_right.grid(row=0, column=1, rowspan=3)  # 图片显示分区

    txt_msglist.grid()  # 消息列表文本控件加载

    txt_msgsend.grid()  # 消息发送文本控件加载

    button_send.grid(row=0, column=0, sticky=W)  # 发送按钮控件加载

    button_cancel.grid(row=0, column=1, sticky=W)  # 取消按钮控件加载
    button_resetServer.grid(row=0, column=2, sticky=W)  # 取消按钮控件加载
    label.grid()  # 右侧分区加载标签控件
    # 客户端的启动也需要独立线程
    client = threading_local.Thread(target=chatClient.core)
    client.start()
    '''
        一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
        ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
    '''
    labelUpdate = threading_local.Thread(target=changeLabel, args=(label,))
    # labelUpdate.setDaemon(True)
    labelUpdate.start()
    tk.mainloop()
    # asyncore.loop()
    ending()
    print("end")
