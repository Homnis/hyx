import pymysql


class mySqlHelper():
    def __init__(self, host, port, db, user, password, charset='utf8'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.psw = password
        self.charset = charset

    def connect(self):
        self.con = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, password=self.psw,
                                   charset=self.charset)
        self.cursor = self.con.cursor()

    def close(self):
        self.cursor.close()
        self.con.close()

    def getOne(self, queryStr, args=None):
        try:
            row = self.cursor.execute(queryStr, args)
            if row > 0:
                return self.cursor.fetchone()
            else:
                return None
        except Exception as e:
            print(e)
        finally:
            self.close()

    def getAll(self,params):
        result = None
        try:
            self.connect()
            self.cursor.execute(params)
            result = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return result

    def insert(self,params):
        row = None
        try:
            self.connect()
            row = self.cursor.execute(params)
            self.con.commit()
            self.close()
        except Exception as e:
            print(e)
        return row

    def update(self,params):
        row = None
        try:
            self.connect()
            row = self.cursor.execute(params)
            self.con.commit()
            self.close()
        except Exception as e:
            print(e)
        return row

    def delete(self,params):
        row = None
        try:
            self.connect()
            row = self.cursor.execute(params)
            self.con.commit()
            self.close()
        except Exception as e:
            print(e)
        return row
