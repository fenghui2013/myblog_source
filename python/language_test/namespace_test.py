#x = 1

#def f():
#    global x
#    x = 12
#
#print(x)
#f()
#print(x)


def f(x):
    #x = 11
    print(x)
    def wrapper():
        global x
        x += 1
        print(x)
    return wrapper



f(1)()
