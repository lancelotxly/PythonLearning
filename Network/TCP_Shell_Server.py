'''
解决粘包问题: 发送端在发送数据前，把自己将要发送的字节流总大小让接收端知晓，然后接收端来一个死循环接收完所有数据
'''
from socket import *
import subprocess,struct, json

IP_PORT = ('127.0.0.1',9000)
BUFSIZE = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.bind(IP_PORT)
tcp_server.listen(5)
print('TCP Server is running')

while True:
    conn, addr = tcp_server.accept()
    print('Receive from (%s:%s)' % (addr[0], addr[1]))
    while True:
        try:
            cmd = conn.recv(BUFSIZE)
            if len(cmd) == 0:
                print('Client quit')
                break
            res = subprocess.Popen(cmd.decode('utf-8'),shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
            stderr = res.stderr.read()
            if stderr:
                feedback = stderr
            else:
                feedback = res.stdout.read()

            '''
            low版:   1. 先发送数据长度
                     2. 接收端收到后返回确认
                     3. 再发送全部信息
                     4. 接收端按一定长度循环接收信息, 直到全部收完
            '''
            # data_length = str(len(feedback))
            # conn.send(data_length.encode('utf-8'))
            # msg = conn.recv(BUFSIZE)
            # if msg.decode('utf-8') == 'recv_ready':
            #     conn.sendall(feedback)


            '''
            struct制作报头:   1. struct 可以将一个类型转为指定长度的bytes
                             2. 整合发送
                             3. 接收端先提取前面四个bytes，获得报文长度
                             4. 循环接收，直到达到报文长度，全部收完
            '''
            # conn.send(struct.pack('i',len(feedback)))
            # conn.sendll(feedback)



            '''
                        复杂报头:  1. 定制报头信息，字典
                                  2. 报头序列化 pickle 或者 json + bytes()
                                  3. struct 报头长度
                                  4. 发送 报头长度 + 报头 + 报文

                                  5. 接收端先获取报头长度
                                  6. 再依据报头长度获得报头
                                  7. 再依据报头获得报文
                        '''
            header = {'data_size': len(feedback)}
            head_json = json.dumps(header)
            head_json_byte = bytes(head_json, encoding='utf-8')

            conn.send(struct.pack('i', len(head_json_byte)))
            conn.send(head_json_byte)
            conn.sendall(feedback)

        except Exception:
            print('Client disconnect')
            break
    conn.close()


