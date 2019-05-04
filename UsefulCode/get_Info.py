# -*- coding: utf-8 -*-
__author__ = 'xzq'

def get_info(filename,mode,encoding):
    with open(filename,mode,encoding=encoding) as f:
        for line in f:
            yield line

if __name__ == '__main__':
    user_info = get_info('test_data','r','utf-8')
    print(user_info)
    for i in user_info:
        print(i)