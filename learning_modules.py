# a module is a file containing Python code (with a .py extension) that defines functions, classes, or variables, which you can reuse in other programs.
# Modules promote code reusability, organization, and namespace management.

# Creating a Module

# # file: mymodule.py
# def greet(name):
#     return f"Hello, {name}!"

# pi = 3.14159


# To use a module in another file, use the import statement.

# # file: main.py
# import mymodule

# print(mymodule.greet("Alice"))
# print(mymodule.pi)


# 3. Types of Modules

# Built-in Modules: These come with Python, e.g., math, os, sys, datetime.

# import math
# print(math.sqrt(16))  # Output: 4.0

# User-defined Modules: These are created by the user like mymodule above.

# External Modules: Installed via pip like numpy, pandas.

# # importing module
# from math import pi, sin
# print(pi)

# # mymodule.py
# def greet(name):
#     return f"Hello, {name}!"

# if _name_ == "_main_":
#     print(greet("Tester"))
