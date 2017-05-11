from functools import wraps

@wraps(add)
def add(a, b):
    return a + b

#print(add(1, 2))
#plus1 = functools.partial(add, 1)
#print(plus1(2))
#plus1_2 = functools.partial(add, 1, 2)
#print(plus1_2())
#plus1_2_3 = functools.partial(add, 1, 2, 3)
#print(plus1_2_3())
print(add(1))


#def wrap3(func):
#    @wraps(func)
#    def call_it(*args, **kwargs):
#        print "before call"
#        return func(*args, **kwargs)
#
#    return call_it
#
#@wrap3
#def hello3():
#    print("hello world3")
#
#hello3()
