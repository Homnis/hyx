import socket


# 设置地址和缓冲区
Host="localhost"
Port=10000
Address=(Host,Port)
Buffer=1024

# 创建对象
udp_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 交互
while True:
    msg=input("请输入要发送的消息内容：")
    udp_client.sendto(msg.encode("utf-8"),Address)
    if msg=='bye':
        udp_client.close()
        break
    info, addr=udp_client.recvfrom(Buffer)

    print("server says:",info.decode("utf-8"))