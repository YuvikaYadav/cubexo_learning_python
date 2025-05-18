# They allow one to write simpler, shorter code without needing to bother about intricacies like loops and branching.

# Map() : 
# The purpose of map() is to generate / create a new iterable object from an existing iterable object by applying existing elements of the iterable object to the particular function. 
# varname=map(function name ,iterable obj)
# Varname is an object of <class ‘map’> map() is a pre_defined function. 
# The execution behaviour of map() is that it applies each element of an iterable object to a specified function and generates a new iterable object based on the logic we write in the function (normal function, anonymous function) . 
# Function name can be either normal function or anonymous function.
# Iterable objects can be either sequence, list, set, dict type. 

# def sq_root(x): 
#     return x**2 

# mp = map(sq_root,(1,2,3,4,5)) 
# for ele in mp: 
#     print(ele, end=” ”)     //1 4 9 16 25
    
# lambda function
# print("value:")
# old = [int (x) for x in input().split()] 
# sq = list(map(lambda x:x**2,old)) 
# print("Old:",old) 
# print("SQ:",sq)

# filter() : 
# The purpose of filter() is to filter out the elements by applying elements of iterable objects to the specified function. 
# varname=filter(functionname,iterable_obj)
# Varname is an object of <class ‘filter’>
# filter() is a pre_defined function, which is used for filtering out the elements of any iterable object by applying it to the function. 
# The execution behaviour of filter() is that if the function returns True then filter that element. If the function returns False then don’t filter that element.
# Function name can be either normal function or anonymous function.
# Iterable objects can be either sequence, list, set, dict type 
# def pos(x): 
#     if x > 0: 
#         return True 
#     else: 
#         return False
# def neg(x): 
#     if x < 0: 
#         return True 
#     else: 
#         return False

# l= [1,2,3-6,-8,-5,-3,-6,4,6,7] 
# pl = list(filter(pos,l)) 
# print("Pos list:",pl) 
# nl = list(filter(neg,l)) 
# print("Neg list:", nl) 
# Lambda function l= [1,2,3-6,-8,-5,-3,-6,4,6,7,-11] 
# pl = tuple(filter(lambda x:x>0,l)) 
# print("Pos list:",pl) 
# nl = tuple(filter(lambda a:a<0,l)) 
# print("Neg list:", nl)

# Reduce(): The purpose of reduce() is to obtain a single element / result from the iterable object by applying it to the function. 
# The reduce() present in a predefined module called “function tools” 
# varname=reduce(function name,iterable obj)

# Varname can be either fundamental data types and strings.
# Function names can either be normal function or lambda function.
# Iterable objects can be either sequence, list, set, dict type. Working functionality of reduce():
# At first step, First two elements of iterable objects are picked and the result is obtained.
# Next step is to apply the same function in such a way that the previously obtained result and the succeeding element of the iterable object and the result obtained again.
# This process continues till no more elements are left in the iterable object.
# The final result must be returned. 
# from functools import reduce 
# print("Values:") 
# lst = [int(x) for x in input().split()] 
# bg = reduce(lambda x,y:x if x>y else y, lst) 
# sm = reduce(lambda x,y:x if x<y else y, lst) 
# print(bg) print(sm)

# Recursion
# Recursion involves a function calling itself directly or indirectly to solve a problem by breaking it down into simpler and more manageable parts. 
# def recursive_function(parameters): 
#     if base_case_condition: 
#         return base_result 
#     else: 
#         return recursive_function(modified_parameters) 
    
# Base Case: This is the condition under which the recursion stops.
# It is crucial to prevent infinite loops. 
# Recursive Case: This is the part of the function that includes the call to itself. 
# It must eventually lead to the base case. 
# def fact(x): 
#     if x == 0 or x == 1: 
#         return 1 
#     return x * fact(x-1)

# print(fact(6)) 
# def fibo(x): 
#     if x == 0: 
#         return 0 
#     elif x == 1: 
#         return 1 
#     else: 
#         return (fibo(x-1) + fibo(x-2))

# print(fibo(3))

