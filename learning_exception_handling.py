# An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.

# x = 10
# y = 0
# print(x / y)  # ZeroDivisionError

# Types of Errors in Python
# 1. Syntax Errors  Mistakes in the code structure
# 2. Exceptions (Runtime Errors)  Occur during program execution

# # Syntax Error
# if True
#     print("Hello")

# # Runtime Error (Exception)
# a = [1, 2, 3]
# print(a[5])  # IndexError

# try:
#     a = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")


# Multiple Exceptions
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
# except ValueError:
#     print("Invalid input! Please enter a number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# using else block
# try:
#     print("Hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")


# Using finally Block
# try:
#     file = open("sample.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Closing file (if it was opened).")
#     try:
#         file.close()
#     except:
#         pass

# Raising Exceptions 

# age = -1
# if age < 0:
#     raise ValueError("Age cannot be negative")

# Nested Try-Except Blocks
# try:
#     try:
#         a = 10 / 0
#     except ZeroDivisionError:
#         print("Inner block: Division by zero!")
# except:
#     print("Outer block: Exception occurred")

# Handling All Exceptions
# try:
#     print(10 / 0)
# except Exception as e:
#     print("Something went wrong:", e)


# Custom Exceptions 

# Python allows users to define their own exceptions by creating a new class derived from the built-in Exception class.

# class MyCustomError(Exception):
#     pass

# def check_value(x):
#     if x < 0:
#         raise MyCustomError("Negative value not allowed!")

# try:
#     check_value(-5)
# except MyCustomError as e:
#     print("Caught an exception:", e)



