# -*- coding: utf-8 -*-
__author__ = 'xzq'

from gevent import monkey;monkey.patch_all()
from socket import *
import gevent

def server(server_ip,port):
    s = socket(AF_INET, SOCK_STREAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   # 地址重用
    s.bind((server_ip,port))
    s.listen(5)
    while True:
        conn,addr = s.accept()
        gevent.spawn(talk,conn,addr)   # 这里不用join，因为真实线程一直在运行，不必担心协程没运行完线程就结束了
                                       # join后反而会等待协程运行完，才会处理下一个协程

def talk(conn,addr):
    try:
        while True:
            res = conn.recv(1024)
            print('client (%s: %s): %s' % (addr[0],addr[1],res.decode('utf8')))
            if not res: break
            conn.send(res.upper())
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    server('127.0.0.1',8080)