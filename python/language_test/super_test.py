class A:
    def test(self):
        print("A")

class B:
    def test(self):
        super().test()
        print("B")

class C:
    def test(self):
        print("C")

class D(A, B, C):
    def test(self):
        super(A, self).test()
        print("D")


d = D()
d.test()
