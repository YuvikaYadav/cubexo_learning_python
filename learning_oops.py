# Object-Oriented Programming (OOPs) 
# OOPs is a programming paradigm that organizes software design around objects, rather than functions and logic. An object can be defined as a collection of data (attributes) and behavior (methods).
# Python is an object-oriented language, and OOP is one of the core aspects of Python. Even though Python supports multiple programming paradigms (procedural, functional, object-oriented), OOP is used widely due to its modularity, reusability, and scalability.

# Key Concepts of OOP 
# 1. Class
# 2. Object
# 3. Inheritance
# 4. Polymorphism
# 5. Encapsulation
# 6. Abstraction

# 1. Class
# A class is a blueprint for creating objects. It defines attributes and methods common to all objects of that type.

# class Dog:
#     species = "Canine"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute

# 2. Object
# An object is an instance of a class. When a class is defined, no memory is allocated. Objects are created using the class constructor.

# class Dog:
#     species = "Canine"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute

# # Creating an object of the Dog class
# dog1 = Dog("Buddy", 3)

# print(dog1.name) 
# print(dog1.species)

# Objects can have different values for their attributes but share the same structure and behavior defined in the class.



# The _init_() Method
# The _init_() method is the constructor method in Python. It is automatically called when a new object is created.

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# dog1 = Dog("Buddy", 3)
# print(dog1.name)


# 3. Inheritance
# Inheritance allows one class to inherit the properties and methods of another class. The class which inherits is called the child class, and the class being inherited from is the parent class.
# Types of Inheritance:
# Single Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hierarchical Inheritance

# class Person:
#     def _init_(self, name):
#         self.name = name

#     def display(self):
#         print("Name:", self.name)

# class Student(Person):
#     def _init_(self, name, roll_no):
#         super()._init_(name)
#         self.roll_no = roll_no

#     def show(self):
#         print(f"Name: {self.name}, Roll No: {self.roll_no}")

# s1 = Student("Alice", 101)
# s1.display()
# s1.show()

# Output:

# Name: Alice
# Name: Alice, Roll No: 101

# The super() function is used to call the constructor of the parent class.


# 4. Polymorphism
# Polymorphism allows us to perform a single action in different ways. In Python, polymorphism is usually implemented through method overriding.

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows")

# def animal_sound(animal):
#     animal.speak()

# animal_sound(Dog())
# animal_sound(Cat())

# Output:

# Dog barks
# Cat meows

# Here, the speak() method behaves differently based on the object passed.


# 5. Encapsulation
# Encapsulation is the concept of hiding the internal details of an object and only exposing selected information. This is usually done by defining private attributes and methods using a leading underscore _ or double underscore __.

# class BankAccount:
#     def _init_(self):
#         self.__balance = 0  # private attribute

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def get_balance(self):
#         return self.__balance

# account = BankAccount()
# account.deposit(1000)
# print(account.get_balance())  # 1000

# # print(account.__balance)  # AttributeError

# Encapsulation protects object data and prevents unauthorized access.


# 6. Abstraction
# Abstraction means hiding complex implementation details and showing only the necessary features.
# In Python, abstraction is implemented using abstract base classes from the abc module.

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def _init_(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth

# r = Rectangle(10, 5)
# print("Area:", r.area())

# Here, the class Shape is abstract and cannot be instantiated directly. The Rectangle class provides the implementation of the abstract method area().


# Additional Features 
# Instance Variable: Belongs to a particular object.
# Class Variable: Shared by all objects of the class.

# class Employee:
#     company = "TechCorp"  # Class variable

#     def _init_(self, name):
#         self.name = name  # Instance variable

# e1 = Employee("John")
# e2 = Employee("Alice")
# print(e1.company)  # TechCorp
# print(e2.company)  # TechCorp


