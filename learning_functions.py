# A function is a block of code that performs a specific task.
# It runs only when it is called. 

# def greet(name):
#     return "Hello, " + name

# print(greet("Amit"))

# def is the keyword to define a function.
# greet is the function name.
# name is a parameter.
# The return statement sends the result back.

# Types of Functions
# Built-in Functions
# Python provides many built-in functions like:
# print()
# len()
# type()
# max(), etc

# def add(a, b):
#     return a + b

# print(add(5, 3))  # Output: 8

# Default Argument
# def greet(name="Guest"):
#     return "Hello " + name

# print(greet())         # Hello Guest
# print(greet("Sita"))   # Hello Sita

# Variable Length Arguments
# *args (Non-keyword arguments)

# def total(*numbers):
#     return sum(numbers)

# print(total(1, 2, 3, 4))  # Output: 10

# **kwargs (Keyword arguments)

# def show_info(**details):
#     for key, value in details.items():
#         print(f"{key} : {value}")

# show_info(name="Amit", age=21)


# A lambda function is a small, anonymous function defined using the lambda keyword. 
# It can have any number of arguments but only one expression.

# lambda arguments: expression

# square = lambda x: x * x
# print(square(5))  # Output: 25





