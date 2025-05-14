# threading
# a process is an instance of a computer program that is being executed
# a thread is a sequence of such instructions within a program that can be executed independently of other code
# can assume that a thread is simply a subset of a process

# Thread Control Block (TCB) :

# Thread Identifier: Unique id (TID) is assigned to every new thread
# Stack pointer: Points to the thread’s stack in the process. The stack contains the local variables under the thread’s scope.
# Program counter: a register that stores the address of the instruction currently being executed by a thread.
# Thread state: can be running, ready, waiting, starting, or done.
# Thread’s register set: registers assigned to thread for computations.
# Parent process Pointer: A pointer to the Process control block (PCB) of the process that the thread lives on.

# Each thread contains its own register set and local variables (stored in the stack) .
# All threads of a process share global variables (stored in heap) and the program code .

# Multithreading is defined as the ability of a processor to execute multiple threads concurrently.

# In context switching, the state of a thread is saved and the state of another thread is loaded whenever any interrupt (due to I/O or manually set) takes place

# import threading


# def print_cube(num):
#     print("Cube: {}" .format(num * num * num))


# def print_square(num):
#     print("Square: {}" .format(num * num))


# if __name__ =="__main__":
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

#     print("Done!")

# A thread pool is a collection of threads that are created in advance and can be reused to execute multiple tasks.

# The concurrent.futures module in Python provides a ThreadPoolExecutor class that makes it easy to create and manage a thread pool.

# The main thread waits for the worker threads to finish using pool.shutdown(wait=True)

# Thread synchronization is defined as a mechanism which ensures that two or more concurrent threads do not simultaneously execute some particular program segment known as critical section.
# Critical section refers to the parts of the program where the shared resource is accessed.

# A race condition occurs when two or more threads can access shared data and they try to change it at the same time. As a result, the values of variables may be unpredictable and vary depending on the timings of context switches of the processes.


