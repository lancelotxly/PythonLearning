# -*- coding: utf-8 -*-
__author__ = 'xzq'

from socket import *
import hmac, os

SECRET_KEY = b'This is a key for authentication'
IP_PORT = ('127.0.0.1',9000)

class TCPClient:
    def __init__(self,ip_port,secret_key,buffsize=1024):
        self.client = self.client_handler(ip_port)
        self.buffsize = 1024
        self.secret_key = secret_key

    def client_handler(self,ip_port):
        tcp_client = socket(AF_INET, SOCK_STREAM)
        tcp_client.connect_ex(ip_port)
        return tcp_client

    def run_client(self):
        print('TCP Client is running')
        self.conn_auth()
        while True:
            try:
                msg = input('>>:')
                if len(msg) == 0: continue
                if msg == 'quit':break
                self.client.sendall(msg.encode('utf-8'))
                feedback = self.client.recv(self.buffsize)
                print(feedback.decode('utf-8'))
            except Exception as e:
                print(e)
                break
        self.client.close()

    def conn_auth(self):
        msg = self.client.recv(32)
        h = hmac.new(self.secret_key,msg)
        digest = h.digest()
        self.client.sendall(digest)


if __name__ == "__main__":
    c = TCPClient(('127.0.0.1',9000),SECRET_KEY)
    c.run_client()
