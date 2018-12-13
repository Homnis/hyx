import socket,threading,time,datetime,os,pickle


HOST = '192.168.11.206'
PORT = 10086  # 设置侦听端口
ADDRESS=(HOST,PORT)
BUFFER = 1024

class server():
    def __init__(self,address):
        self.address=address
        # 所有监听的客户端
        self.clients = {}
        self.thrs = {}
        self.stops = []

        # 设置运行状态
        self.closeClient=False
        self.closeServer=False

    def serve(self):
        self.__connect()
        # self.__users()
        self.__listenClient()

    def __connect(self):
        try:
            self.serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # TCP
            self.serverSocket.bind(self.address)
            self.serverSocket.listen(5)
        except Exception as e:
            print(e)


    def __listenClient(self):
        while 1:
            print(u'等待接入，侦听端口:%d' % (PORT))
            self.tcpClientSock, self.addr = self.serverSocket.accept()
            print(u'接受连接，客户端地址：', self.addr)
            address = self.addr
            # 将建立的client socket链接放到列表self.clients中
            self.clients[address] = self.tcpClientSock
            # 分别将每个建立的链接放入进程中，接收且分发消息
            self.thrs[address] = threading.Thread(args=(address,),target=self.read)
            # print(self.thrs[address])
            self.thrs[address].start()
            time.sleep(0.5)

    def read(self,address):
        # print(address)
        # print(1)
        if address not in self.clients:
            print("地址不存在")
        # 得到发送消息的client socket
        client = self.clients[address]
        # print(client)
        # receiveInfo = client.recv(BUFFER)
        # print(receiveInfo)
        while True:
            # print(1)
            try:
                # print(2)
                # 获取到消息内容
                receiveInfo = client.recv(BUFFER)
                # print(3)
                # print(receiveInfo)
            except Exception as e:
                print(e)
                break
            # python3使用bytes，所以要进行编码
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            s = receiveInfo.decode('utf8')
            # 将获得的消息分发给链接中的client socket
            for k in self.clients:
                self.clients[k].send(s.encode('utf8'))
                print(k)
            print([now_time], address,':', receiveInfo.decode('utf8'))
            # 如果输入bye(忽略大小写),则程序退出
            # 在客户端程序中执行close方法，在服务器端从相应列表中删除
            isStop = (receiveInfo.decode('utf8').upper() == "BYE")
            if isStop==True:
                print("正在退出客户端")
                self.__closeClient(address)
                print("客户端已退出")
                break


    def __closeClient(self,address):
        try:
            # 在在线客户端中删除client，下线client中加入对应账户
            client = self.clients.pop(address)
            self.stops.append(address)
            client.close()
            for k in self.clients:
                self.clients[k].send(str(address) + "已经离开了")
        except Exception as e:
            print(e)
        print(str(address),'已经退出')


if __name__ == '__main__':
    chatServer=server(address=ADDRESS)
    chatServer.serve()








