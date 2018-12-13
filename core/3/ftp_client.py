import ftplib,socket


'''
    ftp=FTP() #设置变量
    ftp.set_debuglevel(2) #打开调试级别2，显示详细信息
    ftp.connect("IP","port") #连接的ftp sever和端口
    ftp.login("user","password")#连接的用户名，密码
    print ftp.getwelcome() #打印出欢迎信息
    ftp.cmd("xxx/xxx") #更改远程目录
    bufsize=1024 #设置的缓冲区大小
    filename="filename.txt" #需要下载的文件
    file_handle=open(filename,"wb").write #以写模式在本地打开文件
    ftp.retrbinaly("RETR filename.txt",file_handle,bufsize) #接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0) #关闭调试模式
    ftp.quit #退出ftpftp相关命令操作
    ftp.cwd(pathname) #设置FTP当前操作的路径
    ftp.dir() #显示目录下文件信息
    ftp.nlst() #获取目录下的文件
    ftp.mkd(pathname) #新建远程目录
    ftp.pwd() #返回当前所在位置
    ftp.rmd(dirname) #删除远程目录
    ftp.delete(filename) #删除远程文件
    ftp.rename(fromname, toname)#将fromname修改名称为toname。
    ftp.storbinaly("STOR filename.txt",file_handel,bufsize) #上传目标文件
    ftp.retrbinary("RETR filename.txt",file_handel,bufsize)#下载FTP文件

'''

# 地址
Host="192.168.11.206"
Dirs="/"
File='./NetAssist.exe'


class FtpClient:
    def __init__(self,host,userName,psw):
        '''

        :param host: 主机地址
        :param userName: 帐号
        :param psw: 密码
        '''
        self.host=host
        self.userName=userName
        self.psw=psw

    def ftp_download(self,dir,file):
        '''

        :param dir: 路径
        :param file: 文件
        :return: 无返回值
        '''
        self.directory=dir
        self.file=file

        self.__ftpConnect()
        self.__ftpLogin()
        self.__ftpChangeDirectory()
        # TODO 查看当前文件夹下所有文件 函数  调用展示
        self.__check_file()
        # self.__ftpDownload()
        self.__ftpQuit()

    def __check_file(self):
        '''查看当前目录中的所有文件列表'''
        pass


    def __ftpConnect(self):
        try:
            # print(1)
            self.ftp=ftplib.FTP(self.host)
            # print(2)
        except (socket.error,socket.gaierror) as e:
            print("目标主机不可访问：",self.host)
        else:
            print("%s连接成功",self.host)

    def __ftpLogin(self):
        try:
            self.ftp.login()
        except ftplib.error_perm as e: # permission
            print("请输入帐号密码")
            try:
                self.ftp.login(user=self.userName,passwd=self.psw)
            except:
                print("帐号密码错误")
            else:
                print("登陆成功")

    def __ftpChangeDirectory(self):
        try:
            self.ftp.cwd(self.directory)
        except ftplib.error_perm as e:
            print("路径修改失败，没有权限")
        else:
            print("路径修改成功,当前路径为：",self.directory)

    def __ftpDownload(self):
        try:
            with open(self.file,'wb') as fp:
                self.ftp.retrbinary("RETR  %s" %(self.file),fp.write) # 应该是file和path出错了 但是没找到具体错误
                '''
                    cmd: A RETR command.
                    callback: A single parameter callable to be called on each
                              block of data read.
                '''
                # print(1)

        except ftplib.error_perm as e:
            print("文件下载失败",e)
        else:
            print("%s下载完成" %(self.file))

    def __ftpQuit(self):
        self.ftp.quit()
        print('程序退出')


if __name__ == '__main__':
    ftp=FtpClient(Host,'hyx','19951218xx')
    ftp.ftp_download(Dirs,File)
