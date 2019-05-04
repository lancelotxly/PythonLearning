# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *
IP_PORT = ('127.0.0.1',9000)
BUFSIZE = 1024
USERS_INFO = {
    'John':{'password':'123','ip_port':None},
    'Jerris':{'password':'456','ip_port':None},
    'Cindy':{'password':'789','ip_port':None}
}


def login():
    msg, addr = udp_server.recvfrom(BUFSIZE)
    username, password = msg.decode('utf-8').split('+')
    if username in USERS_INFO:
        if password == USERS_INFO[username]['password']:
            USERS_INFO[username]['ip_port'] = addr
            print('%s login' % username)
            msg = 'Welcome <%s>, your ip_port is (%s:%s)' % (username, addr[0], addr[1])
            udp_server.sendto(msg.encode('utf-8'), addr)
            return True
        else:
            msg = 'Wrong password'
            udp_server.sendto(msg.encode('utf-8'), addr)
    else:
        msg = 'Sorry, <%s> no exist' % username
        udp_server.sendto(msg.encode('utf-8'),addr)



def send_msg_to():
    while True:
        msg, addr = udp_server.recvfrom(BUFSIZE)
        name = msg.decode('utf-8')
        if name == 'quit':
            print('(%s:%s) quit' % (addr[0], addr[1]))
            break
        if name not in USERS_INFO:
            msg = 'Sorry, <%s> not exist' % name
            udp_server.sendto(msg.encode('utf-8'), addr)
        elif USERS_INFO[name]['ip_port'] is None:
            msg = 'Sorry, <%s> have not connect' % name
            udp_server.sendto(msg.encode('utf-8'),addr)
        else:
            while True:
                msg, addr = udp_server.recvfrom()
                udp_server.sendto(msg, USERS_INFO[name]['ip_port'])






if __name__ == "__main__":
    udp_server = socket(AF_INET, SOCK_DGRAM)
    udp_server.bind(IP_PORT)
    while True:
        flag = login()
        if flag:
            send_msg_to()
    udp_server.close()

