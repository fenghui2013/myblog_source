class T():
    xxx = "hello world"
    def __new__():
        print("__new__")

    def __init__(self):
        print("__init__")

    def __call__(self):
        print("__call__")

    #def __str__(self):
    #    return T.xxx

    #def __repr__(self):
    #    return "repr"


t = T()
print(t)
print(repr(t))



class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, "mgr", pay)

    def __getattribute__(self, k):
        print("__getattribute__: %s" % k)
        return None

    def __getattr__(self, k):
        print("__getattr__: %s" % k)
        return None

m = Manager('wb', 100)
print(m.name)
print(m.xxx)



#class Super:
#    def __init__(self, x):
#        self.x = x
#
#class Sub(Super):
#    def __init__(self, x, y):
#        Super.__init__(self, x)
#        self.y = y
#
#x = Sub(1, 2)


#class Super:
#    def method(self):
#        print("in Super.method")
#
#    def delegate(self):
#        self.action()   # expected to be defined
#
#class Provider(Super):
#    def action(self):
#        print("in Provider.action")
#
#p = Provider()
#p.delegate()


from abc import ABCMeta, abstractmethod

class Super():
    __metaclass__ = ABCMeta
    @abstractmethod
    def method(self):
        pass

s = Super()
