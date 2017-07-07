import time
import logging

import tornado
import tornado.web
import tornado.ioloop

from peewee import *
from playhouse.pool import PooledMySQLDatabase
from peewee_test_model import Ttt


logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db = MySQLDatabase(
    'peewee_test',
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='fenglovehuihui',
    charset='utf8',
    autocommit=False
)
db.set_autocommit(False)
#db = PooledMySQLDatabase(
#    'peewee_test',
#    max_connections=4,
#    stale_timeout=300,
#    host='127.0.0.1',
#    port=3306,
#    user='root',
#    passwd='fenglovehuihui',
#    charset='utf8',
#    autocommit=False
#)

#class PeeweeRequestHandler(tornado.web.RequestHandler):
#    def prepare(self):
#        print('db connection connect')
#        db.connect()
#        return super(PeeweeRequestHandler, self).prepare()
#
#    def on_finish(self):
#        if not db.is_closed():
#            print('db connection close')
#            db.close()
#        return super(PeeweeRequestHandler, self).on_finish()
#
#class MainHandler(PeeweeRequestHandler):
#    def get(self):
#        #time.sleep(30)
#        self.write("hello world")
count = 0

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global count
        #time.sleep(30)
        #with db.atomic():
        with db.transaction() as txn:
            #Ttt.create(count=count)
            Ttt.update(count=90).where(Ttt.count < 10000).execute()
            time.sleep(10)
            txn.rollback()
        count += 1
        self.write("hello world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])

def main():
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
