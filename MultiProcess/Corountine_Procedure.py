# -*- coding: utf-8 -*-
__author__ = 'xzq'


'''
simple test: 利用任务A IO阻塞的时间，去执行其他任务
             无法自动检测IO阻塞
'''
# import time
#
# def task_A():
#     g = task_B()
#     print('running task A')
#     next(g)
#     g.send(2)
#     time.sleep(3)
#     print('task A ending')
#
# def task_B():
#     value = yield
#     print('running task B: %s' % value)
#     print('task B ending')
#     yield
#
# if __name__ == "__main__":
#     start_time = time.time()
#     task_A()
#     print(time.time()-start_time)



'''
Producer & Consumer:     利用Producer做包子的时间，调用Consumer吃包子， 生产者过慢，消费者过快
                         消费者过慢，生产者过快，则反过来写就行了 
'''
# import time
# def Producer():
#     next(con)
#     print('Producer 准备做包子')
#     count = 0
#     while count < 3:
#         time.sleep(1)
#         count += 1
#         print('Producer 做好了第[%s]个包子' % count)
#         con.send(count)
#
# def Consumer(name):
#     print('%s 准备吃包子' % name)
#     count = 0
#     while True:
#         count = yield
#         print('%s 正在吃包子 [%s]' % (name, count))
#         time.sleep(0.1)
#         print('%s 吃完了第[%s]个包子' % (name, count))
#
# if __name__ == "__main__":
#     con = Consumer('xzq')
#     Producer()



'''
greenlet:  
          相比与python自带的yield，它可以使你在任意函数之间随意切换，而不需把这个函数先声明为generator
          1. g = greenlet.greenlet(func) 包装原函数
          2. g.switch(*arg,**kwarg)      切换/调用函数，会保存变量
          
'''
# from greenlet import greenlet
# import time
# def eat(name):
#     print('%s is eating' % name)
#     watch_g.switch('cctv6')
#     time.sleep(3)
#     print('%s has finished' % name)
#     watch_g.switch()
#
# def watch_tv(name):
#     print('wait for %s' % name)
#     eat_g.switch()
#     time.sleep(3)
#     print('%s finished' % name)
#
# if __name__ == "__main__":
#     eat_g = greenlet(eat)
#     watch_g = greenlet(watch_tv)
#
#     eat_g.switch('xzq')


'''
Gevent:   yield/next/send, greenlet 没有解决IO阻塞自动切换
          1. g1 = gevent.spawn(func,*args,**kwargs)  # 相当于创建(并运行)了一个虚拟线程对象，可以自动识别阻塞
          
          2. g1.join()                     # 启动加入主线程(真实的线程)，必须等g1执行完线程才能结束
             geven.joinall([g1,g2...])    # 可以用来处理单线程下大规模并发，协程会出现协程还没运行完线程就结束了
             
          3. g.value                     # 拿到func的返回值
             
          3. 要gevent识别其他阻塞，必须在导入模块之前打补丁
             from gevent import monkey;monkey.patch_all()   # 打补丁
             
'''
# from gevent import monkey;monkey.patch_all()   # 打补丁
# import gevent,time,threading
# def eat(name):
#     print(threading.currentThread().getName())   # DummyThread-1 虚拟线程
#     print('%s eat 1' %name)
#     time.sleep(2)                 # 必须在导入time模块之前打补丁
#     print('%s eat 2' %name)
#
# def play(name):
#     print(threading.currentThread().getName())
#     print('%s play 1' %name)
#     gevent.sleep(1)               # gevent.sleep(1)模拟的是gevent可以识别的io阻塞
#     print('%s play 2' %name)
#
#
# g1=gevent.spawn(eat,'egon')           # 相当于创建了两个虚拟线程
# g2=gevent.spawn(play,name='egon')
#
# g1.join()
# g2.join()
# # 或者gevent.joinall([g1,g2])
# print('主')
