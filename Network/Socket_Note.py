'''
网络编程:
       1. 网络分层
       2. C/S和B/S架构
       3. Socket +  TCP/UDP
       4. TCP粘包
       5. 基于TCP实现验证
       6. 多线程Socket
''' # 综述

'''
1. 网络结构:
      /*OSI七层*/        /*TCP/IP五层*/         /*TCP/IP四层*/    协议
       应用层
       表示层   ------      应用层      ----       应用层          HTTP, FTP, DNS
       会话层
       
       /***************  Socket **********************/
       
       传输层   ------      传输层      ----       传输层         TCP/UDP
       网络层   ------      网路层      ----       网路层           IP 
       
       数据链路层 ----       数据链路层  ----       网络接口层       ARP  
       物理层   ------      物理层

2. Socket分类:   
          AF_UNIX  # 文件socket
          AF_INET  # 网络socket

3. 程序的唯一标识:   IP_PORT = ('ip_port',port)                        
''' # 网络分层, socket分类, 程序的唯一标识

'''
C/S和B/S架构:
    1. C/S: Client and Server
       #1. 两层架构
       #2. 客户端需要实现绝大多少的业务逻辑和界面展示
       #3. 服务器端实现与数据库交互
       
       优点: 
            #1. 交互只有一层, 响应速度快
            #2. 客户端操作丰富
            #3. 安全性好
       缺点:
            #1. 用户群窄, 需要安装客户端
            #2. 维护成本高, 发生一次升级, 所有客户端要更新
    
    2. B/S: Browser and Server
       #1. Browser, Server和DataBase构成三层架构
       #2. 事务主要在后端处理, 前端负责呈现
        
       优点: 
           #1. 客户端无需安装, 浏览器就行了
           #2. 用户群广
           #3. 升级服务器就行了
       缺点:
           #1. 跨浏览器的兼容问题
           #2. 响应速度和安全问题               
''' # C/S和B/S架构

'''
TCP/IP: 面向连接
     1. 流程
        /*Server*/                                                   /*Client*/
        tcp_server = socket(AF_INET,STREAM)                          tcp_client = socket(AF_INET,STREAM)
        tcp_server.bind(IP_PORT)                                     tcp_client.connect_ex(IP_PORT)
        tcp_server.listen(num)
        ---- 准备 --------------                                       
        
        conn, addr = tcp_server.accept()
        ---- 监听, 有用户接入则建立连接-----                             -------  客服端接入 ---------------
        
        conn.recv(BUFSIZE)                                           tcp_client.send(b'msg')
        conn.send(b'msg')                                            tcp_client.recv(BUFSIZE)
        ---- 读取或者发送消息 ------------                              -------- 发送或读取消息 -----------
        
        conn.close()                                                 tcp_client.close()
        ---- 服务器断开连接 -----------                                ------ 客户端断开连接 -------------
        
        tcp.server.close()
        ---- 服务器关闭 --------------
     
     2. 注意:
        1>服务器端有两次阻塞: 
                        1) tcp_server.accept()   # 等待客户端接入, 没有则程序卡住; 
                                                 # 有多个连接接入时, 则将其余存入缓存区, 等当前连接处理完断开后, 再处理下一个连接
                        2) conn.recv()           # 服务器从自己的内核态取数据, 没有数据则卡住                                    
        2>客户端有一次阻塞: 
                        1) tcp_client.recv()     # 客户端从自己的内核态中取数据, 没有则卡住
        3>TCP基于数据流, 不允许收发为空
        4>要先启动服务器, 再启动客户端                
     
     # 见: TCP_Server.py   TCP_Client.py 
''' # Socket: TCP

'''
UDP/IP: 无连接, 对等网络
      1. 流程:
         /*Server*/                                                       /*Client*/
         udp_server = socket(AF_INET, SOCK_DGRAM)                         udp_client = socket(AF_INET,SOCK_DGRAM)
         udp_server.bind(IP_PORT)                                         
         ---- 准备 -----                                                  ------- 准备 --------
         
         msg, addr = udp_server.recvfrom(BUFFSIZE)                       udp_client.sendto(msg,addr)                        
         udp_server.sendto(msg,addr)                                     msg,addr = udp_client.recvfrom(BUFFSIZE)
         --- 接收或发送数据 ---                                            ------ 发送或接收数据 ----
         
         udp_server.close()                                              udp_client.close()
         --- 断开连接,并关闭服务器--                                         ----断开连接并关闭服务器 ---
      
      2. 注意:
         1> 服务器端有一次阻塞:   udp_server.recvfrom()
         2> 客户端有一次阻塞:     udp_client.recvfrom()
         3> UDP基于消息, 可以发空, 收空则阻塞
         4> 服务器和客户端实质上是对等网络, 只不过服务器明确绑定了IP_PORT
         
      见: UDP_Server.py  UDP_Client.py       
''' # Socket: UDP

'''
基于Socket的TCP/UDP收发数据原理:
     1. TCP: 面向连接
            发送:  socket程序 --> 内核态 --> TCP --> 发送
                  TCP是面向数据流的, 会把发送间隔短且数据量小的数据整合打包发送, 接收端不知道文件从何处开始, 何处结束
            
            接收:  TCP --> 内核态 --> socket程序
                  TCP传输的数据不会丢, 一次没有收完的包, 下一次会继续接收, socket程序在取完所有数据时会想内核态发送ack, 才会清除缓存
                  数据可靠, 但会粘包
                  
     2. UDP: 面向数据报
           发送:  socket程序 --> 内核态 --> UDP --> 发送
                 UDP面向数据报, 每一个UDP包有报头, 接收端很容易区分数据报
           
           接收:  UDP --> 内核态 --> socket程序      
                 若时发送数据大于接收额, 数据会丢失, 不会粘包, 但不可靠                                    
''' #  基于Socket的TCP/UDP收发数据原理

