class A:
    def do_this(self):
        print('doing this from class A')

class B(A):
    pass

class C(A):
    def do_this(self):
        print('doing this from class C')

class D(B, C):
    pass

obj = D()
obj.do_this()
print(D.mro())