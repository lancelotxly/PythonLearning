# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *

IP_PORT = ('127.0.0.1',9000)
BUFSIZE = 1024

udp_client = socket(AF_INET,SOCK_DGRAM)

while True:
    msg = input('>>:')
    if not msg: continue
    elif msg.lower() == 'quit': break
    udp_client.sendto(msg.encode('utf8'),IP_PORT)

    feedback, addr = udp_client.recvfrom(BUFSIZE)
    if addr == IP_PORT:
        print(feedback.decode('utf8'))

udp_client.close()