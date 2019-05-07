from socket import *
import struct,json
IP_PORT = ('127.0.0.1',9000)
BUFSIZE = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)
tcp_client.connect_ex(IP_PORT)

while True:
    cmd = input(">>:")
    if len(cmd) == 0: continue
    elif cmd == 'quit': break

    tcp_client.send(cmd.encode('utf-8'))

    # low版
    # length = int(tcp_client.recv(BUFSIZE).decode('utf-8'))
    # tcp_client.send('recv_ready'.encode('utf-8'))

    # struct版
    # msg = tcp_client.recv(4)
    # length = struct.unpack('i', msg)[0]     # 反解数据, 返回一个元组


    # struct复杂报头版
    head_len = tcp_client.recv(4)
    head_json_byte = tcp_client.recv(struct.unpack('i', head_len)[0])
    head_json = json.loads(head_json_byte.decode('utf-8'))
    length = head_json['data_size']


    # 知道数据长度后，开始接受数据
    recv_size = 0
    data = b''
    while recv_size < length:
          data += tcp_client.recv(BUFSIZE)
          recv_size += len(data)

    print(data.decode('gbk'))

tcp_client.close()
