# -*- coding: utf-8 -*-
__author__ = 'xzq'

'''
非阻塞: wait_data(unblock, 轮询), copy_data(block)
'''
# from socket import *
# import time
#
# server = socket(AF_INET,SOCK_STREAM)
# server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# server.bind(('127.0.0.1',8080))
# server.listen(5)
#
# server.setblocking(False)
# r_list = []
# w_dict = {}
#
# while True:
#     try:
#         conn,addr = server.accept()
#         r_list.append(conn)
#     except BlockingIOError:
#         time.sleep(1)
#         print('做其他的事')
#         print('r_list:',len(r_list))
#         print('w_dict:',len(w_dict))
#
#         del_rlist = []
#         for conn in r_list:
#             try:
#                 data = conn.recv(1024)
#                 if not data:
#                     conn.close()                 # 客户端没有发送数据，服务器主动断开链接
#                     del_rlist.append(conn)
#                     continue
#                 w_dict[conn] = data.upper()
#             except BlockingIOError:             # 非阻塞接收，进入下一次轮询
#                 print('进入下一次轮询')
#                 continue
#             except ConnectionResetError:        # 客户端主动断开链接，服务器异常断开链接
#                 conn.close()
#                 del_rlist.append(conn)
#
#
#         del_wlist = []
#         for conn, data in w_dict.items():
#             try:
#                 conn.send(data)
#                 del_wlist.append(conn)
#             except BlockingIOError:
#                 print('进入下一次轮询')
#                 continue
#
#         for conn in del_rlist:
#             r_list.remove(conn)
#
#         for conn in del_wlist:
#             w_dict.pop(conn)


'''
IO复用: 利用select同时检测多个non-blocking的链接，哪个wait_data(ok)就让其copy_data
        r_able, w_able, e_able = select.select(r_list, w_list, e_list, [timeout])
'''
# from socket import *
# import select
#
# server = socket(AF_INET,SOCK_STREAM)
# server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# server.bind(('127.0.0.1',8080))
# server.listen(5)
# server.setblocking(False)
#
# r_list = [server,]
# w_rlist = []
# e_list = []
# w_dict = {}
#
# while True:
#     r_able, w_able, e_able = select.select(r_list,w_rlist,e_list,0.5)
#     for sock in r_able:
#         if sock == server:
#             conn, addr = sock.accept()
#             r_list.append(conn)
#         else:
#             try:
#                 data = sock.recv(1024)
#                 if not data:
#                     sock.close()
#                     r_list.remove(sock)            # 读取接收，关闭链接，移除read监控列表
#                     continue
#                 w_rlist.append(sock)               # 若要对该链接写入， 先将其加入write监控列表
#                 w_dict[sock] = data.upper()
#             except Exception:
#                 sock.close()
#                 r_list.remove(sock)
#
#     for sock in w_able:                            # 处理写链接
#         sock.send(w_dict[sock])
#         w_rlist.remove(sock)
#         w_dict.pop(sock)


'''
selectors:   根据返回对象的不同，多态的实现处理函数，完成各自的任务
'''
from socket import *
import selectors

sel = selectors.DefaultSelector()
w_dict = {}
def accept(sock,mask):
    conn, addr = sock.accept()
    sel.register(conn,selectors.EVENT_READ,read)       # accept得到链接对象后，也将其注册到selector的监听列表内，并指明回调函数
    # sel.register(conn, selectors.EVENT_WRITE, write)  # 只能指明一种回调函数, read, write, read/write自己在回调函数中实现

def read(conn,mask):
    try:
        data = conn.recv(1024)
        if not data:
            print('closing',conn)
            sel.unregister(conn)                      # 若不需要监听则释放链接，解注册
            conn.close()
            return
        w_dict[conn] = data.upper()
        # conn.send(data.upper())
    except Exception:
        print('Client disconnect',conn)
        sel.unregister(conn)
        conn.close()

def write(conn,mask):
    conn.send(w_dict[conn])
    w_dict.pop(conn)


sock = socket(AF_INET,SOCK_STREAM)
sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sock.bind(('127.0.0.1',8080))
sock.listen(5)
sock.setblocking(False)
sel.register(sock,selectors.EVENT_READ,accept)     # 为selector绑定监听对象和回调方法

while True:
    events =sel.select()                          # selector 开始监听
    for sel_obj, mask in events:          # sel_obj 为被select的对象，其可能是 sock 也可能是 conn
        callback = sel_obj.data           # sel_obj.data 为之前绑定的回调函数, 这里有多态的意思，回调函数可能是sock.accept(), conn.read()/conn.write()
        callback(sel_obj.fileobj,mask)    # sel_obj.fileobj可能为sock, conn,
