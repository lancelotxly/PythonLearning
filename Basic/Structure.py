'''
基本知识: 1. .py文件的结构
         2. .py文件的运行加载过程: 1) 初始化, 导入环境
                                2)  导入必要的modules, 内置模块
                                3） 从上到下动态运行代码: 1>. 对于定义的语法, 只导入不执行
                                                       2>. 调用时才执行
         3. .py文件的运行特点:  1) 可以动态的导入modules, 只要在调用之前
                             2) 可以动态的创建类, 只要在调用之前
                             3） 函数只有在调用时才执行                                              
'''
# -*- coding: utf-8 -*-              # 1. 起始行: 编码方式, 作者
__author__ = 'xzq'

'''                                  
this is a test module                
'''                                  # 2. 模块说明

import sys, os                       # 3. 导入模块

debug = True                         # 4. 全局变量

class ClassName(object): pass        # 5. 定义类

def func(): pass                     # 6. 定义函数

if __name__ == "__main__":           # 7. 主函数: 只在该.py文件下, 下面的代码才会运行, 一般用来测试本模块
    c = ClassName()
    func()