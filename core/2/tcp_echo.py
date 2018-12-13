import socket
import datetime


def client():
    # 初始化客户端
    print("初始化客户端")
    Host="localhost"
    Port=9000
    Address=(Host,Port)
    Buffer=1024

    # 创建TCP服务端程序
    tcp_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 连接主机
    tcp_client.connect(Address)

    while True:
        info = tcp_client.recv(Buffer)
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print("server:",info.decode("utf-8"),now_time)
        msg=input("input:")
        tcp_client.send(msg.encode("utf-8"))
        print("已发送")
        if info.decode("utf-8").lower()=="bye":
            print("结束")
            tcp_client.close()
            break

client()