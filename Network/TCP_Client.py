# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *

ip_port = ('127.0.0.1',9000)
BUFSIZE = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect_ex(ip_port)

while True:
    msg = input('>>:')
    if msg.lower() == 'quit':
        break
    elif len(msg) == 0:
        continue
    tcp_client.send(msg.encode('utf-8'))

    feedback = tcp_client.recv(BUFSIZE)
    print(feedback.decode('utf-8'))

tcp_client.close()

