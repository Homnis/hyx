import socket
import datetime


# 创建本地地址
Host=''
Port=9000
Address=(Host,Port)
Buffer=1024

# 创建TCP服务对象
tcp_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 绑定主机
tcp_server.bind(Address)

# 启动监听
tcp_server.listen(10)
# 此处listen的参数是指允许多少个客户端排队

while True:
    # 5. 等待客户端连接
    print("等待客户端连接========")
    client ,address= tcp_server.accept()
    print(client ,address)
    print(type(client))
    print("客户端{}连接成功".format(address))
    client.send("welcome".encode("utf-8"))

    # 6. 收发消息
    while True:
        info=client.recv(Buffer)
        try:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print("client客户端：{}".format(info.decode("uft-8")),now_time)
        except Exception as e:
            now_time = datetime.datetime.now().strftime('%Y-%m-%d')
            # print("不是utf-8")
            print("client客户端：{}".format(info.decode("gbk")),now_time)

        msg1 = input("input:")
        client.send(msg1.encode("utf-8"))
        print("已发送")

        if info == b'bye':
            print("客户端退出")
            client.close()
            break

