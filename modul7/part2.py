class D():

    def test_m2(self):
        print('in D ')


class A():
    test1 = 1
    def test_m1(self):
        print('in A')

class B(A):
    test2 = 2
    def test_m1(self):
        super().test_m1()

class C(B, D):
    test3 = 3
    def test_m1(self):
        super().test_m1()
        super(B, self).test_m1()

    def test_m2(self):
        super().test_m1()


c = C()
print(c.test1, c.test2, c.test3)
c.test_m1()
c.test_m2()