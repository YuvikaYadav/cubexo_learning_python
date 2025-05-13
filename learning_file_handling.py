# Text files store data in plain text format with .txt extension.

# Opening a Text File

# file = open('sample.txt', 'r')  # 'r' = read mode

# Reading a Text File

# with open('sample.txt', 'r') as file:
#     content = file.read()
#     print(content)

# Other reading methods:
# readline(): Reads one line at a time.
# readlines(): Returns all lines in a list.


# with open('sample.txt', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())

# Writing to a Text File

# with open('sample.txt', 'w') as file:
#     file.write("Hello, this is a new file.")

# 'w' mode overwrites.
# 'a' mode appends.


# with open('sample.txt', 'a') as file:
#     file.write("\nThis line is appended.")


# CSV File Handling

# CSV (Comma-Separated Values) files are used to store tabular data.

# Python has a built-in csv module for handling CSV files.

# import csv

# Reading a CSV File

# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# Output:

# ['Name', 'Age']
# ['Alice', '22']
# ['Bob', '25']

# DictReader to access data as a dictionary

# with open('data.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row['Name'], row['Age'])

# Writing to a CSV File

# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Age'])
#     writer.writerow(['Alice', '22'])
#     writer.writerow(['Bob', '25'])

# Using DictWriter

# with open('data.csv', 'w', newline='') as file:
#     fieldnames = ['Name', 'Age']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
    
#     writer.writeheader()
#     writer.writerow({'Name': 'Alice', 'Age': 22})
#     writer.writerow({'Name': 'Bob', 'Age': 25})

# JSON File Handling

# JSON (JavaScript Object Notation) is used to store data in key-value pairs. 
# Python provides the built-in json module.

# import json

# Writing to a JSON File

# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# with open('data.json', 'w') as file:
#     json.dump(data, file)

# Reading from a JSON File

# with open('data.json', 'r') as file:
#     content = json.load(file)
#     print(content)

# Working with JSON Strings

# json.dumps() – Converts Python object to JSON string.

# json.loads() – Converts JSON string to Python object.


# json_string = json.dumps(data)
# print(json_string)

# python_obj = json.loads(json_string)
# print(python_obj['name'])

# Pretty Printing JSON

# print(json.dumps(data, indent=4))
