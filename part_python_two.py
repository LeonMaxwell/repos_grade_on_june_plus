

class MyFirstClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
class MySecondClass(MyFirstClass):
    def __init__(self, name, age, staff_num):
        super().__init__(name, age)
        self.staff_num = staff_num
    
    def _hi(self):
        print("Приват метод")
        return True
    
    @staticmethod
    def mystat():
        print("Это статичный")
        return True



if "__main__" == __name__:
    my_first = MyFirstClass("Вася", 20)
    my_second = MySecondClass("Петя", 20, 200)
    
    print(MySecondClass.mro())
    
    print(my_second._hi())
    print(my_first.name)
    print(my_second.mystat())
    
    num: int = 1
    
    print(type(num))
    

