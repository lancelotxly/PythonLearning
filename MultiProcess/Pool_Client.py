# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect_ex(('127.0.0.1',8080))

while True:
    msg = input('>>:').strip()
    if not msg:continue
    if msg == 'quit':break

    client.send(msg.encode('utf8'))
    msg = client.recv(1024)
    print(msg.decode('utf8'))