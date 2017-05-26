class OperatorOverloadTest(object):
    def __init__(self, val_l, val_s, val_i):
        self.val_l = val_l
        self.val_s = val_s
        self.val_i = val_i
        self._index = 0
        self._len = len(self.val_l)

    def __sub__(self, other):
        #return OperatorOverloadTest(self.val_l, self.val_i-other)
        self.val_i = self.val_i - other
        return self

    def __getitem__(self, index):
        print "__getitem__", index,
        return self.val_l[index]

    def __setitem__(self, index, data):
        self.val_l[index] = data

    # single active iteration
    #def __iter__(self):
    #    print("__iter__")
    #    self._index = 0
    #    return self

    #def next(self):
    #    if self._index == self._len:
    #        raise StopIteration
    #    temp = self.val_l[self._index]
    #    self._index += 1
    #    return temp

    # many active iterations
    def __iter__(self):
        print("__iter__")
        return OperatorOverloadTest.MyIterator(self.val_l)

    class MyIterator(object):
        def __init__(self, wrapped):
            self.wrapped = wrapped
            self._index = 0
            self._len = len(self.wrapped)

        def next(self):
            if self._index == self._len:
                raise StopIteration
            temp = self.wrapped[self._index]
            self._index += 1
            return temp

    def __contains__(self, x):
        print("__contains__")
        return (x in self.val_l)

    #def __getattr__(self, name):
    #    print("__getattr__:%s" % name)
    #    return "undefined"

    def __setattr__(self, name, value):
        print("__setattr__:%s %s" % (name, value))
        self.__dict__[name] = value


    #def __getattribute__(self, name):
    #    print("__getattribute__:%s" % name)
    #    if name in self.__dict__
    #    return getattr(self, name)

    def __str__(self):
        content = ""
        #for i in range(26):
        #    content += (self.val_l[i]+", ")
        for temp in self:
            content += (temp+", ")
        return content

s = "abcdefghijklmnopqrstuvwxyz"
l = [temp for temp in s]
oot = OperatorOverloadTest(l, s, 100)

print("----__sub__----")
oot = oot - 10
print(oot.val_i)
print("----__getitem__:index----")
print(oot[3])
print(oot)
print("----__getitem__:slice----")
print(oot[7:19])
print("----__setitem__:index----")
oot[0] = "@"
print(oot[0])
#oot[1:5] = ['#', '#', '#', '#', '#']
oot[1:5] = '####'
print(oot)


#for temp1 in oot:
#    for temp2 in oot:
#        print temp1+temp2,
print("----__contains__----")
print("x" in oot)



print("----__setattr__----")




class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'
        #self.name = 'Tom'

t2 = Test2()


class NewProps(object):
    def get_age(self):
        return 40

    age = property(get_age, None, None, None) # get set del docs

x = NewProps()
print(x.age)
x.name = "xxx"
print(x.name)


print("-----------property---------------")
class Person(object):
    def __init__(self, name):
        self._name = name

    def getName(self):
        print("getName")
        return self._name

    def setName(self, value):
        print("setName")
        self._name = value

    def delName(self):
        print("delName")
        del self._name

    name = property(getName, setName, delName, None)

person = Person("xxx")
print(person.name)
person.name = "wang"
print(person.name)
del person.name

person.name = "xxxx"
print(person.name)



print("-----------descriptor------------")
class Name(object):
    "name descriptor docs"
    def __get__(self, instance, owner):
        print("__get__")
        return instance._name
    def __set__(self, instance, value):
        print("__set__")
        instance._name = value
    def __delete__(self, instance):
        print("__delete__")
        del instance._name


class Person(object):
    def __init__(self, name):
        self._name = name

    name = Name()

person = Person("xxx")
print(person.name)
person.name = "wang"
print(person.name)
del person.name

person.name = "xxxx"
print(person.name)
#class Descriptor(object):
#    def __get__(self, instance, owner):
#        print(self, instance, owner)
#
#class Subject:
#    attr = Descriptor()
#
#x = Subject()
#
#x.attr  # x.attr --> Descriptor.__get__(Subject.attr, x, Subject)
#
#
#Subject.attr
