'''
多进程(线程)编程:
         1. 进程和线程
         2. 并发与并行
         3. 同步和异步
         4. 阻塞和非阻塞
         5. 进程/线程的调度模型
''' # 综述

'''
进程和线程:
    1. 进程: 
         1) 是一个程序在数据集上的一次动态执行过程
         2) 由程序, 数据集, 进程控制模块组成
    
    2. 线程: 
         1) 是CPU的一个最小执行单元, 
         2) 线程的出现是为了降低进程间切换的消耗
         3) 实现在一个进程内的并发
         4) 由线程ID, 程序计数器, 寄存器集合, 堆栈组成
    
    3. 进程和线程的关系:
         1) 进程是线程的容器, 程序至少有一个进程, 一个进程至少有一个线程
         2) 一个进程内的线程们共享进程资源, 线程几乎不拥有资源
         3) 进程之间的资源不共享
    
    4. 多进程/多线程的切换方式:
         1) IO阻塞
         2) 时间轮询               
''' # 进程和线程

'''
并发和并行:
    1. 并发:  系统具有处理多个任务的能力,(可能不是并行, 如快速切换)
    
    2. 并行:  系统具有'同时'处理多个任务的能力
    
    3. 并发和并行的关系:  并行是并发的子集
''' # 并发和并行

'''
同步和异步:
    1. 同步: 当进程(线程)执行IO操作时, 没得到结果就等待
    
    2. 异步: 当进程(线程)执行IO操作时, 不等待, 数据接收成功后, 再回来处理
    
    3. 同步和异步时针对任务的调度方式而言(等待/不等待)
''' # 同步和异步

'''
阻塞和非阻塞:
    1. 阻塞: 当进程(线程)执行IO操作时, 该进程(线程)被挂起, 直到有结果时才被激活
    
    2. 非阻塞: 当进程(线程)执行IO操作时, 该进程(线程)不会被挂起, 没有结果也返回
    
    3. 阻塞和非阻塞时针对进程(线程)的调度(挂起/不挂起)
''' # 阻塞和非阻塞

'''
进程(线程)的调度模型: 
     1. 进程(线程)的三种状态: 就绪, 执行, 阻塞
     2. 调度模型:

                ------执 行--------------------
                |        ^_______            |
               等待IO             |       执行其他线程
                |             执行该线程       |
                v                |            |
               阻 塞 ---有效IO--> 就 绪 <-------
''' # 进程(线程)调度模型

'''
Python的GIL全局解释器锁
    1. Python没有多线程: 同一个时刻, 在一个进程内(无论有多少线程), Python解释器只允许执行一个线程
    
    2. 一般任务类型:
                 1) IO密集型 --> IO切换(阻塞即切换)     无影响
                 2) 计算密集型 --> 轮询切换             Python不适合用于计算密集型任务
    
    3. 解决GIL锁的方法:
          多进程 + 协程 (但主要还是为IO密集型服务的)                     
''' # GIL全局锁

