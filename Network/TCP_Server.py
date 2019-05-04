# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *

ip_port = ('127.0.0.1',9000)
BUFSIZE = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(5)
print('Server is running')

while True:                                           # 一直可以接收客户端连接
      conn, addr_client = tcp_server.accept()
      print('Receive info from %s' % addr_client[0])

      while True:                                     # 处理一次连接, 一直通信
          try:
              msg = conn.recv(BUFSIZE)
              if len(msg) == 0:                       # 当客户端正常断线时, recv不再阻塞, 防止进入死循环
                  print('Client Quit')
                  break
              print(msg.decode('utf-8'))

          except Exception:
              print('Client Disconnect')              # 当客户端非正常断线时, conn.recv()会报异常, 因此服务器直接断开连接
              break

          conn.send(msg.upper())

      conn.close()

tcp_server.close()


