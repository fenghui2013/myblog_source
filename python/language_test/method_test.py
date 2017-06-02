class C:
    def test1(self, name):
        print(name)

    def test2(name):
        print(name)

c = C()
c.test1("xxx")
C.test1(c, "xxx")
C.test2(c)
