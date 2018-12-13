import threading, socket

# 定义服务器信息
HOST = '192.168.11.206'
PORT = 10000
ADDRESS = (HOST, PORT)
BUFFER  = 1024

def core():
    '''主函数：负责创建套接字、连接指定主机'''
    # 创建一个客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务器
    client_socket.connect(ADDRESS)
    # 接受服务器提示信息
    msg = client_socket.recv(BUFFER).decode("utf-8") + ":"
    # 发送昵称给服务器
    # client_socket.send(name.encode("utf-8"))

    # 和服务器之间消息交互
    sender = threading.Thread(target=message_send, args=(client_socket,))
    recevier = threading.Thread(target=message_recevie, args=(client_socket,))
    sender.start()
    recevier.start()
    return client_socket


def message_send(client_socket):
    '''发送消息的函数'''
    while True:
        msg = input("发送消息：")

        client_socket.send(msg.encode("utf-8"))


def message_recevie(client_socket):
    '''接受消息的函数'''
    while True:
        info = client_socket.recv(BUFFER)
        print('\n',"someone said:",info.decode("utf-8"),'\n')
