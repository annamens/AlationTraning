class A:
    def first(self):
        print('I am in class A')

class B:
    def second(self):
        print('I am in class B')

class C(A):
    def first(self, a , b):
        print(a+b)
    sum = C
