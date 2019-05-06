# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *

IP_PORT = ('127.0.0.1',9000)
BUFFSIZE = 1024

udp_server = socket(AF_INET,SOCK_DGRAM)
udp_server.bind(IP_PORT)
print('Server is running...')

while True:
    msg, addr = udp_server.recvfrom(BUFFSIZE)
    print('Receive from %s' % addr[0])
    print(msg.decode('utf8'))

    udp_server.sendto(msg.upper(),addr)

udp_server.close()