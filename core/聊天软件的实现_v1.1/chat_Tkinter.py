# !/usr/bin/env python3

# _*_ coding:utf-8 _*_

'''
    关闭前清空client文件
    thread无法访问属性
'''
from tkinter import *
import time, pickle,sys,os,shutil
import chatClient, threading_local

'''

定义消息发送函数：

1、在<消息列表分区>的文本控件中实时添加时间；

2、获取<发送消息分区>的文本内容，添加到列表分区的文本中；

3、将<发送消息分区>的文本内容清空。

'''

class end():
    def __init__(self, nowClient,path):
        self.nowClient = nowClient
        self.path=path
        # 获得label要显示的用户名
    def labelName(self):
        '''
            TODO
            将文件存放位置改为对应ip和port文件夹下
        :param name:
        :return:
        '''
        with open(r"{path}\client.txt".format(path=self.path), "rb") as isNone:  # 用文件保存用户名
            reading = isNone.read()
            if reading != b'':
                names = pickle.loads(reading)
                return names

    def __del__(self):
        '''
            TODO
            将文件存放位置改为对应ip和port文件夹下
        :param name:
        :return:
        '''
        with open(r"{path}\client.txt".format(path=self.path), "rb") as isNone:  # 用文件保存用户名
            reading = isNone.read()
            names = pickle.loads(reading)
            # print(names)
            # print(self.name)
            names.remove(self.nowClient)
            names = pickle.dumps(names)
        with open(r"{path}\client.txt".format(path=self.path), "wb") as d:
            d.write(names)
        print(self.labelName)
        labelSet = self.labelName()
        # print(labelSet)
        if labelSet==set():
            shutil.rmtree(self.path)


