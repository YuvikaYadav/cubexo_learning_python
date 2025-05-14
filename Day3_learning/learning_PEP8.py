# PEP 8 is a Coding Style guide in Python
# it is a document that provides guidelines, coding conventions, and best practices on how to write Python code.

# Some important points:
# 1. Use 4-space indentation and no tabs.
# 2. Use docstrings 
# 3. Wrap lines so that they don’t exceed 79 characters
# 4. Use of regular and updated comments are valuable to both the coders and users
# 5. Use of trailing commas
# 6. Use Python’s default UTF-8 or ASCII encodings and not any fancy encodings
# 7. Use spaces around operators and after commas, but not directly inside bracketing constructs
# 8. Naming Conventions
# 9. Characters that should not be used for identifiers
# 10.Don’t use non-ASCII characters in identifiers
# 11.Name your classes and functions consistently(CamelCase for class and lowercase_with_underscore for functions and methods)

# Type hints indicate the datatypes of both the inputs and outputs in functions (it applies to class methods as well)
# def meet_someone(name, age):
#     return f"Hey {name}, I heard you are {age}. I'm 21 and from Mars!"

# update:
# def meet_someone(name: str, age: int) -> str:
#     return f"Hey {name}, I heard you are {age}. I'm 21 and from Mars!"


# Multiple Data Types

# from typing import Union
# def meet_someone(name: str, age: Union[int, float]) -> str:
#     return f"Hey {name}, I heard you are {age}. I'm 21 and from Mars!"

# It’s simple: Union[int, float] means that we expect either an integer or a float.

# another approach for python 3.10 and higher
# def new_interns(name: str,age: int|float)->str:
#     return f"Intern name:{name}\nAge:{age}"

# info = new_interns('Riya', 23)
# print(info)

# from typing import Union
# def meet_them_all(people: dict[str, int|float]) -> str:
#     msg = ""
#     for person in people:
#         msg += meet_someone(person, people[person])
#     return msg