'''
粘包: 
    粘包情况: 1) 发送间隔短, 数据量小
             2）一次没接收完
    
    解决方法: 发送端在发送数据前，把自己将要发送的字节流总大小让接收端知晓，然后接收端来一个死循环接收完所有数据
    见: TCP_Shell_Server.py  TCP_Shell_Client.py       
''' # 粘包

'''
基于TCP的验证:
    1. 面向对象的TCPServer, TCPClient写法
    2. 验证: hmac + key
    见: TCP_Server_Authentication.py TCP_Client_Authentication.py
''' # 基于TCP的验证

'''
socketserver:
继承结构:
         #1. Server类(解决连接):
                                                +------------+
                                                | BaseServer |
                                                +------------+
                                                      ^
                                                      |
                                                +-----------+        +------------------+
                                            |-->| TCPServer |<-------| UnixStreamServer |
                                            |   +-----------+        +------------------+
+--------------------+                      |          ^
| ThreadingMixIn     | <-----------|        |          |
+--------------------+             |        |          |
         ^                         |        |          |
         |                         |        |     +-----------+        +--------------------+
         |                         |        |     | UDPServer |<-------| UnixDatagramServer |
         |                         |        |     +-----------+        +--------------------+
+--------------------+             |        |           ^
| ThreadingTCPServer | ------------|--------|           |
+--------------------+             |                    |
                                   |                    |
                            +--------------------+      |
                            | ThreadingUDPServer |------|
                            +--------------------+

         #2. Request类: 解决通信
                                 +--------------------+
                     |---------> | BaseRequestHandler |<-----|
                     |           +--------------------+      |
                     |                               +----------------------+
                     |                               | StreamRequestHandler |
                     |                               +----------------------+
            +----------------------+
            | StreamRequestHandler |
            +----------------------+
''' # 多线程Socket: socketserver继承结构

'''
TCP多线程          
一、处理逻辑:
    1. 创建服务器 s = socketserver.ThreadingTCPServer(ip_port, MyServer)
       1) s.socket = socket(AF_INET,SOCK_STRAEM)
       2) s.server_bind() --> s.socket.bind()
       3) s.server_active() --> s.socket,listen()
    
    2. 运行服务器 s.server_forever()
       1) s.verify_request()                                # 在BaseSever类里面, 是一个钩子函数
       2) req, client_addr = s.socket.accept()              # 接受请求
       3） t = threading.Thread(target = process_request_thread,args = (req, client_addr))  # 为当前请求分配一个线程, 并指定处理函数
           t.start()
       *) 处理函数会创建myhandler = MyServer(req,client_addr,server_obj)对象, 其中handler方法会在创建时执行    

二、socketserver用法: 
     1. 继承socketserver.BaseRequestHandler, 重写定义自己的handler方法
        class MyServer(socketserver.BaseRequestHandler):           
            def handle(self):
                # 本连接内通信逻辑
                # 本线程可访问的属性有:
                        self.request = request                     # 本线程内的连接conn
                        self.client_address = client_address       # 客户端ip_port
                        self.server = server                       # 服务器对象
                        self.setup()                               # 钩子函数, 需要重写setup()方法
     
     2. 创建多线程的服务器
        s = socketserver.ThreadingTCPServer(ip_port, MyServer)     # 创建服务器对象
        s.serve_forever()                                          # 启动服务器, 会给每一个接入连接分配一个线程
        # 服务器对象可访问的属性有:
          s.server_address    # 服务器地址
          s.socket            # 服务器的socket对象    
    见: TCP_Server_SocketServer.py   
''' # 多线程Socket: TCP

'''
UDP多线程
一、处理逻辑:
    1. 创建服务器 s = socketserver.ThreadingUDPServer(ip_port, MyServer)
       1) s.socket = socket(AF_INET,SOCK_DGRAM)
       2) s.server_bind() --> s.socket.bind()
    
    2. 运行服务器 s.server_forever()
       1) s.verify_request()                                # 在BaseSever类里面, 是一个钩子函数
       2) data, client_addr = s.socket.recvfrom()           # 接受请求
                                                            # socketserver中返回的是 req = (data,socket)                                                    
       3） t = threading.Thread(target = process_request_thread,args = (req, client_addr))  # 为当前请求分配一个线程, 并指定处理函数
           t.start()
       *) 处理函数会创建myhandler = MyServer(req,client_addr,server_obj)对象, 其中handler方法会在创建时执行 

二、socketserver用法: 
     1. 继承socketserver.BaseRequestHandler, 重写定义自己的handler方法
        class MyServer(socketserver.BaseRequestHandler):           
            def hanle(self):
                # 本连接内通信逻辑
                # 本线程可访问的属性有:
                        self.request = request                     # 本线程内的req = (data,socket)
                        self.client_address = client_address       # 客户端ip_port
                        self.server = server                       # 服务器对象
                        self.setup()                               # 钩子函数, 需要重写setup()方法
     
     2. 创建多线程的服务器
        s = socketserver.ThreadingTCPServer(ip_port, MyServer)     # 创建服务器对象
        s.serve_forever()                                          # 启动服务器, 会给每一个接入连接分配一个线程
        # 服务器对象可访问的属性有:
          s.server_address    # 服务器地址
          s.socket            # 服务器的socket对象 
    
     见: UDP_Server_SocketServer.py                
''' # 多线程Socket: UDP
