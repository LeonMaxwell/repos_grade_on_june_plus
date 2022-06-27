class MyComparable:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        if isinstance(other, type(self)):
            try:
                return self.a == other.a
            except AttributeError:
                print("Я не утка значиит")
        return NotImplemented


class Blank(MyComparable):
    def __init__(self, a):
        self.b = a 


a = MyComparable("Лол")
b = Blank(1)
c = MyComparable("2")

print(a == c)
print(b == c)
print(a == a)


print(isinstance(a, type(b)))
print(isinstance(b, type(c)))
print(isinstance(c, type(a)))