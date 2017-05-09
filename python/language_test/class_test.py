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


#from abc import ABCMeta, abstractmethod
#
#class Super():
#    __metaclass__ = ABCMeta
#    @abstractmethod
#    def method(self):
#        pass
#
#s = Super()

#l = [5, 6, 7, 8, 9]
#print(l[::2])
#print(l[slice(None, None, 2)])
#
#class Indexer:
#    data = [5, 6, 7, 8, 9]
#    def __getitem__(self, index):
#        print("__getitem__: %s" % index)
#        return self.data[index]
#
#    def __setitem__(self, index, value):
#        self.data[index] = value
#
#    def __len__(self):
#        return len(self.data)
#
#x = Indexer()
#print(x[2])
#print(x[::2])
#print(x[:])
#x[:] = [1, 2, 3]
#print(x[:])
#
#for i in x:
#    print(i)

#class C:
#    def __index__(self):
#        return 255
#
#c = C()
#print(c)
#print(bin(c))


class steper:
    data = "tom"
    def __getitem__(self, i):
        print("__getitem__: %s" % i)
        return self.data[i]

x = steper()
print(x[1])
#----for----
for item in x:
    print(item)
#----in----
print('o' in x)
#----list comprehension----
print([c for c in x])
print(map(str.upper, x))
