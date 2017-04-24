class Singleton1(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton1, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass1(Singleton1):
    a = 1

mc1 = MyClass1()
mc2 = MyClass1()
print(id(mc1))
print(id(mc2))
mc1.a = 2
print(mc1.a)
print(mc2.a)

class Singleton2(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob = super(Singleton2, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob

class MyClass2(Singleton2):
    a = 1

mc1 = MyClass2()
mc2 = MyClass2()
print(id(mc1))
print(id(mc2))
mc1.a = 2
print(mc1.a)
print(mc2.a)


def singleton(cls, *args, **kwargs):
    instances = {}
    def get_instance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class MyClass3:
    a = 1

mc1 = MyClass3()
mc2 = MyClass3()
print(id(mc1))
print(id(mc2))
mc1.a = 2
print(mc1.a)
print(mc2.a)


#mysingleton.py
#class MySingleton(object):
#    def foo(self):
#        pass
#
#my_singleton = MySingleton()
#
#from mysingleton import my_singleton
#
#my_singleton.foo()
