# -*- coding: utf-8 -*-
import sys

__author__ = 'xzq'

import socket,optparse,json,os

STATUS_CODE = {
    250: "Invalid cmd format, e.g: {'action':'get','filename':'test.py','size':344}",
    251: "Invalid cmd",
    252: "Invalid auth data",
    253: "Wrong username or password",
    254: "Passed authentication",
    255: "Filename doesn't provided",
    256: "File doesn't exist on server",
    257: "ready to send file",
    258: "md5 verification",

    800: "the file exist, but not enough, is continue?",
    801: "the file exist",
    802: "ready to receive data",

    900: 'md5 validate success'
}


class ClientHandler:
    def __init__(self):
        self.op = optparse.OptionParser()
        self.op.add_option('-s','--server',dest='server')
        self.op.add_option('-P','--port',dest='port')
        self.op.add_option('-u','--username',dest='username')
        self.op.add_option('-p','--password',dest='password')

        self.options,self.args = self.op.parse_args()

        self.verify_args()
        self.make_connection()

        # D:\PythonWorkspace\PythonLearning\Network\FTP_Client
        self.mainPath = os.path.dirname(os.path.abspath(__file__))

    def verify_args(self):
        server = self.options.server
        port =self.options.port

        if int(port) > 0 and int(port) < 65535:
            return True
        else:
            exit('port is in 0-65535')

    def make_connection(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect_ex((self.options.server,int(self.options.port)))

    def interactive(self):
        print('Begin to interactive...')
        if self.authenticate():
            while True:
                cmd_info = input('[%s]'%self.current_dir).strip()
                cmd_list = cmd_info.split()
                if hasattr(self,cmd_list[0]):
                    func = getattr(self, cmd_list[0])
                    func(*cmd_list)

    def authenticate(self):
        if self.options.username is None or self.options.password is None:
            username = input('username:')
            password = input('password:')
            return self.get_auth_result(username, password)
        return self.get_auth_result(self.options.username,self.options.password)

    def response(self):
        data_json = self.sock.recv(1024).decode('utf-8')
        data = json.loads(data_json)
        return data

    def get_auth_result(self,username,password):
        data = {
            "action":'auth',
            "username":username,
            "password":password
        }
        self.sock.send(json.dumps(data).encode('utf-8'))
        response = self.response()
        if response['status_code'] == 254:
            self.username = username
            self.current_dir = username
            print(STATUS_CODE[254])
            return True
        else:
            print(STATUS_CODE[response['status_code']])

    def put(self,*cmd_list):
        # put 12.png images
        action, local_path, target_path = cmd_list
        local_path = os.path.join(self.mainPath, local_path)
        filename = os.path.basename(local_path)
        filesize = os.stat(local_path).st_size

        has_sent = 0
        data = {
            "action":"put",
            "filename":filename,
            "filesize":filesize,
            "target_path":target_path
        }
        self.sock.send(json.dumps(data).encode('utf-8'))

        ########################################################
        is_exist = self.sock.recv(1024).decode('utf-8')

        if is_exist == '800':
            # 文件不完整:  服务端先发送已经传了多少字节, 本地seek到已经传输的位置, 继续传输
            choice = input('the file exist, but not enough, is continue?[Y/N]').strip()
            if choice.upper() == 'Y':
                self.sock.sendall('Y'.encode('utf-8'))
                continue_position = self.sock.recv(1024).decode('utf-8')
                has_sent += int(continue_position)
            else:
                self.sock.sendall('N'.encode('utf-8'))

        elif is_exist == '801':
            # 文件完全存在
            print('the file exist')
            return

        f = open(local_path,'rb')
        f.seek(has_sent)
        while has_sent < filesize:
            data = f.read(1024)
            self.sock.sendall(data)
            has_sent += len(data)
            self.show_progress(has_sent,filesize)

        f.close()

        print('put success!')

    def show_progress(self,has,total):
        rate = float(has)/float(total)
        rate_num = int(rate*100)
        if rate_num == 100:
            sys.stdout.write('\n')
        else:
            sys.stdout.write('%s%% %s\r' % (rate_num, '#'*rate_num))

    def ls(self,*cmd_list):
        data = {
            'action':'ls'
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        print(data)

    def cd(self,*cmd_list):
        data ={
            'action':'cd',
            'dirname':cmd_list[1]
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        self.current_dir = os.path.basename(data)

    def mkdir(self,*cmd_list):
        data ={
            'action':'mkdir',
            'dirname':cmd_list[1]
        }
        self.sock.sendall(json.dumps(data).encode('utf-8'))
        data = self.sock.recv(1024).decode('utf-8')
        print(data)

ch = ClientHandler()
ch.interactive()
