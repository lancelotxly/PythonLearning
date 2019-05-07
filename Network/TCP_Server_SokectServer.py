# -*- coding: utf-8 -*-
__author__ = 'xzq'

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is',self.request)
        print('addr is', self.client_address)
        print('server is', self.server.socket)
        print(self.server.server_address)

        while True:
            try:
                data = self.request.recv(1024)
                if len(data) == 0:
                    break
                print(data, self.client_address)
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
                break

if __name__ == "__main__":
    ip_port = ('127.0.0.1',9000)
    s = socketserver.ThreadingTCPServer(ip_port, MyServer)
    s.serve_forever()

