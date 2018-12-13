import socket

# 设置地址和缓冲区
Host=""
Port=10000
Address=(Host,Port)
Buffer=1024

# 创建对象并绑定主机
udp_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server.bind(Address)
print("waiting for client.....")
# 交互
while True:
    msg, addr=udp_server.recvfrom(Buffer)
    print("client:",addr)
    print("says:",msg.decode("utf-8"))
    udp_server.sendto("this is server".encode("utf-8"),addr)