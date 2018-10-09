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
               
              3. Communications between two processes 
                #1. from multiprocess import Queue
                #2. 
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


from multiprocessing import Process, Queue
import os, time, random

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue..' % value)
        q.put(value)
        time.sleep(1)

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get()
        print('Get %s from queue' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))

    start = time.time()
    pw.start()
    pr.start()
    pw.join()
    print('Write end')
    pr.terminate()
    end = time.time()
    print(end-start)