class watch():
    def __init__(self,address):
        self.address=address
        self.now_clients = set()
        self.nowClient = None
        self.window = Tk()
        ip=str(address[0])
        port=int(address[1])
        self.path = "E:\hyx\core\聊天软件的实现_v1.1\{ip}\{port}".format(ip=ip, port=str(port))
        self.window.title('聊天窗口')

        '''创建分区'''

        f_msglist = Frame(height=300, width=300)  # 创建<消息列表分区 >

        f_msgsend = Frame(height=300, width=300)  # 创建<发送消息分区 >

        f_floor = Frame(height=100, width=300)  # 创建<按钮分区>

        f_right = Frame(height=700, width=100)  # 创建<当前用户列表分区>

        '''创建控件'''

        self.txt_msglist = Text(f_msglist)  # 消息列表分区中创建文本控件

        self.txt_msglist.tag_config('green', foreground='blue')  # 消息列表分区中创建标签

        self.txt_msgsend = Text(f_msgsend)  # 发送消息分区中创建文本控件

        self.txt_msgsend.bind('<KeyPress-Up>', self.msgsendEvent)  # 发送消息分区中，绑定‘UP’键与消息发送。

        '''txt_right = Text(f_right) #图片显示分区创建文本控件'''

        button_send = Button(f_floor, text='Send', command=self.msgsend)  # 按钮分区中创建按钮并绑定发送消息函数

        button_cancel = Button(f_floor, text='Cancel', command=self.cancel)  # 分区中创建取消按钮并绑定取消函数
        button_resetServer = Button(f_floor, text='ResetServer', command=self.resetServer)  # 分区中创建取消按钮并绑定取消函数
        self.users = StringVar()
        # print(getName())

        self.users.set("users:" + '\n')
        label = Label(f_right, textvariable=self.users)  # 右侧分区中添加列表

        '''分区布局'''

        f_msglist.grid(row=0, column=0)  # 消息列表分区

        f_msgsend.grid(row=1, column=0)  # 发送消息分区

        f_floor.grid(row=2, column=0)  # 按钮分区

        f_right.grid(row=0, column=1, rowspan=3)  # 图片显示分区

        self.txt_msglist.grid()  # 消息列表文本控件加载

        self.txt_msgsend.grid()  # 消息发送文本控件加载

        button_send.grid(row=0, column=0, sticky=W)  # 发送按钮控件加载

        button_cancel.grid(row=0, column=1, sticky=W)  # 取消按钮控件加载
        button_resetServer.grid(row=0, column=2, sticky=W)  # 取消按钮控件加载
        label.grid()  # 右侧分区加载标签控件
        # 客户端的启动也需要独立线程
        self.nowClient = self.getNowClient()

        client = threading_local.Thread(target=chatClient.core, args=(self.address,self.txt_msgsend, self.txt_msglist, self.nowClient,))
        client.start()
        '''
            一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
            ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
        '''
        labelUpdate = threading_local.Thread(target=self.changeLabel, args=(label,))
        # labelUpdate.setDaemon(True)
        labelUpdate.start()
        self.window.mainloop()
        # asyncore.loop()
        end(self.nowClient,self.path)

    def getNowClient(self):
        '''
            TODO
            将文件存放位置改为对应ip和port文件夹下
        :param name:
        :return:
        '''
        open(r"{path}\nowClient.txt".format(path=self.path), 'a')
        with open(r"{path}\nowClient.txt".format(path=self.path), "r") as isNone:  # 用文件保存用户名为列表
            reading = isNone.read()
            if reading != '':
                # print(reading, 1)
                with open(r"{path}\nowClient.txt".format(path=self.path), "w") as dClient:
                    dClient.truncate()
                return reading

    def msgsend(self):
        # txt_msglist.insert(END, msg, 'green')  # 添加时间
        #
        # txt_msglist.insert(END, txt_msgsend.get('0.0', END))  # 获取发送消息，添加文本到消息列表
        #
        time.sleep(0.2)
        self.txt_msgsend.delete('0.0', END)  # 清空发送消息

    '''定义取消发送 消息 函数'''

    def cancel(self):
        self.txt_msgsend.delete('0.0', END)  # 取消发送消息，即清空发送消息

    '''绑定up键'''

    def msgsendEvent(self,event):
        if event.keysym == 'Up':
            self.msgsend()


    # 重置server.txt

    def resetServer(self):
        '''
            TODO
            将文件存放位置改为对应ip和port文件夹下
        :param name:
        :return:
        '''
        os.removedirs(self.path)

    def changeLabel(self,label):
        if self.nowClient == None:
            self.nowClient = self.getNowClient()
        while True:
            try:
                # labelSet是一个要显示的set类型
                labelSet = self.labelName()
                # labelSet={'h'}
                # now_clients={'h','hyx'}
                # 如果labelSet比原来少了怎么减少显示
                # print(labelSet)
                if labelSet is not None:
                    for i in labelSet:
                        if i not in self.now_clients:
                            self.users.set(self.users.get() + i + '\n')
                            self.now_clients.add(i)

                    #  如果now_clients中有不存在的i，重新读取用户列表
                    delClient = self.now_clients - labelSet
                    # print(delClient)
                    if delClient != set():
                        self.now_clients = self.now_clients - delClient
                        self.users.set("users:" + '\n')
                        for i in self.now_clients:
                            self.users.set(self.users.get() + i + '\n')
            except Exception as e:
                print(e)
                break
            # print("label")
            try:
                label.update()
            except Exception as e:
                print(e)
                break
        # label.config(textvariable=users)

    def labelName(self):
        # 获得label要显示的用户名
        '''
            TODO
            将文件存放位置改为对应ip和port文件夹下
        :param name:
        :return:
        '''
        with open(r"{path}\Client.txt".format(path=self.path), "rb") as isNone:  # 用文件保存用户名
            reading = isNone.read()
            if reading != b'':
                names = pickle.loads(reading)
                return names

#
# if __name__ == '__main__':
#     HOST = '192.168.11.206'
#     PORT = 10000
#     watch()
#     print("end")