'''
多线程使用:
     1. 导入模块 import threading
     2. 开启线程的方法:
        1) 直接开启:  
                  1> 创建Thread对象
                     t = threading.Thread(target=func,args=(a,),kwargs={'k1':v1})
                  2> 开启线程
                     t.start
        2) 继承开启:
                  1> 继承Thread类, 重写run()方法[即要执行的函数]
                     class MyThread(threading.Thread):
                          def __init__(self):
                             super(MyThread,self).__init__()
                             # 其他初始化代码,如要传给函数值
                          def run(self): pass
                  2. 创建实例,开启显线程
                     t = MyThread()
                     t.start()           # 会调用其run()方法
     
     3. 子线程和主线程的关系:
        1> 主线程和子线程分别执行, 主线程会等待最后一个子线程执行完毕后, 关闭
        
        2> 子线程t.join()到主线程, 会阻塞主线程, 执行完该子线程后主线程继续执行, 最后主线程等待最后一个子线程执行完毕后, 关闭
        
        3> 在子线程开启之前, 申明该子线程为t.setDaemon(True)守护线程, 最后主线程不会等待该子线程, 其他线程执行完就关闭主线程
     
     4. 线程的属性和方法:
        1) 对象属性和方法: t.attr t.func()    
             t.func(): 
                     t.start()          # 启动线程
                     t.join()           # 阻塞当前线程
                     t.setDaemon(True)  # 设置为守护线程
                     t.run()            # 在当前线程下调用该线程的run方法
                     
                     t.getName()        # 获取线程名
                     t.setName()        # 设置线程名
                     
                     t.isAlive()        # 判断线程是否被激活
                     t.isDaemon()       # 判断线程是否为守护线程       
             t.attr:
                     t.name                # 线程名
                     t.daemon = True/False # 是否为守护线程
        
        2) threading方法:
             threading.currentThread()     # 当前线程对象   
             threading.enumerate()         # 返回一个List包含当前所有活跃的线程对象
             thread.activeCount()          # 相等于len(threading.enumerate())                                                     
''' # 多线程: 使用, 见Mulit_Threading.py

'''
线程之间通信:
一、同步锁(Lock):
       1. 多线程操作公共变量的问题:
          一个线程还未来得及对公共变量进行操作, 就又有其他线程来访问该公共变量并修改了值
       
       2. 同步锁的作用:  部分串行     
          将一部分代码打包成一个整体(加锁), 同一个时刻只有获得锁的线程才能运行锁内的代码
          Lock = threading.Lock()
          Lock.acquire()
          # code
          Lock.release()
          
       3. GIL下的Lock:  线程A，线程B，线程C,...
                       #1. 多线程争夺GIL, 若A抢到GIL的获得运行权限
                       #2. 若A有Lock则执行锁内代码
                       ...
                       #3. 多线程继续争夺GIL, 若B抢到GIL
                       #4. 此时A尚未执行完锁内代码, 锁未释放; B没有Lock, 阻塞
                       ...
                       #5. 直到A再次抢到GIL,执行完锁内代码,释放Lock
       4. join和Lock:
           t.join()是将该线程整体阻塞到当前线程, 即整体串行
           Lock是部分串行
       
       5. 应用: 账户模型    
          
           
二、死锁:  同步锁不能解决锁中锁的问题
      一把锁不能重用导致的, 后面的代码需要前面的锁, 但前面的锁已经被其他线程抢到了
      
      考虑: 线程A, 线程B, Lock_A(Lock_B), Lock_B(Lock_A)
          1. 线程A先竞争到了Lock_A, 又竞争到了Lock_B, 执行锁中代码
          2. 线程A执行完了, 顺序释放Lock_B, Lock_A
          3. 线程A竞争到了Lock_B, 线程B竞争到了Lock_A
          4. 死锁, 线程A在等Lock_A, 线程B在等Lock_B
            
三、递归锁(RLock): 解决死锁问题 
              可重入锁, 可递归使用, 没用完就不会释放
      1. 原理:
         1) RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。
         2) 直到一个线程所有的acquire都被release，其他的线程才能获得资源
      2.使用:
          RLock = threading.RLock()
          with RLock:
              #code 1
              with RLock:
                  #code 2
''' # 多线程通信: 同步锁(threading.Lock), 死锁, 递归锁(threading.RLock)

'''
同步对象(Event): 
       1.作用: 多线程运行中, 每个线程都是独立运行, Event保证其他线程需要等待某个线程的指令才能执行 
       
       2. 使用: 通过event.wait()来阻塞线程，event.wait()后的代码必须等待某一个线程event.set()执行了才能执行
              #1. Event = threading.Event()
              #2. 指定某个线程为大哥, Event.set()发出指令
              #3. 将其他线程设为小弟, Event.wait(), 要等待大哥发出指令后，Event.wait()之后代码才会执行
                  执行后将Event.clear() 等待下一个指令
       3. 方法:
          Event.isSet()
          Event.set()
          
          Event.wait()            
          Event.clear()
''' # 多线程通信: 同步对象(threading.Event)

