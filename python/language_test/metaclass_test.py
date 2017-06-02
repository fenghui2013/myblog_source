#class MetaOne(type):
#    def __new__(meta, classname, supers, classdict):
#        print("In MetaOne.new:", classname, supers, classdict)
#        return type.__new__(meta, classname, supers, classdict)
#
#
#class Eggs(object): pass
#
#class Spam:
#    __metaclass__ = MetaOne
#    data = 1
#    def meth(self, arg): pass
#
#x = Spam()
#print(x.data)


class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        A.__init__(self)


class C(B):
    def __init__(self):
        print("C")
        B.__init__(self)

c = C()


class MetaA(type):
    data = "xxx"
    def __call__(meta, classname, supers, classdict):
        print("MetaA", MetaA.data)
        return type.__call__(meta, classname, supers, classdict)


class MetaB(type, metaclass=MetaA):
    def __new__(meta, classname, supers, classdict):
        print("MetaB new")
        return type.__new__(meta, classname, supers, classdict)

    def __init__(c, classname, supers, classdict):
        print("MetaB init")

    #def __call__(meta, classname, supers, classdict):
    #    return type.__call__(meta, classname, supers, classdict)


class C(metaclass=MetaB):
    data = 1
    def __init__(self):
        print("C", C.data)

    def meth(self, arg):
        pass

class D(C):
    def __init__(self):
        print("D")
        C.__init__(self)

class E(D):
    def __init__(self):
        print("E")
        D.__init__(self)

e = E()
