from socket import *
import os,hmac

SECRET_KEY = b'This is a key for authentication'
IP_PORT = ('127.0.0.1',9000)

class TCPServer(object):
    def __init__(self,ip_port,secret_key,buffsize=1024,backlog=5):
        self.buffsize = buffsize
        self.secret_key = secret_key
        self.server = self._server_handler(ip_port,backlog)

    def _server_handler(self,ip_port,backlog):
        server = socket(AF_INET,SOCK_STREAM)
        server.bind(ip_port)
        server.listen(backlog)
        return server

    def run_server(self):
        print('TCP Server is running...')
        while True:
            conn,addr = self.server.accept()
            print('Receive from %s' % addr[0])
            self._data_handler(conn)

    def _data_handler(self,conn):
        if self._conn_auth(conn):
            print('illegal connection, closed')
            conn.close()
            return
        print('Connection has built...')
        while True:
            try:
                msg = conn.recv(self.buffsize)
                if not msg:
                    print('Client quit')
                    break
                print(msg.decode('utf8'))
                conn.sendall(msg.upper())
            except Exception as e:
                print(e)
                break
        return conn.close()

    def _conn_auth(self,conn):
        print('Authenticate...')
        msg = os.urandom(32)
        conn.sendall(msg)
        key = hmac.new(self.secret_key,msg).digest()
        feedback = conn.recv(self.buffsize)
        return hmac.compare_digest(key,feedback)

if __name__ == "__main__":
    s = TCPServer(IP_PORT,SECRET_KEY)
    s.run_server()