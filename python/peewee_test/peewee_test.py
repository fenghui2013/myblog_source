import logging
from datetime import date
import time

from peewee import *

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
    is_relative = BooleanField()

class Pet(BaseModel):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()


db.connect()
#db.create_tables([Person, Pet])

herb = Person.select().where(Person.name == "Herb").get()
for pet in herb.pets:
    print(pet.name, pet.animal_type)

#bob = Person(name='Bob', birthday=date(1989, 4, 17))
#bob.save()
#
#
#foo = Person.create(name='Foo', birthday=date(1991, 1, 6))
#time.sleep(30)
#foo.name = 'Fu'
#foo.save()
#
#
#test = Person.create(name="test", birthday=date(2017, 1, 1))
#time.sleep(30)
#test.delete_instance()
#
#
#uncle_bob = Person.create(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
#grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
#herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
#
#
#bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
#herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
#herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
#herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')
#
#
#fu = Person.select().where(Person.name == 'Fu').get()
#print(fu.birthday)
#bob = Person.get(Person.name == 'Bob')
#print(bob.birthday)
#
#for person in Person.select():
#    print(person.name, person.birthday)
#
#
#for person in Person.select().order_by(Person.name):
#    print(person.name, person.birthday)
#
#
#for person in Person.select().order_by(Person.birthday.desc()):
#    print(person.name, person.birthday)
#
#
#for person in Person.select():
#    print(person.name, person.pets.count(), 'pets')
#    for pet in person.pets:
#        print('    ', pet.name, pet.animal_type)
#
#
#subquery = Pet.select(fn.COUNT(Pet.id)).where(Pet.owner == Person.id)
#query = (Person.select(Person, Pet, subquery.alias('pet_count')).join(Pet, JOIN.LEFT_OUTER).order_by(Person.name))
#
#for person in query.aggregate_rows():
#    print(person.name, person.pet_count, 'pets')
#    for pet in person.pets:
#        print('    ', pet.name, pet.animal_type)


db.close()
