import pymysql
import time

conn = pymysql.connections.Connection(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'fenglovehuihui',
    database = 'peewee_test',
    charset = 'utf8',
    autocommit = False
)


conn.begin()
cur = conn.cursor()
cur.execute("update ttt set count=0 where count<10000")
time.sleep(30)
conn.commit()
#conn.rollback()
conn.close()
