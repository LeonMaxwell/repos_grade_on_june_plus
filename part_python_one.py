from ast import main
from asyncore import read

from collections import namedtuple

import enum

from dataclasses import dataclass

import vals

@dataclass
class Book:
    title: str
    author: str
    

class MyEnum(enum.Enum):
    TEST = 0
    BETA = 1
    ALPHA = 2
    REALESE = 3


def my_func(a,b):
    print(a,b)


def my_func_two(*args):
    print(args)


def func(a):
    def fact():
        print("Вложенная функция")
    fact()
    a += 1
    print(a)
    print("Значение внутри функции")


if "__main__" == __name__:
    # Структуры данных
    
    # Кортеж
    
    unnamed_tuple = ()
    
    print(type(unnamed_tuple))
    
    unnamed_tuple = ("Вася", "Витя")
    
    print(unnamed_tuple)
    
    NameTuple = namedtuple('Named', 'x y z')
    
    n = NameTuple(1, y=2, z=3)
    
    print(n)
    
    print(type(n))
    
    print(n[0])
    
    print(n.x)
    
    
    # Списки
    
    list_one = ['Вася', 'Петя', 'Катя']
    list_two = list()
    list_two.append(1)
    list_two.append(3)
    list_two.append(2)
    
    print(type(list_one))
    print(sorted(list_one))
    print(sum(list_two))
    
    
    # Словари
    
    my_generation_dict = dict()
    
    print(type(my_generation_dict))
    
    my_generation_dict = {list_two[i]: list_one[i] for i in range(0,3)}
    
    print(my_generation_dict)   
    
    
    # Множества
    
    
    my_set_one = {0, 3, 5, 9}
    my_set_two = {0, 2, 3, 5, 6}
    
    my_set_three = my_set_one.difference(my_set_two)    
    
    print(type(my_set_three))
    
    print(my_set_one)
    print(my_set_two)
    print(my_set_three)
    
    
    # Enum
    
    print(MyEnum.BETA.value)
    
    
    print(type(MyEnum))
    
    
    # Data Class
    
    
    book = Book(title="Хребты безумия", author="Лавкрафт")
    
    print(type(book))
    
    print(book)
    print(book.title)
    
    
    # Конструкции
    
    for reader in list_one:
        if reader == "Вася":
            print("Я не читаю нечего")
            continue
        print(f"{reader} читает {book.title} от автора {book.author}")
        
        

    # Функции
    
    
    my_func(a=book.title, b=book.author)
    
    
   
    
    print(list(map(lambda x: x ** 2, list_two)))
    
    
    my_func_two(my_generation_dict, my_generation_dict)
    
    
    # Исключения
    
    
    bc = [1,2,3,4,5,6,7]
    
    try:
        for i in bc:
            print(list_two[bc.index(i)])
    except Exception:
        print("Выход за пределы")
        
    
    # Работа с файлами
    
    
    file = open("text.txt", "w+")
    
    file.write(",".join(list_one))
    
    file.close()
    
    with open("text.txt", "r+") as f:
        print(f)
        for text in f:
            print(text)
    
    # Работа с видимостью
    
    a = 3
    print(a)
    func(vals.a)
    print(vals.a)
    
    
    
    
