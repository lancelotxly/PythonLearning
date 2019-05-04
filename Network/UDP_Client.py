# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *

ip_port = ('127.0.0.1',9000)
BUFSIZE = 1024

udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>:')
    if len(msg) == 0: continue
    elif msg.lower() == 'quit': break
    udp_client.sendto(msg.encode('utf-8'),ip_port)

    feedback, addr_server = udp_client.recvfrom(BUFSIZE)           # 阻塞, 等待下一次接收, 可以接收空
    print('Receive from server %s' % addr_server[0])
    print(feedback.decode('utf-8'))

udp_client.close()


'''
ntp
'''
# while True:
#     msg = input('>>:')
#     udp_client.sendto(msg.encode('utf-8'),ip_port)
#
#     feedback, add_server = udp_client.recvfrom(BUFSIZE)
#     print('Receive from server %s' % add_server[0])
#     print(feedback.decode('utf-8'))
