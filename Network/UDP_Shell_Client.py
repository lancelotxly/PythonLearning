# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *
ip_port=('127.0.0.1',9003)
bufsize=1024

udp_client=socket(AF_INET,SOCK_DGRAM)


while True:
    msg=input('>>: ').strip()
    udp_client.sendto(msg.encode('utf-8'),ip_port)

    data,addr=udp_client.recvfrom(bufsize)
    print(data.decode('gbk'),end='')

udp_client.close()