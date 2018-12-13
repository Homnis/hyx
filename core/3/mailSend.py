from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr,formataddr
from email import encoders
from logging import debug,info,warning,error,basicConfig,DEBUG


class MailSender():
    '''
        创建发送者对象
    '''
    # 发件人
    _from=None
    # 附件列表
    _attachments=[]
    def __init__(self,server,port,userName,psw):
        '''

        :param server: 邮箱服务器
        :param port: 使用端口
        :param userName: 帐号
        :param psw: 密码
        '''
        basicConfig(level=DEBUG,format='''
                        %(asctime)s - %(levelname)s:%(message)s
                        ,\n filename: %(filename)s''')

        # 连接服务器
        info("连接指定smtp服务器..{}".format(server))
        self.server=SMTP_SSL(server,port)
        info("服务器连接成功")
        # 登录服务器
        self.__login(userName,psw)

    def __login(self,user,psw):
        debug("设置发件人信息")
        self._from=user
        info("开始使用指定账号%s登录服务器" %(user))
        try:
            self.server.login(user,psw)
        except:
            info("服务器登录失败")
        info("服务器登陆成功")

    def add_attachment(self,file):
        '''
        添加附件
        :param file:文件路径
        :return:None
        '''
        info("邮件中添加附件%s" %(file))
        with open(file,'rb') as f:
            debug("封装附件对象")
            attach=MIMEBase('application','octet-stream')
            debug(attach)
            attach.set_payload(f.read())
            debug(attach)
            attach.add_header(
                'Content-Disposition',
                'attachment',
                filename=('utf-8','',f.name)
            )
            debug("开始编码")
            encoders.encode_base64(attach)
            debug("编码完成")
        self._attachments.append(attach)
        info("附件%s添加完成" %(file))

    def send(self,subject,to_addr,content):
        info("开始封装邮件")
        msg=MIMEMultipart()
        debug("开始添加文本邮件内容")
        contents=MIMEText(content,'html',_charset='utf-8')
        debug("开始设置邮件标题等")
        msg['Subject']=subject
        msg['From']=self._from
        msg['To']=to_addr
        info("添加附件")
        for i in self._attachments:
            msg.attach(i)
        info("添加文本内容")
        msg.attach(contents)
        try:
            info("开始发送")
            self.server.sendmail(self._from,to_addr,msg.as_string())
            info("邮件发送成功")
            return True
        except Exception as e:
            info("发送失败",e)
            return False

    def close(self):
        self.server.quit()
        info("客户端退出")

if __name__ == '__main__':

    # 创建对象
    mail=MailSender(
        'smtp.qq.com',
        465,
        '675868749@qq.com',
        'sznwymhsganvbfbc'
    )
    # 添加附件
    mail.add_attachment(r'E:\ftp_test\NetAssist.exe')
    msg='<h1>发送的测试邮件<h1>'
    mail.send('测试邮件测试邮件',"675868749@qq.com",msg)
    mail.close()
