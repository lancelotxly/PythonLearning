# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *
import hmac, os

SECRET_KEY = b'This is a key for authentication'

class TCPServer:
    def __init__(self,ip_port,secret_key,buffsize=1024,backlog=5):
        self.ip_port = ip_port
        self.buffsize = buffsize
        self.server = self.server_handler(ip_port,backlog)
        self.secret_key = secret_key

    def server_handler(self,ip_port,backlog):
        tcp_server = socket(AF_INET, SOCK_STREAM)
        tcp_server.bind(ip_port)
        tcp_server.listen(backlog)
        return tcp_server


    def run_server(self):
        print('TCP Server is running...')
        while True:
            conn, addr = self.server.accept()
            print('Receive connection request from <%s: %s>' % (addr[0], addr[1]))
            self.data_handler(conn)

        conn.close()

    def data_handler(self,conn):
        if not self.conn_auth(conn):
            print('Illegal connection request, close')
            conn.close()
            return
        print('Connection has built, please contact..')
        while True:
            try:
               data = conn.recv(self.buffsize)
               if len(data) == 0:
                   print('Client quit')
                   break
               conn.sendall(data.upper())
            except Exception as e:
                print(e)
                break

    def conn_auth(self,conn):
        print('Authenticating...')
        msg = os.urandom(32)
        conn.sendall(msg)
        h = hmac.new(self.secret_key, msg)
        digest = h.digest()
        feedback = conn.recv(self.buffsize)
        return hmac.compare_digest(digest,feedback)

if __name__ == "__main__":
    s = TCPServer(('127.0.0.1',9000),SECRET_KEY)
    s.run_server()