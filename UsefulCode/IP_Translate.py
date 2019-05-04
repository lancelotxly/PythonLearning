# -*- coding: utf-8 -*-
__author__ = 'xzq'

import re

class IP_Translate(object):
    def IP_to_Bin(self,ip,joint='.'):
        if self._ip_validate(ip):
            ip_part = ip.split(joint)
            bin_iter = map(self._int2bin,ip_part)
            bin_str = joint.join(bin_iter)
            return bin_str
        else:
            return 'IP地址格式错误'

    def Bin_to_IP(self,bin_ip,joint='.'):
        bin_part = bin_ip.split(joint)
        ip_iter = map(self._bin2int,bin_part)
        ip_str = joint.join(ip_iter)
        return ip_str

    def _ip_validate(self, ip):
        ip_re = re.compile(r'((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?$)')
        if ip_re.match(ip):
            print(ip_re.match(ip).group())
            return True
        else:
            return False

    def _int2bin(self, num):
        num = int(num)
        bin_part = bin(num).lstrip('0b').rjust(8,'0')
        return bin_part

    def _bin2int(self,num):
        num = str(num)
        ip_part = int(num,2)
        return str(ip_part)

if __name__ == "__main__":
    ip_tranlater = IP_Translate()
    bin_str = ip_tranlater.IP_to_Bin('10.3.12.7',)
    ip_str = ip_tranlater.Bin_to_IP(bin_str)
    print(ip_str)