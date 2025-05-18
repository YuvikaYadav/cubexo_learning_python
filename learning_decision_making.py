# # Decision making is a core concept in any programming language. In Python, it allows you to control the flow of execution based on certain conditions. These decisions are made using conditional statements like if, if-else, if-elif-else, and nested conditionals. It enables a program to choose different paths of execution depending on the outcome of logical conditions.

# # Python uses indentation (whitespace) to define the scope of the code block, unlike other languages which use braces {}

# # if Statement

# # age = 20
# # if age >= 18:
# #     print("You are eligible to vote.")

# # if-else Statement

# # marks = 45
# # if marks >= 50:
# #     print("Pass")
# # else:
# #     print("Fail")

# # if-elif-else Ladder

# # score = 75
# # if score >= 90:
# #     print("Grade A")
# # elif score >= 75:
# #     print("Grade B")
# # elif score >= 50:
# #     print("Grade C")
# # else:
# #     print("Fail")

# # Nested if Statements

# # age = 25
# # citizen = True

# # if age >= 18:
# #     if citizen:
# #         print("Eligible to vote")
# #     else:
# #         print("Not a citizen")
# # else:
# #     print("Too young to vote")

# # Conditional Expressions (Ternary Operator) shorthand for if-else called the ternary operator or conditional expression.

# # x = value_if_true if condition else value_if_false

# # num = 5
# # result = "Even" if num % 2 == 0 else "Odd"
# # print(result)


# # Logical Operators in Conditions
# # and: True if both conditions are true.
# # or: True if at least one condition is true.
# # not: Inverts the condition.

# # age = 25
# # salary = 30000

# # if age > 18 and salary > 25000:
# #     print("Eligible for loan")
# # else:
# #     print("Not eligible")



# # logged_in = False

# # if not logged_in:
# #     print("Please log in.")

# # Membership and Identity Operators

# # fruits = ["apple", "banana", "mango"]
# # if "banana" in fruits:
# #     print("Banana is available.")


# # a = [1, 2, 3]
# # b = a
# # if a is b:
# #     print("Same object.")

# # Using Boolean Variables in Decision Making sometimes, we assign conditions to variables for clarity.

# # is_admin = True

# # if is_admin:
# #     print("Access granted.")
# # else:
# #     print("Access denied.")



# Loops are a fundamental part of programming that allow a set of instructions to be executed repeatedly until a certain condition is met. 
# In Python, there are two main types of loops:
# 1. for loop
# 2. while loop

# for Loop
# The for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string)

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# The range() function is commonly used with for loops to repeat a block of code a certain number of times

# for i in range(5):
#     print(i)

# range(5) generates numbers from 0 to 4 (5 excluded).

# for i in range(3):
#     print("Inside loop:", i)
# else:
#     print("Loop finished.")

# The else block executes after the for loop completes normally

# while Loop
# The while loop is used to execute a block of statements repeatedly as long as a condition is True.

# i = 1
# while i < 5:
#     print(i)
#     i += 1

# while True:
#     name = input("Enter your name (or 'q' to quit): ")
#     if name == 'q':
#         break
#     print("Hello", name)

# Nested Loops

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, "*", j, "=", i*j)

# Loop Control Statements

# break Statement -> terminates the loop even if the condition is true

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# continue Statement -> skips the current iteration and moves to the next

# for i in range(6):
#     if i == 3:
#         continue
#     print(i)

# pass Statement -> does nothing – a placeholder when a statement is syntactically required but no action is needed.

# for i in range(3):
#     pass  # To be implemented later







