import threading, socket,chat_Tkinter,time

# 定义服务器信息
HOST = '192.168.11.206'
PORT = 10000
ADDRESS = (HOST, PORT)
BUFFER  = 1024

def core(textArea,showArea,nowClient):
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
    sender = threading.Thread(target=message_send, args=(client_socket,textArea,nowClient,))
    recevier = threading.Thread(target=message_recevie, args=(client_socket,showArea,))
    sender.start()
    recevier.start()
    return client_socket


def message_send(client_socket,textArea,nowClient):
    '''发送消息的函数'''
    msg = nowClient+"     " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ':\n'
    toSend = ''
    # exText:输入栏未输入的状态
    while True:
        try:
            text = textArea.get('0.0', 'end')
            # print(text=='\n')
            time.sleep(0.1)
            if text!='\n':
                # 有输入的情况下，循环读取
                toSend=text
            if text=='\n':
                # 点击过发送以后
                # 通过exText是否为空来判断是否点击了发送
                if toSend!='':
                    msg=msg+toSend+'\n'
                    print(msg)
                    client_socket.send(msg.encode("utf-8"))
                     # 清空toSend
                    toSend=''
        except Exception as e:
            print(e)
            break
        # txt_msgsend控件



def message_recevie(client_socket,showArea):
    '''接受消息的函数'''
    while True:
        info = client_socket.recv(BUFFER)
        info=info+"\n\n"
        showArea.insert("end", info.decode('utf-8'))
