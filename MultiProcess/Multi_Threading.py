# -*- coding: utf-8 -*-
__author__ = 'xzq'

import threading,time


'''
直接调用:  1. 创建Thread对象
             t = threading.Thread(target=target_func, args=tuple, kwargs=dict)
          2. 开启线程
             t.start()
'''
# def sayhi(*args,**kwargs):
#     print('running on number <%s> with key <%s>' % (args[0],kwargs['key']))
#     time.sleep(3)
#
# if __name__ == "__main__":
#     t1 = threading.Thread(target=sayhi,args=(1,),kwargs={'key':'A'})
#     t2 = threading.Thread(target=sayhi,args=(2,),kwargs={'key':'B'})
#
#     t1.start()
#     t2.start()
#
#     print(t1.name)
#     print(t2.getName())


'''
继承调用:  1. 继承Thread类, 必须重写run()方法
             class MyThread(threading.Thread):
                  def __init__(self):
                      super(MyThread,self).__init__()
                      # code
                  
                  def run(self): pass
                  
          2. 创建MyThread类的实例
             t = MyThread()
             
          3. 开启线程
             t.start() 
'''
# class MyThread(threading.Thread):
#     def __init__(self,*args,**kwargs):
#         super(MyThread,self).__init__()
#         self.num = args[0]
#         self.key = kwargs['key']
#
#     def run(self):
#         print('running on number <%s> with key <%s>' % (self.num, self.key))
#         time.sleep(3)
#
# if __name__ == "__main__":
#     thread_list = []
#     t1 = MyThread(1,key='A')
#     t2 = MyThread(2,key='B')
#     thread_list.append(t1)
#     thread_list.append(t2)
#     for t in thread_list:
#         t.start()
#     print('ending...')



'''
子线程与主线程的关系: 1. 并列运行，所有子线程结束后，主线程关闭
                   2. 子线程join阻塞主线程
                   3. 子线程Daemon脱离主线程，主线程可不必等待该子线程结束
'''
# import threading,time
# def ListenMusic(name):
#     print('Begin listening to music %s. %s' % (name, time.ctime()))
#     time.sleep(3)
#     print('end listening. %s' % (time.ctime()))
#
# def RecordBlog(title):
#     print('Begin recording %s. %s' % (title, time.ctime()))
#     time.sleep(5)
#     print('end recording. %s' % (time.ctime()))
#
#
# t1 = threading.Thread(target=ListenMusic,args=('水手',))
# t2 = threading.Thread(target=RecordBlog, args=('Python_Note',))
#
# if __name__ == "__main__":
#     t1.start()
#     t2.start()
#
#     t1.start()
#     t2.start()
#     t1.join()
#
#     t1.setDaemon(True)
#     t1.start()
#     t2.start()
#
#     t1.start()
#     t2.setDaemon(True)
#     t2.start()
#     print('all over %s' % time.ctime())


'''
线程方法:  1. 对象方法和属性
             t.start()  启动线程，自动运行run()方法
             t.join()   阻塞主线程
             t.setDaemon(True)  脱离主线程
             t.run()    调用run方法，在主线程下
             
             t.name /  t.getName    获取线程名
             t.name = new_name / t.setName(new_name)  设置线程名
             t.daemon = True/ False
             
             t.isAlive()      判断线程是否活跃
             t.isDaemon()     判断线程是否脱离
             
         
         2. threading方法
             threading.currentThread()  当前线程对象
             threading.enumerate()      返回一个list包含目前正在运行的所有线程对象
             threading.activeCount()    等于 len(threading.enumerate())        
'''




'''
同步锁:   
      多线程操作公共变量问题:  一个线程还未来得及对公共变量进行操作，就又有其他的线程来访问该公共变量
      解决方法:   同步锁，
                 将部分代码打包转为一体， 只有当一个线程处理完后，才能分配另外的线程进行处理  
                 
      同步锁流程:  线程A，线程B，线程C,...
                 1. 多线程执行A,B,C
                 2. A竞争到lock, 先执行锁内代码，释放lock
                 3. 其他线程竞争lock
'''
# import threading,time
#
# def addNum(i):
#     global num
#     print('running in numer <%s>' % i)
#     # Lock.acquire()
#     with Lock:
#         temp = num
#         time.sleep(0.01)                 # IO阻塞, 还没来得及对全局变量计算, 就又有另外的线程来读取全局变量了
#         num = temp - 1
#     # Lock.release()
#
# num = 100
# thread_list = []
# Lock = threading.Lock()
#
# if __name__ == "__main__":
#     for t in range(100):
#         t = threading.Thread(target=addNum,args=(t,))
#         t.start()
#         thread_list.append(t)
#
#     for t in thread_list:
#         t.join()
#
#     print('final num: %s' % num)



