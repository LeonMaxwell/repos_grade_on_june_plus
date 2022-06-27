from functools import wraps


def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return out

class Meee:
    def __init__(self, name, age):
      self.name = name
      self.age = age

@debug
def add(x, y):
    return x + y



if __name__ == "__main__":
    print(add(1,2))
