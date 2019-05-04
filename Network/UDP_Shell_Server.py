# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *
import subprocess, struct, json

IP_PORT = ('127.0.0.1',9000)
BUFSIZE = 1024

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.bind(IP_PORT)

while True:
    cmd, addr = udp_server.recvfrom(BUFSIZE)
    res = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    stderr = res.stderr.read()
    if stderr:
        feedback = stderr
    else:
        feedback = res.stdout.read()

    udp_server.sendto(feedback.encode('utf-8'),addr)

udp_server.close()
