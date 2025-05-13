# numbers are a basic data type used to store numeric values.:

# Types 
# int: Integer numbers 
# float: Floating-point numbers or decimals 
# complex: Complex numbers 


# Arithmetic Operations

x = 5
y = 2
print(x + y)  # 7
print(x - y)  # 3
print(x * y)  # 10
print(x / y)  # 2.5
print(x // y) # 2 
print(x % y)  # 1 
print(x ** y) # 25 


# A string is a sequence of characters enclosed in single (') or double (") quotes.

s1 = "Hello"
s2 = 'World'

# String Operations

s = "Python"
print(s[0])         # P
print(s[1:4])       # yth (slicing)
print(len(s))       # 6
print(s.lower())    # python
print(s.upper())    # PYTHON
print(s.replace("Py", "My"))  # Mython

# String Concatenation and Repetition

print("Hello" + " World")   # Hello World
print("Hi " * 3)            # Hi Hi Hi

# String Formatting

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# A list is a mutable, ordered collection that can store mixed data types.

# Creating a List
my_list = [1, 2, 3, "Python", 3.14]

# List Methods
my_list.append("New")        # Adds element at end
my_list.insert(2, "Insert")  # Inserts at index 2
my_list.remove("Python")     # Removes specific value
my_list.pop()                # Removes last element
print(len(my_list))          # List length


# Tuples 
# A tuple is similar to a list but immutable (can’t be changed after creation).

# Creating a Tuple
my_tuple = (1, 2, 3, "Python")

# Tuples are safer than lists for fixed data, faster access and iteration

# A set is an unordered collection of unique items. It is mutable but does not allow duplicates.

# Creating a Set
my_set = {1, 2, 3, 4, 5}
another_set = set([3, 4, 5, 6])

# Set Methods
my_set.add(6)            # Adds 6
my_set.remove(2)         # Removes 2
my_set.discard(10)       # Does nothing if 10 not present

# Sets are used to remove duplicates from lists, to perform mathematical operations like union, intersection

# A dictionary is an unordered, mutable collection that stores data as key-value pairs.

# Creating a Dictionary

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing Elements
print(my_dict["name"])         # Alice
print(my_dict.get("age"))      # 25

# Modifying a Dictionary
my_dict["age"] = 26            # Change age
my_dict["email"] = "a@xyz.com" # Add new key

# Dictionary Methods
print(my_dict.keys())          # dict_keys(['name', 'age', 'city', 'email'])
print(my_dict.values())        # dict_values(['Alice', 26, 'New York', 'a@xyz.com'])
print(my_dict.items())         # dict_items([('name', 'Alice'), ('age', 26)...])
my_dict.pop("city")            # Removes 'city'
