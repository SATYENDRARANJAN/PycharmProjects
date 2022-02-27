# meta programming
# function can be referenced and passed to a variable and returned to another function
# function can be declared inside another function and passed as an argunent to another function

def func():
    print("We are in first func")
    def func1():
        print("This is the first child")
    def func2():
        print("This is the second child")
    func1()
    func2()

func()


#### Higher order function : A function that accepts another function as an argument .
def add(x):
    return x+1

def sub(x):
    return x-1

def operator(func,x):
    temp = func(x)
    return temp

print(operator(add,100))
print(operator(sub,100))


#### Return another function
def hello():
    def hi():
        print("hellohell0")
    return hi

new = hello()
new()

#### Decorating funciton with parameters
def divide(x,y):
    print(x/y)

def outer_divide(func):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return func(x,y)
    return inner

divide1 = outer_divide(divide)
divide1(2,4)


#### Syntactic Decorator Decorator with @ symbol
def outer_div2(func):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return func(x,y)
    return inner

@outer_div2
def divide(x,y):
    print(x/y)

divide1= outer_div2(divide)
divide1(2,4)


#### Reusing Decorator
def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_do_twice


@do_twice
def say_hello():
    print("Hello There Reusing decorator")
say_hello()


#### Python Decorator with Argument

def do_twice_with_args(func):
    def wrapper_do_twice(*args,**kwargs):
        # print(type(args),type(kwargs))
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper_do_twice


@do_twice
@do_twice
@do_twice_with_args
@do_twice_with_args
def showname(name,age):
    print(f'{name[0]}' + "   " + f'{age[2]}')

showname(("Ram",1,2,3),{1:12,2:34})


#### Return values from decorated function
def return_hello(name):
    print("hello")
    return f'Hi {name}'
hi_adam = return_hello("Adam")
print(hi_adam)



#### Fancy Decorators
#classmethod
#staticmethod
#property

class Student:
    def __init__(self,name,std):
        self.name = name
        self.std = std

    def display(self):
        print( self.name + " got grade " + str(self.std))

    @property
    def display_as_a_property(self):
        return self.name + " got grade " + str(self.std)


stu = Student("John" ,8)
print(stu.name ,stu.std)
stu.display()
print(stu.display_as_a_property)


##### DECORATOR WITH ARGUMENTS
import functools

def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator_repeat


@repeat(num=5)
def function1(name):
    print(f'{name}')


#### Stateful Decorators : Keep track of the decorator state .
def count_fuction(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args,**kwargs):
        wrapper_count_calls.num_calls +=1
        print(f'Call {wrapper_count_calls.num_calls} of {func.__name!r}')
        return func(*args,**kwargs)
    wrapper_count_calls.num_calls=0
    return wrapper_count_calls

@count_fuction
def say_hello():
    print('say hello')

say_hello()
say_hello()
















#### Singleton instance
# Limit concurrent access to a shared resource
# create a global point of acces for a resource
# create just one instance of a class through lifetime of a program
# static object
# private constructor
# static method
# MONOSTATE BORG'S SINGLETON DESIGN PATTERN
# MODULE LEVEL SINGLETON
# CLASSIC SINGLETON

class Borg:
    __shared_state = dict()

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'GeeksforGeeks'

    def __str__(self):
        return self.state


