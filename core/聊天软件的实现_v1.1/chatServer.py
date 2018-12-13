import asynchat, asyncore, socket,threading,shutil

class Server(asyncore.dispatcher):

    def __init__(self, host,port):
        asyncore.dispatcher.__init__(self)
        # 建立套接字对象
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        #  设置地址可重用
        self.set_reuse_addr()
        # print((host, port))
        self.bind((host,port))
        self.listen(5)
        self.sessions = []
        # print(1)
    # Server类的handle_accept方法，接收用户接入请求，为每个用户创建一个socket对象，表示用户。并为每一个socket对象调用ChatSession类
    # 创建实例。
    # 重写处理客户端连接的方法
    def handle_accept(self):
        conn, addr = self.accept()
        # print(2)
        conn.send("已连接".encode('utf-8'))
        # 将新用户添加到对话列表
        a=ChatSession(self, conn)
        # print("session")
        self.sessions.append(a)
        # print(self.sessions)
        # print(3)

    def broadcast(self, line):
        # '向所有的用户发送指定消息'
        for session in self.sessions:
            session.push(line)
        # print("did")


class ChatSession(asynchat.async_chat):
    def __init__(self, server,sock):
        asynchat.async_chat.__init__(self, sock)
        self.server = server
        # 设置终止符
        self.set_terminator("\n".encode('utf-8'))
        self.data = []
        # print("x")
        # self.send("欢迎进入".encode('utf-8'))
        self.client_name = ''
        # print(4)

    # 重写接收方法
    def collect_incoming_data(self, data):
        # 将接收的消息存入data列表中
        # print("y")
        self.data.append(data.decode('utf-8'))
        # print(self.data)
        self.server.broadcast(data)

    # 重写发现终止符后要运行的方法
    def found_terminator(self):
        # 转存data中的数据为一行以供显示
        # print("a")
        line = ''.join(self.data)
        self.data = []
        # print(line)
        # try:

class start():
    def __init__(self,address,path):
        self.path=path
        # print(address)
        host = str(address[0])
        port = int(address[1])
        # print(type(host))
        # print(type(port))
        Server(host,port)
        asyncore.loop()

    def __del__(self):
        shutil.rmtree(self.path)
# if __name__ == '__main__':
#
#     print("server已调用")
#     s = Server(HOST,PORT)
#     # loop=threading.Thread(target=asyncore.loop(),)
#     # loop.start()
#     s.close()
#     with open(r"E:\hyx\core\聊天软件的实现_v1.1\server.txt", "w") as cover:
#         cover.truncate()
#     # loop()一直运行 使主页面无法继续
#     # 主程序中使用独立线程解决