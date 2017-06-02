class A(object):
    count = 0
    @classmethod
    def inc(cls):
        cls.count += 1

    def __init__(self):
        self.inc()

class B(A):
    count = 0
    def __init__(self):
        A.__init__(self)

class C(B):
    count = 0

a = A()
b1, b2, b3 = B(), B(), B()
c1, c2, c3, c4 = C(), C(), C(), C()

print(a.count, b1.count, c1.count)
print(A.count, B.count, C.count)
