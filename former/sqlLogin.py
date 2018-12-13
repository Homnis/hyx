import pymysql


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
    while True:
        wanna = int(input("请选择要进行的操作：1.登陆 2.注册 3.退出"))
        if wanna == 3:
            return False
        elif wanna == 2:
            name = input("请输入用户名：")
            psw = input("请输入密码")
            newReg = reg(name, psw)
            print(1)
            isExist = newReg.getOne()
            print(isExist)
            if isExist == None:
                print(3)
                newReg.insert()
            else:
                print("用户名已存在")
        elif wanna == 1:
            name = input("请输入用户名：")
            psw = input("请输入密码")
            newLogin = login(name, psw)
            iPsw = newLogin.getPsw()[0]
            if iPsw == psw:
                print("登陆成功")
                print(newLogin.getOne("select * from user where name=%s", (name,)))
            else:
                print("密码错误")

        else:
            print("输入有误。")


Main()
