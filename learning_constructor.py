# constructor is a method used to initialize the newly created object of a class. 
# It allows the class to assign values to the properties of the object when it is created. 
# The constructor is defined using the _init_() method.

# The _init_() function is called automatically every time the class is being used to create a new object.
# This means whenever you create an object from a class, Python automatically calls the _init_() method to initialize it.

# syntax:
# class ClassName:
#     def _init_(self, parameters):
#         # initialization code

# class Person:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("John", 25)
# print(p1.name)  # Output: John
# print(p1.age)   # Output: 25

# Types of Constructors 

# Python supports mainly two types of constructors:
# Default Constructor: Takes no parameters.
# Parameterized Constructor: Takes parameters to assign values during object creation.


# Default Constructor 

# class Demo:
#     def _init_(self):
#         print("Default Constructor Called")

# obj = Demo()

# Parameterized Constructor Example

# class Demo:
#     def _init_(self, data):
#         print("Parameterized Constructor with:", data)

# obj = Demo("Python")

# add default values to the parameters.

# class Car:
#     def _init_(self, brand="Toyota"):
#         self.brand = brand

# c1 = Car()
# c2 = Car("Honda")

# print(c1.brand)  # Toyota
# print(c2.brand)  # Honda


# Constructor Overloading 

# Unlike languages like Java, Python does not support constructor overloading directly. If you define multiple _init_ methods, only the last one is used.

# To simulate overloading, you can use default arguments or *args and **kwargs.

# class Example:
#     def _init_(self, x=None):
#         if x is not None:
#             print("Parameterized constructor:", x)
#         else:
#             print("Default constructor")

# obj1 = Example()
# obj2 = Example(10)






# ---