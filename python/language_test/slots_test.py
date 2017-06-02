class D(object):
    __slots__ = ['a', 'b']

    c = 3

d = D()
print(d.c)

d.a = 1
print(d.a)

D.c = 2
print(D.c)
