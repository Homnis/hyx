'''
AUTHOR: DAMU 牟文斌
VERSION: V1.0.000
DESC: 端对端聊天服务端模块
'''
# 导入依赖的模块
import threading, socket

# 定义服务器信息
HOST = ''
PORT = 8888
ADDRESS = (HOST, PORT)
# 消息缓冲
BUFFER = 1024

# 定义字典， 存储每个接入的客户端信息
# customers = {'小王': (socket, address)}
customers = dict()


def engine():
    '''启动服务器，绑定主机，监听连接'''
    # 服务端套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定主机
    server_socket.bind(ADDRESS)
    # 监听连接
    server_socket.listen(128)
    # 等待客户端连接
    while True:
        c_socket, address = server_socket.accept()
        print("客户端{}已经连接到服务器".format(address))

        # 发送消息提示输入昵称
        c_socket.send("\n请输入您的昵称：".encode("utf-8"))

        # 接受消息存储客户端
        name = c_socket.recv(BUFFER).decode("utf-8")
        customers[name] = (c_socket, address)

        # 启动一个独立的交互线程~可该客户端进行消息传输
        customer = threading.Thread(target=message_transfer, args=(c_socket,), name=name)
        customer.start()


def message_transfer(c_socket):
    '''消息转发'''
    # 消息接受
    msg = c_socket.recv(BUFFER).decode('utf-8')
    # 消息拆分【昵称-消息内容】
    nickname = msg.split('-')[0]
    # 得到目标socket
    target_socket = customers[nickname][0]
    # 给目标用户发送消息
    msg = threading.current_thread().name + ":" + msg.split('-')[1]
    target_socket.send(msg.encode('utf-8'))


if __name__ == "__main__":
    engine()
