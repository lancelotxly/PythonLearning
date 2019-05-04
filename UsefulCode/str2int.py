# -*- coding: utf-8 -*-
__author__ = 'xzq'

from functools import reduce
def str2int(str):
    DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

    def char2num(c):
        return DIGITS[c]

    def num2int(x,y):
        return x * 10 + y

    num = reduce(num2int, map(char2num, str))
    return num

if __name__ == "__main__":
    num = str2int('4678974')
    print(num, type(num))