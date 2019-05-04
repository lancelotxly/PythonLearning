# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *
import time

ip_port = ('127.0.0.1',9000)
BUFSIZE = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(ip_port)

while True:
    msg, addr_client = udp_server.recvfrom(BUFSIZE)           # 阻塞, 等待下一次接收, 可以接收空
    print('Receive from client %s' % addr_client[0])
    print(msg.decode('utf-8'))

    udp_server.sendto(msg.upper(),addr_client)

udp_server.close()

'''
ntp
'''
# while True:
#     msg, addr_client = udp_server.recvfrom(BUFSIZE)
#
#     if len(msg) == 0:
#         fmt = '%Y%m%d%X'
#     else:
#         fmt = msg.decode('utf-8')
#
#     time_server = time.strftime(fmt,time.localtime())
#     udp_server.sendto(time_server.encode('utf-8'),addr_client)
#
# udp_server.close()