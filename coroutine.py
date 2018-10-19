'''
注意到consumer函数是一个generator，把一个consumer传入produce后：

    1.首先调用c.send(None)启动生成器；

    2.然后，一旦生产了东西，通过c.send(n)切换到consumer执行；

    3.consumer通过yield拿到消息，处理，又通过yield把结果传回；

    4.produce拿到consumer处理的结果，继续生产下一条消息；

    5.produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
'''
# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return n
#         print('Consumer consuming %s' % n)
#         r = '200 ok'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('Producer producing %s' % n)
#         r = c.send(n)
#         print('Consumer return: %s' % r)
#     c.close();
#
# c = consumer()
# produce(c)

# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from asyncio.sleep(10)
#     print("Hello again!")
#
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# import threading
# import asyncio
#
# @asyncio.coroutine
# def hello1():
#     print('Hello world1! (%s)' % threading.currentThread())  #1
#     yield from hello2()                                     #2
#     print('Hello again1! (%s)' % threading.currentThread())  #3
#
# def hello2():
#     print('Hello world2! (%s)' % threading.currentThread())  #4
#     yield from asyncio.sleep(1)                             #5
#     print('Hello again2! (%s)' % threading.currentThread())  #6
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello1(), hello2()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# import asyncio
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()





import asyncio

async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
