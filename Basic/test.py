# -*- coding: utf-8 -*-
__author__ = 'xzq'




def ip_to_int(ip):
    def int2bin(ip_part):
        int_num = int(ip_part)
        bin_num = bin(int_num)
        bin_num = bin_num.lstrip('0b')
        return bin_num.rjust(8,'0')
    ip_part_list = ip.split('.')
    ip_part_iterator = map(int2bin,ip_part_list)
    joint = ' '
    return joint.join(ip_part_iterator)

if __name__ == '__main__':
    ip = '10.3.9.12'
    print(ip_to_int(ip))
