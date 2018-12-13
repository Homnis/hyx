import tkinter as tk
from tkinter import messagebox
import pickle, runpy, threading,chat_Tkinter

now_client = set()


# 设置窗口居中
def window_info():
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d,%d" % (ws, hs))
    return x, y


# 设置登陆窗口属性


# 当前用户列表

def startServer():
    open(r"E:\hyx\core\聊天软件的实现_v1.0\server.txt", 'a')
    with open(r"E:\hyx\core\聊天软件的实现_v1.0\server.txt", "rb") as isNone:  # 通过server文件是否为空来判断服务端是否已在运行
        reading = isNone.read()
        # print(reading)
        if reading == b'':
            with open(r"E:\hyx\core\聊天软件的实现_v1.0\server.txt", "w") as f:
                f.write("did")
            runpy.run_path('chatServer.py', run_name='__main__')
        else:
            print("已开启过服务端")


# 登陆函数
def usr_login():
    # 获取输入的账号密码
    name = var_usr_name.get()
    psw = var_usr_pwd.get()
    open(r"E:\hyx\core\聊天软件的实现_v1.0\reg.txt", 'a')
    with open(r"E:\hyx\core\聊天软件的实现_v1.0\reg.txt", "rb") as isNone:  # 判断是否为空，不为空的话重新建立字典，代替原有的
        reading = isNone.read()
        # print(reading)
        if reading != b'':
            with open(r"E:\hyx\core\聊天软件的实现_v1.0\reg.txt", "rb") as isTrue:
                a = pickle.load(isTrue)
                if name in a:
                    if a[name] == psw:
                        tk.messagebox.showinfo(title='Welcome', message='Welcome,' + name)
                        # print(type(name))
                        print(name)
                        createName(name)
                        window.destroy()
                        startServe = threading.Thread(target=startServer, )
                        startServe.start()
                        runpy.run_path('chat_Tkinter.py', run_name='__main__')
                    else:
                        tk.messagebox.showerror('对不起', '用户名或密码错误!')
                else:
                    tk.messagebox.showerror('对不起', '不存在该用户!')
        else:
            print("无数据")


def createName(name):
    global now_client
    setNowClient(name)
    # print(now_client)
    open(r"E:\hyx\core\聊天软件的实现_v1.0\client.txt", 'a')
    with open(r"E:\hyx\core\聊天软件的实现_v1.0\client.txt", "rb") as isNone:  # 用文件保存用户名为列表
        reading = isNone.read()
        # now_client.add("x")
        now_client.add(name)
        x = pickle.dumps(now_client)
        if reading != b'':
            y = pickle.loads(reading)
            y.add(name)
            y = pickle.dumps(y)
            with open(r"E:\hyx\core\聊天软件的实现_v1.0\client.txt", "wb") as cover:
                cover.write(y)
        else:
            with open(r"E:\hyx\core\聊天软件的实现_v1.0\client.txt", "wb") as creat:
                creat.write(x)


def setNowClient(name):
    open(r"E:\hyx\core\聊天软件的实现_v1.0\nowClient.txt", 'a')
    with open(r"E:\hyx\core\聊天软件的实现_v1.0\nowClient.txt", "r") as isNone:  # 用文件保存用户名为列表
        reading = isNone.read()
        # print(reading)
        if reading == '':
            with open(r"E:\hyx\core\聊天软件的实现_v1.0\nowClient.txt", "w") as nClient:
                nClient.write(name)
# 注册账号
def usr_sign_up():
    def sign_to_Pyhon():
        psw_get = new_pwd.get()
        psw_confirm = new_pwd_confirm.get()
        getNewName = new_name.get()
        if psw_confirm != psw_get:
            tk.messagebox.showerror('对不起', '两次密码输入不一致！')
        elif psw_get == psw_confirm:
            dictReg = {getNewName: psw_confirm}
            x = pickle.dumps(dictReg)
            with open(r"E:\hyx\core\聊天软件的实现_v1.0\reg.txt", "rb") as isNone:  # 判断是否为空，不为空的话重新建立字典，代替原有的
                reading = isNone.read()
            if reading != b'':
                y = pickle.loads(reading)
                if getNewName in y.keys():
                    tk.messagebox.showerror('对不起', '此账号已经存在!')
                elif getNewName not in y.keys():
                    y[getNewName] = psw_confirm
                    y = pickle.dumps(y)
                    with open(r"E:\hyx\core\聊天软件的实现_v1.0\reg.txt", "bw") as cover:
                        cover.write(y)
                    tk.messagebox.showinfo('Welcome', '您已经注册成功！')
                    window_sign_up.destroy()
            else:
                with open(r"E:\hyx\core\聊天软件的实现_v1.0\reg.txt", "bw") as userReg:
                    userReg.write(x)
                tk.messagebox.showinfo('Welcome', '您已经注册成功！')
                window_sign_up.destroy()

    # 创建top窗口作为注册窗口
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')

    new_name = tk.StringVar()
    new_name.set('')
    tk.Label(window_sign_up, text='账号:').place(x=80, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='密码:').place(x=80, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='再次输入:').place(x=80, y=90)
    entry_usr_pwd_again = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_again.place(x=150, y=90)

    btn_again_sign_up = tk.Button(window_sign_up, text='注册', command=sign_to_Pyhon)
    btn_again_sign_up.place(x=160, y=130)


if __name__ == '__main__':
    window = tk.Tk()
    window.title('欢迎使用')
    a, b = window_info()
    window.geometry("450x300+%d+%d" % (a, b))

    # 登陆界面的信息
    tk.Label(window, text="聊天软件的实现", font=("宋体", 32)).place(x=80, y=50)
    tk.Label(window, text="账号：").place(x=120, y=150)
    tk.Label(window, text="密码：").place(x=120, y=190)
    # 显示输入框
    var_usr_name = tk.StringVar()
    # 显示默认账号
    var_usr_name.set('')
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
    entry_usr_name.place(x=190, y=150)
    var_usr_pwd = tk.StringVar()
    # 设置输入密码后显示*号
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
    entry_usr_pwd.place(x=190, y=190)
    # 登陆和注册按钮
    btn_login = tk.Button(window, text="登陆", command=usr_login)
    btn_login.place(x=170, y=230)
    btn_sign_up = tk.Button(window, text="注册", command=usr_sign_up)
    btn_sign_up.place(x=270, y=230)

    window.mainloop()
