# iterator

# an iterator is an object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets
# iterators object is initialized using the iter() method and  returns the iterator object itself
# It uses the next() method for iteration that retrieves the next available item

# iterable

# Iterables are objects that can return an iterator
# includes lists, dictionaries, and sets
# An iterable implements the __iter__() method, which is expected to return an iterator object.

# s = "GFG"
# it = iter(s)

# print(next(it))     # G
# print(next(it))     # F
# print(next(it))     # G

# # custom iterator
# class OddNumbers:       #created class
#     def __iter__(self):     #initialization
#       self.a = 1
#       return self
  
#     def __next__(self):     #iteration
#       x = self.a
#       self.a += 2
#       return x

# odd = OddNumbers()
# it = iter(odd)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# There are many build-in iterators in the module “itertools“. 
# 1. accumulate(iter, func) :- This iterator takes two arguments, iterable target and the function which would be followed at each iteration of value in target.
# 2. chain(iter1, iter2..) :- This function is used to print all the values in iterable targets one after another mentioned in its arguments.

# import itertools
# import operator

# lst1 = [2,4,5,7]
# lst2 = [1,2,3,4,5,6]
# lst3 = [8,9,0,3,4,56,7]

# print(list(itertools.accumulate(lst1)))     #by default gives addition if no  function is passed
# print(list(itertools.accumulate(lst2, operator.mul)))
# print(list(itertools.chain(lst1, lst2, lst3)))

# 3. chain.from_iterable() :- This function is implemented similarly as chain() but the argument here is a list of lists or any other iterable container.
# 4. compress(iter, selector) :- This iterator selectively picks the values to print from the passed container according to the boolean list value passed as other argument. 
#    The arguments corresponding to boolean true are printed else all are skipped.

# import itertools
# import operator

# lst1 = [2,4,5,7]
# lst2 = [1,2,3,4,5,6]
# lst3 = [8,9,0,3,4,56,7]
# lst4 = [lst1,lst2,lst3]
# print(list(itertools.chain.from_iterable(lst4)))
# print(list(itertools.compress('learning Python Programming',[1,0,0,0,1,0,0,0,1,1,0,0])))

# iter(callable,sentinel)

# import random 

# random_iter = iter(lambda: random.randint(25,40),35)
# for num in random_iter:
#     print(num)

# If there are no more elements, it raises the StopIteration exception

# tuple = (2,4,6,7,8,1)

# tup = iter(tuple)
# while True:
#     try:
#         print(tup.__next__())
#     except StopIteration:
#         break

# iterator is also an iterable, but not every iterable is an iterator in Python.


# Yield
# Return sends a specified value back to its caller whereas Yield can produce a sequence of values. 
# We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory. 
# Yield is used in generators.

# Generator
# A generator function is a special type of function that returns an iterator object

# def fun():
#     yield 1
#     yield 2

# for val in fun():
#     print(val)          ## 1 2
                           

# def min(min_val):
#     i = 10
#     while i > min_val:
#         yield i 
#         i -= 1
        
# value = min(2)
# for val in value:
#     print(val)      # 10 to 3

# Generator expressions are a concise way to create generators.
# They are similar to list comprehensions but use parentheses instead of square brackets and are more memory efficient.

# (expression for item in iterable)

# num = (x*x for x in range(2,10))
# <generator object <genexpr> at 0x000001CAD2F3C380>      # if not using iterator in will return a generator object

# sqroot = (x**0.5 for x in range(1,11))
# for sq in sqroot:
#     print(round(sq,2))      
# o/p 
# 1.0
# 1.41
# 1.73
# 2.0
# 2.24
# 2.45
# 2.65
# 2.83
# 3.0
# 3.16