'''
账户模型: 保证同一时刻只能取钱（Lock）或是存钱(Lock)，不能又取钱又存钱
'''
# import threading,time
# class Account:
#     def __init__(self,id,balance):
#         self.__id = id
#         self._balance = balance
#         self.lock = threading.Lock()
#
#     def withdraw(self,amount):
#         with self.lock:           # 保证同一时刻只能取钱
#             self._balance -= amount
#
#     def deposit(self,amount):
#         with self.lock:           # 保证同一时刻只能存钱
#             self._balance += amount
#
#     def drawcash(self,amount):
#         with self.lock:
#             interest = 0.05
#             count = amount + amount*interest
#             self.withdraw(count)
#
# def transfer(_from, _to, amount):
#     _from.withdraw(amount)
#     _to.deposit(amount)
#
# alex = Account('alex',1000)
# yuan = Account('yuan',1000)
#
# '''
# t1 = alex.withdraw  and yuan.deposit
# t2 = yuan.withdraw  and alex.deposit
# 当t1, t2并行执行alex.withdraw, yuan.withdraw时无影响, t1取alex的锁，t2取yuan的锁
# 若t1先执行完alex.withdraw要等t2执行完yuan.withdraw，然后t1取yuan的锁，t2取alex的锁(即交换锁)
# '''
# t1 = threading.Thread(target=transfer,args=(alex,yuan,100))
# t2 = threading.Thread(target=transfer, args=(yuan,alex,200))
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# print('alex: >>',alex._balance)
# print('yuan: >>',yuan._balance)



''' 
死锁:  线程A，线程B
     1. 线程A先竞争到Lock_A, 进而竞争到Lock_B, 先执行door_A()
     2. 线程A执行完door_A, 顺序释放Lock_B 和 Lock_A
     3. 线程A竞争到Lock_B执行door_B(), 线程B竞争到Lock_A执行door_A()
     4. 死锁，线程A等待线程B释放Lock_A, 线程B等待线程A释放Lock_B
'''
# import threading,time
# class MyThread(threading.Thread):
#     def door_A(self):
#         with Lock_A:
#             print(threading.currentThread())
#             print('open lock_A')
#             time.sleep(0.1)
#             with Lock_B:
#                 print('open lock_B')
#                 print('door_A is opened')
#
#     def door_B(self):
#
#         with Lock_B:
#             print(threading.currentThread())
#             print('open lock_B')
#             time.sleep(0.2)
#             with Lock_A:
#                 print('open lock_A')
#                 print('door_B is opened')
#
#     def run(self):
#         self.door_A()
#         self.door_B()
#
# Lock_A = threading.Lock()
# Lock_B = threading.Lock()
# thread_list = []
#
# if __name__ == "__main__":
#     for t in range(2):
#         thread_list.append(MyThread())
#
#     for t in thread_list:
#         t.start()



'''
递归锁: 
      解决死锁问题: 锁不能重用导致的，后面的代码需要前面的锁，但前面的锁已经被其他线程抢到了
                  --> 递归锁: 可重入锁， 允许一个把用多次，直到不用了再释放
'''
# import threading,time
# class MyThread(threading.Thread):
#     def door_A(self):
#         with RLock:
#             print(threading.currentThread())
#             print('open lock_A')
#             time.sleep(0.1)
#             with RLock:
#                 print('open lock_B')
#                 print('door_A is opened')
#
#     def door_B(self):
#
#         with RLock:
#             print(threading.currentThread())
#             print('open lock_B')
#             time.sleep(0.2)
#             with RLock:
#                 print('open lock_A')
#                 print('door_B is opened')
#
#     def run(self):
#         self.door_A()
#         self.door_B()
#
# RLock = threading.RLock()
# thread_list = []
#
# if __name__ == "__main__":
#     for t in range(5):
#         thread_list.append(MyThread())
#
#     for t in thread_list:
#         t.start()


