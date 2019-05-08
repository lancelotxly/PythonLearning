# -*- coding: utf-8 -*-


__author__ = 'xzq'


'''
直接调用
'''
# from multiprocessing import Process
# import time

# def sayhi(*args,**kwargs):
#     print('running on number <%s> with key of <%s>'% (args[0],kwargs['key']))
#     time.sleep(1)
#
# if __name__ == "__main__":
#     p1 = Process(target=sayhi,args=(1,),kwargs={'key':'A'})
#     p2 = Process(target=sayhi,args=(2,),kwargs={'key':'B'})
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#     print('ending...')



'''
继承调用
'''
from multiprocessing import Process
import time,os
class MyProcess(Process):
    def __init__(self,*args,**kwargs):
        super(MyProcess,self).__init__()
        self.num = args[0]
        self.key = kwargs['key']

    def run(self):
        print('running on number <%s> with key of <%s>' % (self.num, self.key))
        time.sleep(1)

if __name__ == "__main__":
    p1 = MyProcess(1,key='A')
    p2 = MyProcess(2,key='B')

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('ending...')

'''
子进程与主进程的关系: 1. 并列运行，所有子进程结束后，主进程关闭
                   2. 子进程join阻塞主进程
                   3. 子进程daemon脱离主进程, 设置为守护线程, 主进程可不必等待该子进程结束
'''



'''
进程方法:  1. 对象方法和属性
             p.start()  启动进程，自动运行run()方法
             p.join()   阻塞主进程
             p.daemon = True  脱离主进程
             p.run()    调用run方法，在主进程下

             p.name     获取进程名
             p.name = new_name  设置进程名
             p.num      获取进程序号
             p.pid      获取进程号，进程未开启时为None
             

             p.is_alive()      判断进程是否活跃
             p.terminate()     结束进程


         2. os方法
             os.getpid()       获取当前进程号
             os.getppid()      获取当前进程父进程号  
'''



'''
锁机制: Lock/ Event/ Semaphore
       Lock, Event, Semaphore是进程的公共资源，因此要作为参数传入函数中才能调用
'''




'''
进程队列:  multiprocessing.Queue(num),    通过q.put()加满则阻塞 和 q.get()取空则阻塞来维护线程安全
          与线程queue.Queue()不同的是: Queue()是进程的公共资源，因此要作为参数传入函数中才能调用
'''
# from multiprocessing import Process, Queue
# import time,queue
#
# def Producer(name,q):
#   count = 0
#   while count <9:
#     print("making........")
#     time.sleep(1)
#     q.put(count)
#     print('Producer %s has produced %s baozi..' %(name, count))
#     count +=1
#
# def Consumer(name,q):
#   count = 0
#   while count <9:
#     time.sleep(3)
#     if not q.empty():
#         data = q.get()
#         print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
#     count += 1
#
# if __name__ == '__main__':
#   q = Queue()
#   p1 = Process(target=Producer, args=('A',q))
#   c1 = Process(target=Consumer, args=('B',q))
#   c2 = Process(target=Consumer, args=('C',q))
#   c3 = Process(target=Consumer, args=('D',q))
#   p1.start()
#   c1.start()
#   c2.start()
#   c3.start()



'''
管道: multiprocess.Pipe 是一个双向管道，每个端口都有send()和recv()方法
     1. parent_conn, child_conn = Pipe()
     2. conn.recv() 为空则阻塞
'''
# from multiprocessing import Process, Pipe
# import os
# class MyProcess(Process):
#   def __init__(self,name,conn):
#     super(MyProcess,self).__init__()
#     self.conn = conn
#     self.name = name
#
#   def run(self):
#     print(os.getpid())
#     # self.conn.send('hello, i am %s <%s>' % (self.name, self.pid))
#     self.conn.send('')
#     print('heeee')
#     # response = self.conn.recv()
#     # print(response)
#
# if __name__ == "__main__":
#   parent_conn, child_conn = Pipe()
#   p1 = MyProcess('A',parent_conn)
#   p2 = MyProcess('B',child_conn)
#   p1.start()
#   p2.start()
#
#   p1.join()
#   p2.join()
#   # parent_conn.close()
#   # child_conn.close()


'''
Manager:  1. manager = Manager() 为所有进程创建一个manager对象,
          2. manager对象可创建公共的
                    list, dict, Namespace, 
                    Lock, RLock, Semaphore, BoundedSemaphore, Event, Queue （类似multiprocess.Lock/RLock/Semaphore/...）
          3. 各个进程可通过这些对象(manager.list(), manager.dict())对公共数据进行访问, 但注意加锁，不加锁必然会导致读写数据紊乱               
'''
# from multiprocessing import Manager,Process
# def work(d,lock):
#     with lock: #不加锁而操作共享的数据,肯定会出现数据错乱
#         d['count'] = d ['count'] - 1
#
# if __name__ == '__main__':
#     with Manager() as m:
#         dic=m.dict({'count':100})
#         lock = m.Lock()
#         p_l=[]
#         for i in range(100):
#             p=Process(target=work,args=(dic,lock))
#             p_l.append(p)
#             p.start()
#         for p in p_l:
#             p.join()
#         print(dic)


'''
进程池: 与信号量类似，但没有加锁。
       信号量是，可以开无限多的进程(线程)，但某一时刻只允许num个进程(线程)修改数据
       进程池是，从始至终只开num个进程
       1. pool = multiprocess.Pool(num)   # Pool内的进程数默认是cpu核数
       2. 同步调用 pool.apply(func= ,args=, kwargs=)
          异步调用 pool.apply_async(func=, args=, kwargs=, callback=)  
                  callback = 回调函数，该进程函数执行后再去执行的内容，执行在主线程
                             e.g. 如一些logger操作不需要再耗费子进程资源，就可以让其在子进程结束后，执行在主进程
       3. pool.close()            关闭进程池
          poo.join()              返回主进程
'''
from multiprocessing import Pool
import os,time
def work(n):
    print('%s run' %os.getpid())
    time.sleep(3)
    return n**2

if __name__ == '__main__':
    p=Pool(3) #进程池中从无到有创建三个进程,以后一直是这三个进程在执行任务
    res_l=[]
    for i in range(10):
        res=p.apply_async(work,args=(i,)) #异步运行, 非阻塞, 拿到的是对象;  同步运行, 阻塞， 直接拿到的是数据
        res_l.append(res)

    #异步apply_async用法：如果使用异步提交的任务，主进程需要使用join，等待进程池内任务都处理完，然后可以用get收集结果，否则，主进程结束，进程池可能还没来得及执行，也就跟着一起结束了
    p.close()
    p.join()
    for res in res_l:
        print(res.get()) #使用get来获取apply_aync的结果,如果是apply,则没有get方法,因为apply是同步执行,立刻获取结果,也根本无需get
