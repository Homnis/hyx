import tkinter as tk
from tkinter import messagebox
import pickle, runpy, threading, chat_Tkinter,os,shutil,chatServer


now_client = set()


# 设置登陆窗口属性


# 当前用户列表


# 登陆函数
class Login():
    def __init__(self, window, userName, psw):
        self.window = window
        self.userName = userName
        self.psw = psw
        self.address = (0, 0)
        self.usr_login()

    def portWatch(self):
        # 通过弹出窗口传递ip和port值，点击确定按钮之后，返回对应的ip和port值，在startServer方法中
        # 通过os读取对应ip文件夹下的对应port文件夹，
        # 若存在，则直接启动聊天窗口及client模块，若不存在，则启动聊天窗口及server，并弹出提示窗口：
        # “你是第一个进入此聊天室的用户”
        self.enter_ip = tk.Toplevel(self.window)
        self.enter_ip.geometry('350x200')
        self.enter_ip.title('ip&port')

        new_ip = tk.StringVar()
        new_ip.set('')
        tk.Label(self.enter_ip, text='ip:').place(x=80, y=10)
        entry_new_ip = tk.Entry(self.enter_ip, textvariable=new_ip)
        entry_new_ip.place(x=150, y=10)

        new_port = tk.StringVar()
        tk.Label(self.enter_ip, text='port:').place(x=80, y=50)
        entry_port = tk.Entry(self.enter_ip, textvariable=new_port, show='*')
        entry_port.place(x=150, y=50)

        btn_set = tk.Button(self.enter_ip, text='确定',
                            command=lambda: self.getPort(new_ip, new_port))
        btn_set.place(x=160, y=130)

    def getPort(self, ipArea, portArea):
        ip = ipArea.get()
        port = portArea.get()
        self.address = (ip, port)
        print(self.address)
        ip = str(self.address[0])
        port = self.address[1]
        self.path = "E:\hyx\core\聊天软件的实现_v1.1\{ip}\{port}".format(ip=ip, port=str(port))
        if os.path.exists(self.path):
            open(r"{path}\client.txt".format(path=self.path), "a")
        elif os.path.exists(self.path) is False:
            os.makedirs(self.path)
            open(r"{path}\client.txt".format(path=self.path), "a")
        # print(self.existClients())
        if self.existClients() is None:
            tk.messagebox.showinfo(title='Welcome', message='Welcome,' + self.name)
            # print(type(name))
            # print(name)
            self.createName(self.name)
            self.window.destroy()
            startServe = threading.Thread(target=self.startServer, )
            startServe.start()
            chat_Tkinter.watch(self.address)
        elif self.name not in self.existClients():
            tk.messagebox.showinfo(title='Welcome', message='Welcome,' + self.name)
            # print(type(name))
            # print(name)
            self.createName(self.name)
            self.window.destroy()
            chat_Tkinter.watch(self.address)
        else:
            tk.messagebox.showerror('对不起', '用户已登录')

        # runpy.run_path('chat_Tkinter.py', run_name='__main__')

    def usr_login(self):
        # 获取输入的账号密码

        name = self.userName.get()
        psw = self.psw.get()
        open(r"E:\hyx\core\聊天软件的实现_v1.1\reg.txt", 'a')
        with open(r"E:\hyx\core\聊天软件的实现_v1.1\reg.txt", "rb") as isNone:  # 判断是否为空，不为空的话重新建立字典，代替原有的
            reading = isNone.read()
            # print(reading)
            if reading != b'':
                with open(r"E:\hyx\core\聊天软件的实现_v1.1\reg.txt", "rb") as isTrue:
                    a = pickle.load(isTrue)
                    if name in a:
                        if a[name] == psw:
                            # 登陆成功
                            self.name = name
                            self.portWatch()
                            # if name not in self.existClients():
                                # 登录成功之后，进行ip和port的输入
                            # else:
                            #     tk.messagebox.showerror('对不起', '用户已登录')
                        else:
                            tk.messagebox.showerror('对不起', '用户名或密码错误!')
                    else:
                        tk.messagebox.showerror('对不起', '不存在该用户!')
            else:
                print("无数据")

    def startServer(self):
        '''
            TODO
            通过对应ip下的port文件夹是否存在，来判断服务器是否已创建
            如果没有创建，创建该文件并运行服务端代码
        :return:
        '''
        # print(self.path)
        # serveOrNot=os.path.exists(self.path)
        # if serveOrNot is False:
        #     os.makedirs(self.path)
        chatServer.start(self.address,self.path)
        # elif serveOrNot is True:
        #     print("服务端已在运行")

    def createName(self, name):
        '''
            TODO
            将文件存放位置改为对应ip和port文件夹下
        :param name:
        :return:
        '''
        global now_client
        # 设置当前用户名
        self.setNowClient(name)
        # print(now_client)
        open("{path}\client.txt".format(path=self.path), 'a')
        with open("{path}\client.txt".format(path=self.path), "rb") as isNone:  # 用文件保存所有用户名为列表
            reading = isNone.read()
            # now_client.add("x")
            now_client.add(name)
            x = pickle.dumps(now_client)
            if reading != b'':  # 将当前用户名添加于列表中
                y = pickle.loads(reading)
                y.add(name)
                y = pickle.dumps(y)
                with open("{path}\client.txt".format(path=self.path), "wb") as cover:
                    cover.write(y)
            else:
                with open("{path}\client.txt".format(path=self.path), "wb") as creat:
                    creat.write(x)

    def setNowClient(self, name):
        '''
            TODO
            将文件存放位置改为对应ip和port文件夹下
        :param name:
        :return:
        '''
        open(r"{path}\nowclient.txt".format(path=self.path), 'a')
        with open(r"{path}\nowclient.txt".format(path=self.path), "r") as isNone:  # 用文件保存当前用户名
            # print("setNowClient")
            reading = isNone.read()
            # print(reading)
            if reading == '':
                with open(r"{path}\nowclient.txt".format(path=self.path), "w") as nClient:
                    nClient.write(name)

    def existClients(self):
        '''
            TODO
            将文件存放位置改为对应ip和port文件夹下
        :param name:
        :return:
        '''
        # 获得label要显示的用户名
        with open(r"{path}\client.txt".format(path=self.path), "rb") as isNone:  # 用文件保存用户名
            reading = isNone.read()
            if reading != b'':
                names = pickle.loads(reading)
                return names


