import socketserver


# 设置地址和缓冲区
Host=""
Port=10001
Address=(Host,Port)
Buffer=1024

class myRequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        print("客户端%s已连接。" %str(self.client_address))
        msg=self.request.recv(Buffer)
        # print("客户端%s发来信息：%s" %(str(self.client_address),msg.decode("utf-8")))
        toSend="客户端%s发来信息：%s" %(str(self.client_address),msg.decode("utf-8"))
        print(toSend)
        # self.request.sendall(toSend.encode("utf-8"))


if __name__ == '__main__':
    tcp_server=socketserver.TCPServer(Address,myRequestHandler)
    print("waiting.....")
    tcp_server.serve_forever()