# -*- coding: utf-8 -*-
__author__ = 'xzq'

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('data is ', self.request[0])
        print('Server is', self.server)
        print('socket is', self.server.socket)
        print('socket is', self.request[1])
        print(self.client_address)

        data = self.request[0]
        self.request[1].sendto(data.upper(), self.client_address)


if __name__ == "__main__":
    s = socketserver.ThreadingUDPServer(('127.0.0.1',9000),MyServer)
    s.serve_forever()