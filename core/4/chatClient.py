import socket,threading,time,datetime,pickle

HOST = '192.168.11.206'
PORT = 10086  # 设置侦听端口
ADDRESS=(HOST,PORT)
BUFFER = 1024

class client():
    def __init__(self,address):
        self.address=address
        # 创建socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # print(self.client)
        self.client.connect(self.address)
        self.__users()
        # 监听接收的信息
        self.recv = threading.Thread(target=self.recvmsg)
        self.recv.start()
        print("连接成功")

    def __users(self):
        '''
        {用户名：密码}
        :return:
        '''
        while True:
            choice=int(input("请输入要进行的操作：1.注册，2.登录"))
            if choice==1:
                self.__reg()
            elif choice==2:
                isTrue=self.__login()
                if isTrue==True:
                    break


    def __reg(self):
        '''
        TODO 注册
        :return:
        '''
        name = input("请输入用户名：")
        psw = input("请输入密码：")
        dictReg = {name: psw}
        x = pickle.dumps(dictReg)
        with open(r"E:\hyx\core\4\reg.txt", "rb") as isNone:  # 判断是否为空，不为空的话重新建立字典，代替原有的
            reading = isNone.read()
        if reading != b'':
            y = pickle.loads(reading)
            y[name] = psw
            y = pickle.dumps(y)
            with open(r"E:\hyx\core\4\reg.txt", "bw") as cover:
                cover.write(y)
        else:
            with open(r"E:\hyx\core\4\reg.txt", "bw") as userReg:
                userReg.write(x)
        print("注册成功")

    def __login(self):
        '''
        TODO 登录
        :return:
        '''
        name = input("请输入用户名：")
        psw = input("请输入密码：")
        open(r"E:\hyx\core\4\reg.txt", 'a')
        with open(r"E:\hyx\core\4\reg.txt", "rb") as isNone:  # 判断是否为空，不为空的话重新建立字典，代替原有的
            reading = isNone.read()
            # print(reading)
            if reading != b'':
                with open(r"E:\hyx\core\4\reg.txt", "rb") as isTrue:
                    a = pickle.load(isTrue)
                    if a[name] == psw:
                        self.name=name
                        return True
                    else:
                        return False
            else:
                print("无数据")

    def recvmsg(self):
        # 接收消息，如果链接一直存在，则持续监听接收消息
        try:
            while self.client.connect_ex(self.address): # 功能与connect(address)相同，但是成功返回0，失败返回errno的值。
                info = self.client.recv(BUFFER)
                print(info.decode('utf8'))
                '''
                    如果想输出对应的用户名，需要从表中读取对应信息
                '''
        except Exception as e:
            print(e)

    def sendmsg(self):
        # 循环发送聊天消息，如果socket连接存在则一直循环，发送quit时关闭链接
        while self.client.connect_ex(self.address):
            data=input("发送：")
            msg="%s 说： %s" %(self.name,data)
            self.client.send(msg.encode('utf8'))
            # print('发送信息到%s：%s' % (self.address, data))
            # print(data[-3:3])
            if data[-3:3].upper() == "BYE":
                self.client.close()
                print("关闭客户端")
                break


if __name__ == '__main__':
    aClient=client(ADDRESS)
    aClient.sendmsg()