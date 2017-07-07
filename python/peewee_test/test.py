import logging
from datetime import date
import time

from peewee import MySQLDatabase, Model, CharField, DateField, BooleanField, IntegerField

logger = logging.getLogger("peewee")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

db = MySQLDatabase('peewee_test', host='192.168.99.110', port=3306, user='root', passwd='Fenglovehuihui!@#123', charset='utf8')

class BaseModel(Model):
    class Meta:
        database = db


class Person(BaseModel):
    name = CharField(max_length=10, null=False, index=True)
    birthday = DateField(null=False, default=None)


db.connect()
#db.create_tables([Person])


#bob = Person(name='Bob', birthday=date(1989, 4, 17))
#bob.save()


#foo = Person.create(name='Foo', birthday=date(1991, 1, 6))
#time.sleep(30)
#foo.name = 'Fu'
#foo.save()


#test = Person.create(name="test", birthday=date(2017, 1, 1))
#time.sleep(30)
#test.delete_instance()


fu = Person.select().where(Person.name == 'Fu').get()
print(fu.birthday)
bob = Person.get(Person.name == 'Bob')
print(bob.birthday)

for person in Person.select():
    print(person.name, person.birthday)


for person in Person.select().order_by(Person.name):
    print(person.name, person.birthday)


for person in Person.select().order_by(Person.birthday.desc()):
    print(person.name, person.birthday)
