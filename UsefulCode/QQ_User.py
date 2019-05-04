# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *

IP_PORT = ('127.0.0.1',9000)
BUFSIZE = 1024

def login():
    username = input('Please input username:')
    password = input('Please input password:')
    msg = username + '+' + password
    udp_client.sendto(msg.encode('utf-8'),IP_PORT)

    feedback, addr = udp_client.recvfrom(BUFSIZE)
    print(feedback.decode('utf-8'))
    return True

def send_msg_to():
    while True:
        qq_name = input('Please input your friend name:')
        if qq_name == 'quit':
            udp_client.sendto(qq_name.encode('utf-8'), IP_PORT)
            print('Bye')
            break
        udp_client.sendto(qq_name.encode('utf-8'),IP_PORT)
        feedback, addr = udp_client.recvfrom(BUFSIZE)
        print(feedback.decode('utf-8'))



if __name__ == "__main__":
    udp_client = socket(AF_INET, SOCK_DGRAM)
    flag = login()
    if flag:
        send_msg_to()

    udp_client.close()