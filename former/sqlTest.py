from former.mySqlHelper import *

print(pymysql)
# 创建连接
try:
    con = pymysql.connect(host="localhost", port=3306, user="root", password="123456", database="shopping")
    print(con)
    # 创建游标对象
    cursor = con.cursor(pymysql.cursors.DictCursor)
    print(cursor)
    # 操作数据库
    cursor.execute("select * from goods where id=2")
    # 获取返回值
    result = cursor.fetchall()
    print(result, 1)
    newSql = mySqlHelper(host="localhost", port=3306, user="root", password="123456", db="shopping")
    a = newSql.getOne("select name,place from goods where id=%s" % (15))
    print(a)
    # con.commit()

except Exception as e:
    print(e)
finally:
    print(1)
