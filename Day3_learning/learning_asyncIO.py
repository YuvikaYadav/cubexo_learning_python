# Asyncio is a Python library that is used for concurrent programming
# It is not multi-threading or multi-processing

# to achieve asynchronus programming async keyword is used
# await keyword is used to sleep of the program exceution

# import asyncio

# async def fun():
#     print("hello")
#     await asyncio.sleep(2)
#     print("perform addition")
#     await asyncio.sleep(2)
#     a = 1
#     b = 2
#     print(f"{a} + {b} = {a+b}")
    
# asyncio.run(fun())

# import asyncio

# async def fun1():
#     print("Hello!!")
#     await asyncio.sleep(2)
#     await fun2()
#     print("report with SOD before 10:05 A.M.")
#     await asyncio.sleep(2)
#     print("also, EOD before lelaving the office")
#     await asyncio.sleep(1)
#     print("Good Day")
    
# async def fun2():
#     print("New Interns")
#     await asyncio.sleep(1)
#     print("you all are assigned your task")
#     await asyncio.sleep(1)
#     print("complete it asap")
#     await asyncio.sleep(1)
    
# asyncio.run(fun1())

# import asyncio

# async def fun1():
#     task = asyncio.create_task(fun2())
#     print("first")
#     await asyncio.sleep(2)
#     print("third")
#     await asyncio.sleep(2)
#     print("fifth")
    
# async def fun2():
#     print("second")
#     await asyncio.sleep(2)
#     print("fourth")
#     await asyncio.sleep(2)
    
# asyncio.run(fun1())

# i/o bound

# import asyncio

# async def fun1():
#     print("f1 started")
#     await asyncio.sleep(2)
#     print("f1 ended")
    
# async def fun2():
#     print("f2 started")
#     await asyncio.sleep(1)
#     print("f2 ended")
    
# async def fun3():
#     print("f3 started")
#     await asyncio.sleep(3)
#     print("f3 ended")
    
# async def main():
#     a = await asyncio.gather(
#         fun1(),
#         fun2(),
#         fun3(),
#     )
#     print("Asynchronization End.")
    
# asyncio.run(main())

