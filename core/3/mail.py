import email,smtplib
from email.mime.text import MIMEText


# 发送人信息
SMTP_SERVER='smtp.qq.com'
userName='675868749@qq.com'
psw='sznwymhsganvbfbc' # 码没设置


#定义双方邮箱
sender=userName
receiver='yanxin2258@163.com'

# 定义邮件内容
msg=MIMEText("邮件测试：hello world","plain","utf-8")
# 定义收件人、发件人和邮件主题，如果不定义可能会引发554垃圾邮件的检查错误
msg['from']=sender
msg['to']=receiver
msg['subject']='测试邮件 求求你别说是垃圾邮件'

# 连接服务器
server= smtplib.SMTP_SSL(SMTP_SERVER,465)
# 设置信息展示级别
server.set_debuglevel(1)
# 登录服务器
server.login(userName,psw)
#发送
server.sendmail(from_addr=sender,to_addrs=[receiver],msg=msg.as_string())

#退出并关闭客户端
server.quit()
print("邮件发送结束。")