# 注册账号
class Sign_up():
    def __init__(self, window):
        self.window = window
        self.__usr_sign_up()

    def sign_to_Pyhon(self, nameArea, pswArea, pswConfirmArea):
        psw_get = pswArea.get()
        psw_confirm = pswConfirmArea.get()
        getNewName = nameArea.get()
        if psw_confirm != psw_get:
            tk.messagebox.showerror('对不起', '两次密码输入不一致！')
        elif psw_get == psw_confirm:
            dictReg = {getNewName: psw_confirm}
            x = pickle.dumps(dictReg)
            with open(r"E:\hyx\core\聊天软件的实现_v1.1\reg.txt", "rb") as isNone:  # 判断是否为空，不为空的话重新建立字典，代替原有的
                reading = isNone.read()
            if reading != b'':
                y = pickle.loads(reading)
                if getNewName in y.keys():
                    tk.messagebox.showerror('对不起', '此账号已经存在!')
                elif getNewName not in y.keys():
                    y[getNewName] = psw_confirm
                    y = pickle.dumps(y)
                    with open(r"E:\hyx\core\聊天软件的实现_v1.1\reg.txt", "bw") as cover:
                        cover.write(y)
                    tk.messagebox.showinfo('Welcome', '您已经注册成功！')
                    self.window_sign_up.destroy()
            else:
                with open(r"E:\hyx\core\聊天软件的实现_v1.1\reg.txt", "bw") as userReg:
                    userReg.write(x)
                tk.messagebox.showinfo('Welcome', '您已经注册成功！')
                self.window_sign_up.destroy()

    def __usr_sign_up(self):
        # 创建top窗口作为注册窗口
        self.window_sign_up = tk.Toplevel(self.window)
        self.window_sign_up.geometry('350x200')
        self.window_sign_up.title('注册')

        new_name = tk.StringVar()
        new_name.set('')
        tk.Label(self.window_sign_up, text='账号:').place(x=80, y=10)
        entry_new_name = tk.Entry(self.window_sign_up, textvariable=new_name)
        entry_new_name.place(x=150, y=10)

        new_pwd = tk.StringVar()
        tk.Label(self.window_sign_up, text='密码:').place(x=80, y=50)
        entry_usr_pwd = tk.Entry(self.window_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=150, y=50)

        new_pwd_confirm = tk.StringVar()
        tk.Label(self.window_sign_up, text='再次输入:').place(x=80, y=90)
        entry_usr_pwd_again = tk.Entry(self.window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_again.place(x=150, y=90)

        btn_again_sign_up = tk.Button(self.window_sign_up, text='注册',
                                      command=lambda: self.sign_to_Pyhon(new_name, new_pwd, new_pwd_confirm))
        btn_again_sign_up.place(x=160, y=130)


class watch():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('欢迎使用')

        a, b = self.__window_info()
        self.window.geometry("450x300+%d+%d" % (a, b))
        # 登陆界面的信息
        tk.Label(self.window, text="聊天软件的实现", font=("宋体", 32)).place(x=80, y=50)
        tk.Label(self.window, text="账号：").place(x=120, y=150)
        tk.Label(self.window, text="密码：").place(x=120, y=190)
        # 显示输入框
        var_usr_name = tk.StringVar()
        # 显示默认账号
        var_usr_name.set('')
        entry_usr_name = tk.Entry(self.window, textvariable=var_usr_name)
        entry_usr_name.place(x=190, y=150)
        var_usr_pwd = tk.StringVar()
        # 设置输入密码后显示*号
        entry_usr_pwd = tk.Entry(self.window, textvariable=var_usr_pwd, show='*')
        entry_usr_pwd.place(x=190, y=190)
        # 登陆和注册按钮
        btn_login = tk.Button(self.window, text="登陆", command=lambda: Login(self.window, var_usr_name, var_usr_pwd))
        btn_login.place(x=170, y=230)
        btn_sign_up = tk.Button(self.window, text="注册", command=lambda: Sign_up(self.window))
        btn_sign_up.place(x=270, y=230)

        self.window.mainloop()

    # 设置窗口居中
    def __window_info(self):
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws / 2) - 200
        y = (hs / 2) - 200
        print("%d,%d" % (ws, hs))
        return x, y


if __name__ == '__main__':
    watch()
