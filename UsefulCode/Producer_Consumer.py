# -*- coding: utf-8 -*-
__author__ = 'xzq'

def Comsumer():
    while True:
        var = yield
        print('Comsumer {0} is running'.format(var))
        yield

def Producer():
    for i in range(1,10):
        print('Producer {0} is running'.format(i))
        c = Comsumer()
        next(c)
        c.send(i)

if __name__ == '__main__':
    Producer()
