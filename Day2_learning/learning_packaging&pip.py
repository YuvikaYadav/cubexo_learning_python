# A package is a collection of related Python files (called modules) inside a folder. 
# This folder must contain a file called _init_.py (tells that the folder should be treated like a package)


# math_operations/
# │
# ├── _init_.py
# ├── addition.py
# └── subtraction.py

# addition.py 

# def add(a, b):
#     return a + b

# subtraction.py 

# def subtract(a, b):
#     return a - b

# another file

# from math_operations import addition
# print(addition.add(3, 5))  # Output: 8


# pip is a tool used to install and manage Python packages.
# It helps us download and use packages from the internet 


# pip install requests

# pip install numpy

# pip install pandas


# custom package
# Create a folder with code
# Add a setup.py file to the folder(describe's the package)

# setup.py:
# from setuptools import setup, find_packages

# setup(
#     name='math_operations',
#     version='0.1',
#     packages=find_packages(),
#     description='A simple math package',
#     author='Yuvika',
#     author_email='yuvika@email.com'
# )

# # creating the package
# python setup.py sdist

# # installation
# pip install dist/math_operations-0.1.tar.gz

# requirements.txt File # for other to know the needed files


# # uninstalling 
# pip uninstall package_name