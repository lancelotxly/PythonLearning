# -*- coding: utf-8 -*-
import sys

__author__ = 'xzq'

import re
def HDB3_decode(str):
    Decode_dir = {
        '+000+':'10000',
        '-000-': '10000',
        '+000-':'10001',
        '-000+': '10001',
        '+00+':'0000',
        '-00-':'0000',
        '+00-':'1001',
        '-00+': '1001',
        '+':'1',
        '-': '1',
        '0':'0'
    }
    data_iter = re.finditer('(?:\+|\-)0{2,3}(?:\+|\-)|[0+-]',str)
    decode = ''
    for data in data_iter:
        decode = decode + Decode_dir[data.group()]
    return decode

if __name__ == '__main__':
    data_list = HDB3_decode('-000-+000+-+-00-+00+-+000-')
    print(data_list)
    print(sys.argv)

