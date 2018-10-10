'''
Process and Thread: multiProcess, multiThread

'''


'''
multiProcess: 1. Create a process
                 #1. from multiprocess import Process 
                 #2. make a process object, p = Process(target=function, args=(, ))
                 #3. start a process, p.start()
                 #4, block(end) a process, p.join()
                 
              2. Multiprocess pool
                 #1. from multiprocess import Pool
                 #2. make a process pool, which is a sequence for process, if need, program will get a process; However, if no one could be provided, the program need to wait for someone end.
                     p = Pool(a)  # 'a' is the capacity of the pool
                 #3. operation of pool:
                     p.apply(function, args=(, ))   # synchronous execution, the next process need to wait the current end
                     p.apply_async(function, args=(, )) # asynchronous execution, don't need wait
                     p.terminate()   # terminate the pool
                     p.close()  # terminate the pool, when all subprocess end
                     p.join()   # must after p.close() or p.terminate(), block the process
                     
                     p.map()  # like map(func, iterable), but with multi operation 
               
              3. Communications between two processes 
                Queue:
                #1. from multiprocess import Queue
                #2. Queue().put(value) in a process
                #3. Queue().get() in another process

                Pipe:
                #1.  from multiprocess import Pipes
                #2.  (con1, con2) = Pipe()   return con1 and con2 as the two side of communication
                #3.  each con has send() and revc() methods

'''
# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print('Run child process %s (%s), which Parent process is %s' % (name, os.getpid(), os.getppid()))
#
# if __name__ == "__main__":
#     print('Parent process %s' % (os.getpid()))
#     p = Process(target=run_proc, args=('child', ))
#     print('Child process will start')
#     p.start()
#     p.join()
#     print('Child process end')

# from multiprocessing import Pool, Process
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s), whose parent process %s' % (name, os.getpid(), os.getppid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s run %0.2f seconds' % (name, end - start))
#
# if __name__ == "__main__":
#     print('Parent process %s' % (os.getpid()))
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i, ))
#     print('Wait for all subprocess done..')
#     p.close()
#     p.join()
#     print('All subprocess end')


# from multiprocessing import Process, Queue
# import os, time, random
#
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue..' % value)
#         q.put(value)
#         time.sleep(1)
#
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get()
#         print('Get %s from queue' % value)
#
# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q, ))
#     pr = Process(target=read, args=(q, ))
#
#     start = time.time()
#     pw.start()
#     pr.start()
#     pw.join()
#     print('Write end')
#     pr.terminate()
#     end = time.time()
#     print(end-start)

# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
#
# if __name__ == "__main__":
#     parent_conn, child_conn = Pipe()  # Pipe() return (conn1, conn2) stands for the two side of communications
#     p = Process(target=f, args=(child_conn, ))
#     p.start()
#     print(parent_conn.recv())
#     p.join()


'''
multi-thread: Create a thread
              #1. from threading import Thread
              #2. define function and args, then create a thread object t = Thread(target=func, args=(, ))
              #3. start a thread, t.start()
              #4. block(end) a thread, t.join()
              
              Lock
              #1. from threading import Lock
              #2. Lock().acquire()  # if the thread acquire the lock, then the following code can execute, or it must wait for the lock
              #3. Lock().release()  # after finish, the thread must release the lock for others
              tips: for python, there exists a GIL(Global Interpreter Lock), 
                    means for all thread in python, they must get the GIL, then the following code can be execute,
                    and after 100 bytecode, the GIL will be released.
'''

# import threading, time
#
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended' % threading.current_thread().name)
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('Thread %s ended' % threading.current_thread().name)

# import threading, time
#
# balance = 0
# lock = threading.Lock()
#
# def change_money(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
# def run_thread(n):
#     for i in range(1000):
#         lock.acquire()
#         try:
#             change_money(n)
#         finally:
#             lock.release()
#
# t1 = threading.Thread(target=run_thread, args=(5, ))
# t2 = threading.Thread(target=run_thread, args=(8, ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

import threading

class Student():
    def __init__(self, name):
        self.name = name

global_dict={}

def run_thread(name):
    std = Student(name)
    global_dict[threading.current_thread()] = std
    printInf()

def printInf():
    std = global_dict[threading.current_thread()]
    print('Hello, %s in (%s)' % (std.name, threading.current_thread().name))

t1 = threading.Thread(target=run_thread, args=('xzq', ), name='Thread-A')
t2 = threading.Thread(target=run_thread, args=('Cindy', ), name='Thead-B')
t1.start()
t2.start()
t1.join()
t2.join()

# ThreadLocal
local = threading.local()
def run_thread2(name):
    std = Student(name)
    local.student = std
    printInf2()

def printInf2():
    std = local.student
    print('Hello, %s in (%s)' % (std.name, threading.current_thread().name))

t1 = threading.Thread(target=run_thread2, args=('xzq', ), name='Thread-A')
t2 = threading.Thread(target=run_thread2, args=('Cindy', ), name='Thead-B')
t1.start()
t2.start()
t1.join()
t2.join()