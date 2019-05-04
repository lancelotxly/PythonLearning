# -*- coding: utf-8 -*-
__author__ = 'xzq'

'''
1. HTTP:
       特点: 1>. 请求/响应模式
            2>. 无状态协议, Client每一次访问都会被Server当作是第一次访问 (Cookie, Session)

       Request:
                     POST /index.html HTTP/1.1     # 请求方法  url  协议版本
             Header: Host: www.bilibili.com        # 请求域名  --> DNS
                     Connection:  keep-alive       # 链接方式
                     User-Agent:  浏览器类型
                     Accept: text/html             # 能接收的文件类型
                     Accept-Encoding: gzip         # 能接收的压缩方式
                     Accept-Charset: GB2312        # 能接收的编码方式
                     Cookie: 再次访问的cookie码
                     Content-Type: text/html       # 请求体的数据类型
                     Content-Length: 13            # 请求体的长度

             Body:   name=xzq&age=18               # 请求体， GET没有会把数据之间放到URL ； POST会把Body数据中的中文采用URL编码到URL上


       Response:
                     HTTP/1.1 200 OK               # 协议版本 状态码
             Header: Server: Web服务器版本
                     Content-Type: text/html       # 响应体文件类型
                     Content-Length: 724           # 响应体长度
                     Set-Cookie: 发给客户端的Cookie
                     Date: 响应时间

             Body:   # html 文件, 图片, 音乐, 视频, JS, CSS 分别发送

             响应码:   2xx   成功:            200
                      3xx   重定向:          302 永久重定向, 301 暂时重定向, 304 请求内容没变化，不重发
                      4xx   客户端错误        404 找不到, 401 未认证, 403 访问被禁
                      5xx   服务端错误        500 服务器出错
'''   # HTTP

'''
Web 流程:
        Client  <--->  Web服务器: HTTP解析软件 <-> [WSGI] <-> Web app (服务器逻辑, 即Web框架)
        
Web app 组成:  MVC, MTV  
            控制器 Controller:        路由分发
            数据库 Model:             操作数据库
            视图函数 ViewFunction:    处理逻辑         ___
            模板    Template:        动态生成html     ___|
            
'''
from wsgiref.simple_server import make_server
import time
def web():
    with open('Simple/index1.html','rb') as f:
        data = f.read()
    return [data]
def xzq():
    with open('Simple/index2.html','rb') as f:
        data = f.read()
    return [data]

def current_time():
    with open('Simple/index3.html','rb') as f:
        data = f.read()
    now = time.ctime(time.time())
    data = str(data,'utf8').replace("{{time}}",str(now))
    return [data.encode('utf8')]

def router():
    url_pattern = (
        ('/web',web),
        ('/xzq',xzq),
        ('/current',current_time)
    )
    return url_pattern

def application(environ,start_response):
    path = environ['PATH_INFO']
    start_response('200 OK', [('Content-Type', 'text/html')])

    url_pattern = router()
    func = None
    for item in url_pattern:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return func()
    else:
        return [b'<h1>4o4 Not Found!</>']

httpd = make_server('',8000,application)

print('Serving HTTP on port 8000..')   # 阻塞直到有连接

httpd.serve_forever()