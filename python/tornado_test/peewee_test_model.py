from peewee import *

database = MySQLDatabase('peewee_test', **{'port': 3306, 'user': 'root', 'host': '127.0.0.1', 'password': 'fenglovehuihui'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Ttt(BaseModel):
    count = IntegerField(null=True)

    class Meta:
        db_table = 'ttt'
        primary_key = False

