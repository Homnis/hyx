import pymysql
import hashlib
from redisHelper import *

class login():
    # 登陆
    def __init__(self, name, psw):
        self.name = name
        self.psw = psw
        self.host = "localhost"
        self.port = 3306
        self.db = "user"
        self.user = "root"
        self.password = "123456"
        self.charset = "utf8"

    def connect(self):
        self.con = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, password=self.password,
                                   charset=self.charset)
        self.cursor = self.con.cursor()

    def close(self):
        try:
            self.cursor.close()
            self.con.close()
        except Exception as e:
            print(e)
            self.con.rollback()

    def getPsw(self):
        result = None
        try:
            self.connect()
            self.cursor.execute("select password from user where name=%s", (self.name,))
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
            self.con.rollback()
        return result

    def getOne(self, param, args=None):
        result = None
        try:
            self.connect()
            self.cursor.execute(param, args)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
            self.con.rollback()
        return result


class reg():
    # 注册
    def __init__(self, name, psw):
        self.name = name
        self.psw = psw
        self.host = "localhost"
        self.port = 3306
        self.db = "user"
        self.user = "root"
        self.password = "123456"
        self.charset = "utf8"

    def connect(self):
        self.con = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, password=self.password,
                                   charset=self.charset)
        self.cursor = self.con.cursor()

    def close(self):
        try:
            self.cursor.close()
            self.con.close()
        except Exception as e:
            print(e)
            self.con.rollback()

    def insert(self):
        row = None
        try:
            self.connect()
            row = self.cursor.execute(
                'INSERT INTO `user`.`user` (`name`, `password`) VALUES (%s,%s);', (self.name, self.psw))
            self.con.commit()
            self.close()
        except Exception as e:
            print(e)
            self.con.rollback()
        return row

    def getOne(self):
        result = None
        try:
            self.connect()
            self.cursor.execute("select * from user where name=%s", (self.name,))
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
            self.con.rollback()
        return result


def Main():
    name=input("请输入用户名：")
    psw=input("请输入密码：")
    # 加密密码
    sha1=hashlib.sha1()
    sha1.update(psw.encode("utf-8"))
    shaPsw=sha1.hexdigest()
    print(shaPsw)

    try:
        redis=redisHelper()
        if redis.getRedis('userName')==name:
            print('ok')
        else:
            newSql=login(name=name,psw=psw)
            newPsw=newSql.getPsw()
            if newPsw==None:
                print("用户名不存在")
            elif newPsw[0]==shaPsw:
                redis.set('userName',name)
                print("redis中不存在信息，已从mysql中读取，登陆成功")
            else:
                print("密码错误")
    except Exception as e:
        print(e)


Main()