'''
信号量(Semaphore): 
       1. 信号量与进(线)程池的区别:
          信号量是, 可以开启无限多的进程(线程), 但某一时刻只允许num个进程(线程)修改数据(涉及加锁)
          进程池是, 始终只开启num个进程(没有加锁)
       
       2. 使用:
              #1. Semaphore = threading.Semaphore(num)    // 创建一个num线程的Lock
              #2. Semaphore.acquire()                     // 从池子中取一个线程, 没有则阻塞
                  # code
                  Semaphore.release()                     // 释放一个空间         
''' # 多线程通信: 信号量(threading.Semaphore)

'''
线程队列(queue): 
       1. 线程安全: 
          1) list不是线程安全的数据类型
          2) 保证线程安全的方法: 
                            1> 加锁
                            2> 线程队列
       2. 队列类型:
          q = queue.Queue(num)              # 正常队列, FIFO
          q = queue.LifoQueue(num)          # 栈, FILO
          q = queue.PriorityQueue(num)      # 优先队列
             : q.put([num,data])            # num从小到大, 优先级从高到低
               q.get()                      # 返回一个list
               
       3. 线程队列保证线程安全
          
          q.put() # 向队列中添加数据, 队列为满则会阻塞       //           q.put_nowait() # 添加, 队列为满报异常 
          q.get() # 从队列中取数据, 队列为空则会阻塞         //           q.get_nowait() # 取值, 队列为空报异常
       
          另一种阻塞方式:
          q.task_done() <--> q.join()
       
       4. 其他方法
          q.qsize()   # 返回当前队列长度
          q.empty()   # 队列是否为空
          q.full()    # 队列是否为满
''' # 多线程通信: 线程队列(queue.Queue)

'''
线程局部变量(ThreadLocal):
    1. 作用: 每个线程只能访问公共变量, ThreadLocal为每个线程创建了自己的变量
    2. 用法:
           #1. thread_local = threading.local()    // 创建全局的thread_local对象
           #2. thread_local.attr = value           // 在每个线程内, 线程可通过thread_local的属性设定变量
                                                   // thread_local的相同属性在各个线程中不一样, 互不影响
    3. 实质:
       #1. thread_local对象内部维护一个dict, 其key为不同线程的ID, value为这些线程存储值
       #2. thread_local.attr调用属性值时, 实际上是以当前线程的ID为key, 去找值
''' # 多线程通信: 线程局部变量(threading.local)

'''
多进程使用:
     1. 导入模块 import threading
     2. 开启进程的方法:
        1) 直接开启:  
                  1> 创建Process对象
                     p = mulitprocessing.Process(target=func,args=(a,),kwargs={'k1':v1})
                  2> 开启线程
                     p.start
        2) 继承开启:
                  1> 继承Process类, 重写run()方法[即要执行的函数]
                     class MyProcess(multiprocessing.Process):
                          def __init__(self):
                             super(MyThread,self).__init__()
                             # 其他初始化代码,如要传给函数值
                          def run(self): pass
                  2. 创建实例,开启显线程
                     p = MyProcess()
                     p.start()           # 会调用其run()方法

     3. 子进程和主进程的关系:
        1> 主进程和子进程分别执行, 主线程会等待最后一个子进程执行完毕后, 关闭

        2> 子进程p.join()到主进程, 会阻塞主线程, 执行完该子进程后主进程继续执行, 最后主进程等待最后一个子进程执行完毕后, 关闭

        3> 在子进程开启之前, 申明该子进程为p.daemon = True守护进程, 最后主线程不会等待该子线程, 其他进程执行完就关闭主线程

     4. 进程的属性和方法:
        1) 对象属性和方法: p.attr p.func()    
             p.func(): 
                     p.start()          # 启动进程
                     p.join()           # 阻塞当前进程
                     p.run()            # 在当前进程下调用该进程的run方法

                     p.isAlive()        # 判断进程是否被激活
                     p.terminate()      # 结束进程      
             p.attr:
                     p.name                # 线程名
                     p.daemon = True/False # 是否为守护线程
                     p.num/p.pid           # 进程号

        2) os方法:
             os.getpid()                   # 获取当前进程号
             os.getppid()                  # 获取当前进程父进程号                                                 
'''  # 多进程: 使用, 见Mulit_Process.py