'''
同步对象:  通过event.wait()来阻塞线程，event后的代码必须等待event.set()执行了才能执行
         1. 创建event = threading.Event()对象
         2. 线程A执行event.set()后，线程B,C才能运行后面的代码
         3. 线程B,C在event.wait()的代码必须要等线程A的信号
         4. 且执行完后，event.clear()等待下一次指令
         
         方法:   event.isSet(), event.set()
                event.wait(), event.clear()
'''
# import threading, time
# class Boss(threading.Thread):
#     def run(self):
#         print('Boss: 今晚大家都要加班到22:00')
#         print(event.isSet())
#         event.set()
#         time.sleep(3)
#         print('Boss: <22:00>可以下班了')
#         print(event.isSet())
#         event.set()
#
# class Worker(threading.Thread):
#     def run(self):
#         event.wait()
#         print('Worker: 命苦啊')
#         time.sleep(1)
#         event.clear()
#         event.wait()
#         print('Worker:yeah')
#
# if __name__ == "__main__":
#     event = threading.Event()
#     thread_list =[]
#     for i in range(5):
#         thread_list.append(Worker())
#     thread_list.append(Boss())
#     for t in thread_list:
#         t.start()



'''
信号量:   semaphore = threading.Semaphore(num)  类似于进程池，一次最多执行num个进程， 
         信号量与进程池的概念很像，但是要区分开，信号量涉及到加锁
         Lock同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据
         
         1. semaphore.acquire()   从池子中取一个线程，若没有则阻塞等待
         2. semaphore.release()   释放一个线程，用完后放回池子
         
         threading.BoundedSemaphore(num) 在release()会检测池子是否满了，满了则抛出异常
'''
# import threading,time
# class MyThread(threading.Thread):
#     def run(self):
#         if semaphore.acquire():
#             print(self.name)
#             time.sleep(0.1)
#             semaphore.release()
#
# if __name__ == "__main__":
#     semaphore = threading.Semaphore(2)
#     thread_list = []
#     for i in range(100):
#         thread_list.append(MyThread())
#     for t in thread_list:
#         t.start()


'''
线程队列: list不是线程安全的，保证线程安全: 1> 加锁(保证某一时刻只有一个线程在操作数据) 2> 线程队列 
         q = queue.Queue(num) 通过q.put()加满则阻塞 和 q.get()取空则阻塞来维护线程安全
         
         queue.Queue([maxsize])  队列
         queue.LifoQueue([maxsize]) 栈
         queue.PriorityQueue([maxsize]) 优先队列       
            : q.put([1,data])  按从小到大，优先级从高到低  
              q.get()          返回一个list
        
         q.put()    存数据, 满则阻塞                                  q.put_nowait()  存数据, 满则报异常, 不阻塞
         q.get()    取数据(取了队列中没有了), 空则阻塞                  q.get_nowait()  取数据, 空则报异常, 不阻塞
         q.qsize() / q.empty() / q.full()  返回当前队列长度 /  判空 / 判满
         
         q.task_done()   / q.join()  一组阻塞，‘生产者做好一个包子通知用户吃一个’ 或者是 “用户吃了一个通知生产者做一个”
         
'''
# import time
# import queue,threading
#
#
# def Producer(name):
#   count = 0
#   while count <9:
#     print("making........")
#     time.sleep(1)
#     q.put(count)
#     print('Producer %s has produced %s baozi..' %(name, count))
#     count +=1
#     # q.task_done()
#     q.join()
# def Consumer(name):
#   count = 0
#   while count <9:
#     time.sleep(3)
#     if not q.empty():
#         q.task_done()
#         # q.join()
#         data = q.get()
#         print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' %(name, data))
#     count += 1
#
# if __name__ == '__main__':
#   q = queue.Queue()
#
#   p1 = threading.Thread(target=Producer, args=('A',))
#   c1 = threading.Thread(target=Consumer, args=('B',))
#   c2 = threading.Thread(target=Consumer, args=('C',))
#   c3 = threading.Thread(target=Consumer, args=('D',))
#   p1.start()
#   c1.start()
#   c2.start()
#   c3.start()



'''
ThreadLocal:  线程本来只能访问公共变量，ThreadLocal为每个线程创建自己的变量
              1. thread_local = threading.local() 创建全局thread_local对象
              2. thread_local.attr             theread_local对象的属性属于各个线程，互不干扰，由ThreadLocal将其映射到各个线程内
              
'''
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()




