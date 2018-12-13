import os

ip = "123"
port = 456
path="E:\hyx\core\聊天软件的实现_v1.1\{ip}\{port}".format(ip=ip, port=str(port))
print(os.path.exists(path) is True)
path=r"{path}\nowclient.txt".format(path="E:\hyx\core\聊天软件的实现_v1.1")
print(os.path.exists(path) is True)