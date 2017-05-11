# _*_ coding:utf-8 _*_
#def makebold(fn):
#    def wrapped():
#        return '<b>' + fn() + '</b>'
#
#    return wrapped
#
#def makeitalic(fn):
#    def wrapped():
#        return '<i>' + fn() + '</i>'
#
#    return wrapped
#
#@makebold
#@makeitalic
#def say():
#    return 'hello world'
#
#print say()
#
#def closure_test(args):
#    def inner():
#        count = 0
#        while True:
#            if count >= 2:
#                break
#            print(args)
#            count += 1
#    return inner
#
#closure_test("hello")()


#def retry(f):
#    print("before")
#    f()
#    print("after")
#    return f

#class retry():
#    def __init__(self, f):
#        print(id(self))
#        print("init before")
#        self.f = f
#        print("init after")
#    def __call__(self, *args):
#        print(id(self))
#        print("call before")
#        self.f(*args)
#        print("call after")

#def retry(f):
#    def _f(*args):
#        f(*args)
#    return _f

#@retry
#def f(x, y):
#    print("function:x + y = %s" % (x+y))

#class T:
#    @retry
#    def f(self, x, y):
#        print("method:x + y = %s" % (x+y))
#
##f(1, 2)
##f(2, 3)
#
#t = T()
#t.f(1, 2)
##t.f(2, 3)
#
#
#def f2(x, *args):
#    print(len(args))
#
#f2(1)
#f2(1, 2)
#f2(1, 2, 3)



#
#print type(f)
#f(1, 2)
#f(2, 3)

#def retry(times):
#    def _retry(f):
#        def __retry():
#            new_times = times
#            while True:
#                if new_times <= 0:
#                    break
#                try:
#                    f()
#                    break
#                except Exception, e:
#                    new_times -= 1
#        return __retry
#    return _retry
#
#@retry(3)
#def f():
#    print("hello world")
#
#f()



# 类装饰器
#def decorator(cls):
#    class Wrapper:
#        def __init__(self, *args):
#            self.wrapped = cls(*args)
#
#        def __getattr__(self, name):
#            return getattr(self.wrapped, name)
#    return Wrapper
#
#
#@decorator
#class C:
#    def __init__(self, x, y):
#        self.attr = 'spam'
#
#c = C(6, 7)
#print(c.attr)

#def decorator(func, replace_callback=True):
#    def _wrapper(*args):
#        print("in _wrapper %s" % replace_callback)
#        func(*args)
#    return _wrapper
#
#@decorator
#def f():
#    print("hello world")
#
#f()

from functools import wraps

def decorator(func):
    #@wraps(func)
    def _wrapper(*args):
        func(*args)
    _wrapper.__name__ = func.__name__
    return _wrapper

@decorator
def f():
    print("hello world")

print(f.__name__)