'''
多进程通信:
    1. 锁机制: Lock/ RLock/ Event/ Semaphore 同多线程
    2. 进程队列: multiprocessing.Queue       同多线程
    进程间资源不能共享, 因此在主线程中创建的Lock, RLock, Event, Semaphore, Queue, 要作为参数传入到子线程中
    
    3. 管道(Pipe): 通过管道两端的conn双向通信
           用法:  
               #1. conn1, conn2 = multiprocessing.Pipe()    //在主进程中创建
               #2. 将conn1, conn2作为参数传入进程中
               #3. 每一个conn有conn.send(), conn.recv()方法
               #4. conn.recv()为空阻塞, conn.send()为空不阻塞
    
    4. 共享数据(Manager): 所有进程都可访问的数据块
          用法:
              #1. manager = multiprocessing.Manager()   // 主进程中创建
              #2. 通过manager对象可创建公共的
                     list, dict                            // 也需要传入
                     Lock, RLock, Event, Semaphore, Queue  // 也需要传入
              #3. 各个进程可访问这些数据集, 注意进程不安全的(除了Queue)要加锁        
    
    5. 进程池(Pool):  与信号量类似，但没有加锁。
               信号量是，可以开无限多的进程(线程)，但某一时刻只允许num个进程(线程)修改数据
               进程池是，从始至终只开num个进程             
'''  # 多进程通信: 锁机制, 进程队列, Pipe, Manager, Pool

'''
协程: 
     1. 协程的定义:
        1) 是一种用户态的轻量级线程, 即协程是由用户程序自己控制调度的
        2) 是一种协作而非抢占式的处理并发方式, A --> B ---> A --> C
        3) 协程的切换属于程序级别的, 操作系统不需要切换     
     
     2. 协程的特点:
         1) 协程本身是一个线程, 是用户态的切换
         2) 相比线程优点:
                       1> 切换没有消耗 
                       2> 修改共享程序不需要加锁
         3) 相比线程缺点:
            一旦引入协程，就需要检测单线程下所有的IO行为, 实现遇到IO就切换,少一个都不行，因为一旦一个任务阻塞了，整个线程就阻塞了
     
     3. 并发要求:
         1) 要控制多个任务之间的切换 
         2) 切换之前要把当前任务状态保存下来        (yield, greenlet无法检测IO)
         3) 可以自动检测IO操作, 在IO阻塞下发生切换   (geven可以检测IO)    
''' # 协程

'''
协程实现: 
    1. 生成器: yield, next(g), g.send(value)
       用法:
            yield                      # 可以保存状态
            g = generator()            # 创建生成器
            next(g)                    # 检测到最近yield位置, 执行yield之前的代码
            g.send(value)              # 检测当前yield的位置，把值通过该yield传入，执行下一个yield到该yield之间的代码, 然后返回
    
    2. greenlet: 使任意函数变为生成器
       用法:
           g = greenlet.greenlet(fun)    # 将函数包装为生成器
           g.switch(*args,**kwargs)      # 在一个函数中切换到fun  
    
    3. gevent: 可自动完成IO阻塞切换
       用法:
           1) g = gevent.spawn(func,*args,**kwargs)  # 相当于创建了一个虚拟线程对象, 可自动识别IO阻塞
           
           2) 若要gevent识别其他类型阻塞, 必须在导入该模块前打补丁
              from gevent import monkey;monkey.patch_all()
           
           3) g.join()                               # 协程启动加入主线程(真实线程)
              g.joinall([])                          # 线程可能出现协程还没执行完, 线程就结束了, 所有协程必须join到主线程
           
           4) g.value                                # 获取协程返回值
''' # 协程实现

