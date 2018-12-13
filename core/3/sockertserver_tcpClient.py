import socket


# 设置地址和缓冲区
Host="localhost"
Port=10001
Address=(Host,Port)
Buffer=1024

while True:
    tcp_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_client.connect(Address)
    print(tcp_client)
    msg=input("请输入信息：")
    tcp_client.send(msg.encode("utf-8"))
    if msg=="bye":
        tcp_client.close()
        break
    info=tcp_client.recv(Buffer)
    print(info.decode("utf-8"))