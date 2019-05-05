'''
高级特性:
        1. slice :             切片
        2. iterable/iterator:  可迭代对象, 迭代器
        3. list generation:    list推导式
        4. generator:          生成器
''' # 综述

'''
slice: 切片
      1. 定义:
              l_new = l[n:m:i]  # l为一个序列(list,tuple,str,dict.keys())
                                # l_new为切片后的一个新序列, 是一种深拷贝
                                # 切片[n:m), n从0开始, 可设置切片步长为i
      2. 方法:
             s = slice(n,m,i)   # 生成slice对象, 可多次使用
             l_new = l[s]                         
''' # slice

'''
Iterable: 可迭代对象, 只是一种类型, 不能迭代取值
         1. 定义: 实现了__iter__(): return iterable_obj 方法的对象叫iterable
         2. 默认有: list, tuple, str, dict, set, range(), generator
          
Iterator: 迭代器, 由iterator = iter(iterable_obj)生成
          1. 定义: 首先是一个iterable对象, 进而实现了__next__(iterable)方法的, 叫迭代器. 
                  迭代器一定是可迭代对象
          
                  1> __iter__(): return iterable_obj      # 返回可迭代对象
                  2> __next__(iterable): return value     # 定义怎样通过该iterable对象取值 
          
          2. 包括: generator
          
区分迭代器和可迭代对象: 
                   from collections import Iterable, Iterator
                   isinstance(a, Iterable)
                   isinstance(a, Iterator)

Iterable生成Iterator: 1. iterator = iter(iterable)     # 主动调用__iter__()方法
                     2. for x in iterable:            # 遍历时会自动调用__iter__()方法 
''' # Iterable & Iterator

'''
list generation: 列表推导
                1. 定义:
                       def func(x):pass
                       l = [func(x) for x in iterable]
                2. 特点: 会一次性遍历所有的元素, 运行func, 返回一个新的list       
'''  # 列表推导

'''
generator: 生成器
           1. 定义:
                  1> def func(x):pass
                     g = (func(x) for x in iterable)
                  2> def func(x):
                        # other_code1
                        var = yield v1
                        # other_other2
                        yield
                     g = func(x)
           2. 特点: 
                  1> 执行__next__()方法时才开始迭代
                  2> 只能遍历一次
                  3> 超出则报错StopIteration
           3. 操作:
                  1> 对于普通generator, 只能取值
                    next(g):     直到raise StopIteration
                    for x in g:  遍历
                    
                  2> 对于generation function, 利用yield可以取值, 可以传值 
                     yield特性:  
                                1) 返回值
                                2) 保存状态, 下次从yield执行
                                3) 可以传入值
                     取值: 
                          1) next(g)         # 返回v1
                             # other_code    # 执行其他代码
                             next(g)         # 返回v2
                          2) for x in g:     # 遍历
                     传值: 
                          def func(x):
                            # other_code1
                            var = yield v1
                            # other_other2
                            yield
                          g = func(x)    
                          1) v1 = next(g)    # 进入generator, 执行other_code1, 返回v1
                          2) g.send(v2)      # 传入v2到var, 执行other_code2             
           
           应用:
                1) 制作文件读取生成器:
                   def get_info(filename,mode,encoding):
                        with open(filename,mode,encoding=encoding) as f:
                            for line in f:
                                yield line 
                   g = get_info('filename')
                   for line in g: 
                      print(line)  
                                                                                 
                2) 生成者, 消费者模式: 
                   利用任务A阻塞的前分配去执行任务B, 实现并发
'''  # 生成器

# 下一章: Functions.py






# def Fibonacci(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n = n + 1
#     return 'Done'
# f = Fibonacci(6)
# for x in f:
#     print(x)


# def test():
#     print('Begin')
#     first = yield 1
#     print('First', first)
#     yield 2
#     print('Second')
# t = test()
# res = next(t)
# print(res)
# res2 = t.send('123')
# print(res2)


# def get_Info(filename):
#     with open(filename, 'r', encoding='utf-8') as f:
#         for line in f:
#             info = eval(line)
#             yield info
# g = get_Info('Information')
# all_pop = sum(p['population'] for p in g)
# g = get_Info('Information')
# for i in g:
#     print('%s : %.1f' % (i['name'], i['population']/all_pop))


# def Consumer():
#     while True:
#         var = yield
#         print('Consumer is running')
#         yield
#
# def Producer():
#     while True:
#         print('Producer is running')
#         c = Consumer()
#         next(c)
#         c.send(None)
# Producer()