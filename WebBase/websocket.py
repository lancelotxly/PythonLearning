# -*- coding: utf-8 -*-
__author__ = 'xzq'

# -*- coding: utf-8 -*-
__author__ = 'xzq'

'''
WebSocket:
         1. 允许服务端主动向客户端推送数据
         2. 浏览器和服务器只需要完成一次握手，两者之间就直接可以创建持久性的连接，并进行双向数据传输
'''

from socket import *

def handle_request(conn):
    request_data = conn.recv(1024)
    print('request_data:',request_data)
    with open('test.html','rb') as f:
        data = f.read()
    conn.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8'))
    # conn.send('<h1>Hello web</h1>'.encode('utf-8'))
    conn.send(data)

def main():
    sock = socket(AF_INET,SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sock.bind(('127.0.0.1',8080))
    sock.listen(5)

    while True:
        print('Server is waiting for connection...')
        conn, addr = sock.accept()
        handle_request(conn)
        conn.close()

if __name__ == "__main__":
    main()


