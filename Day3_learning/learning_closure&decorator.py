
# Closures are closely related to nested functions and are commonly used in functional programming, event handling and callbacks.
# A closure is created when a function (the inner function) is defined within another function (the outer function) and the inner function references variables from the outer function

# def fun1(a):
    
#     def fun2(b):
        
#         return a*b
    
#     return fun2

# val = fun1(3)

# print(val(5))

# Closures can be used to avoid global values and provide data hiding
# for larger cases with multiple attributes and methods

# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#     return multiplier


# # Multiplier of 3
# times3 = make_multiplier_of(3)

# # Multiplier of 5
# times5 = make_multiplier_of(5)

# # Output: 27
# print(times3(9))

# # Output: 15
# print(times5(3))

# # Output: 30
# print(times5(times3(2)))

# Decorators
# it is a flexible way to modify or extend the behavior of functions or methods, without changing their actual code.

# decorators a function that takes another function as an argument and returns a new function with enhanced functionality
# def decor(func):
    
#     def wrapper():
#         print("Morning!")
#         func()
#         print("Evening!")
        
#     return wrapper

# @decor
# def func():
#     print("Completing task..")
    
# func()

# def decor(f,x):
    
#     return f(x)

# def cube(x):
#     return x**3
# result = decor(cube,5)
# print(result)

# Functions as First-Class Objects
# can be assigned as a variable
# can be use as arguments
# can be returned from other function

# Types of Decorators
# function decorators
# methods decorators
# class decorators

# function decorators
# which takes a function as input and returns a new function
# def decor(func):
    
#     def inn():
#         print("hello",end=" ")
#         func()
#     return inn

# @decor
# def greet():
#     print("World")
    
# greet()

# Method Decorators
# Used to decorate methods within a class. They often handle special cases, such as the self argument for instance methods.

# def method_dec(func):
#     def wrapper(self):
#         print("before")
#         call = func(self)
#         print("after")
#         return call
#     return wrapper

# class DecorClass:
#     @method_dec
#     def greet(self):
#         print("Hello")
    
# d = DecorClass()
# d.greet()

# Class Decorators
# Class decorators are used to modify or enhance the behavior of a class.
# work by taking the class as an argument and returning a modified version of the class.

# def fun(cls):
#     cls.class_name = cls.__name__
#     return cls

# @fun
# class PythonLearning:
#     pass

# print(PythonLearning.class_name)


# Python provides several built-in decorators that are commonly used in class definitions

# @staticmethod
# The @staticmethod decorator is used to define a method that doesn’t operate on an instance of the class (i.e., it doesn’t use self). Static methods are called on the class itself, not on an instance of the class.

# class MyMath:
#     @staticmethod
#     def add(x,y):
#         return x+y
    
# res= MyMath.add(4,5)
# print(res)

# @classmethod
# The @classmethod decorator is used to define a method that operates on the class itself (i.e., it uses cls). Class methods can access and modify class state that applies across all instances of the class.

# class Employee:
#     raise_amount = 1.05

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount

# # Using the class method
# Employee.set_raise_amount(1.10)
# print(Employee.raise_amount)

# @property 
# The @property decorator is used to define a method as a property, which allows you to access it like an attribute. This is useful for encapsulating the implementation of a method while still providing a simple interface.

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, value):
#         if value >= 0:
#             self._radius = value
#         else:
#             raise ValueError("Radius cannot be negative")

#     @property
#     def area(self):
#         return 3.14159 * (self._radius ** 2)

# # Using the property
# c = Circle(5)
# print(c.radius) 
# print(c.area)    
# c.radius = 10
# print(c.area)