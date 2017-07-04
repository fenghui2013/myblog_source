import __builtin__
import time

builtin_import = __builtin__.__import__


def myimport(name, globals={}, locals={}, fromlist=[], level=-1):
    start = time.time()*1000
    res = builtin_import(name, globals, locals, fromlist, level)
    end = time.time()*1000
    print("%s: %s" % (name, end-start))
    return res

__builtin__.__import__ = myimport


import module_1
import sys


print module_1.test()

builtin_abs = abs

def abs(x):
    print(x)
    print(builtin_abs(x))

abs(-1)
