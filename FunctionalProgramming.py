'''
Functional Programming: Features of functions, High-Order function, Closure, Anonymous functions, Decorator, Partial function
'''
'''
Features of functions: 1. variable could be function: x = abs
                       2. function could be variable: abs = 10
                       3. function could be arguments plunging into another function: def func2(x, y, func1): pass
                       4. function could be return value by another function(as Closure): def func2(): return func1
'''
# a = abs(-10)
# x = abs
# abs = 0
# print(a, x(-10), abs)

# def abs_sum(x,y,f):
#     print(f(x) + f(y))
# abs_sum(-10,-10,abs)

'''
High-order function: DON'T CHANGE THE ORIGINAL DATA
                     1. Iterator = map(func, Iterable) # map 'func' for x in Iterable
                     2. Iterator = filter(func, Iterable) # filter x for x in Iterable, if 'func' return True(False) then save(delete) x.
                     3. f(f(x1,x2),x3) = functool.reduce(f,[x1,x2,x3])
                     4. list = sorted(Iterable, key=func, reverse=True)  # list.sort() will change the original data.
'''
# Original_data = list(range(1,6))
# def Twice(x):
#     return x*2
# map_data = map(Twice, Original_data)
# for x in map_data:
#     print(x)
#
# def Biger(x):
#     if x > 3:
#         return True
#     else:return False
# filter_data = filter(Biger,Original_data)
# for x in filter_data:
#     print(x)
#
# def sum(x,y):
#     return x + y
# from functools import reduce
# print(reduce(sum,Original_data))

# # str2int: map, reduce
# from functools import reduce
# Digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
# def str2int(strs):
#     if not isinstance(strs,str):
#         raise TypeError('Wrong type of arguments. Please input string')
#     def char2num(s):
#         return Digits[s]
#     def num2dec(x,y):
#         return x * 10 + y
#     return reduce(num2dec, map(char2num,strs))
# num = str2int('41584654')
# print(num, type(num))

# A = [-9,0,1,-10,18]
# A_new = sorted(A, key=abs,reverse=True)
# print(A,A_new)
# A.sort(key=abs,reverse=True)
# print(A)

'''
Closure: 1. DEFINE: def func1():
                        paras
                        def func2():
                            pass
                        return func2
         2. DISCIPLINE: 1) The return value (func2) is a inner function, doesn't execute right now till call for it.
                        2) 'func2' could use paras of 'func1' whose paras saved in 'args'
                        3) Every call for 'func1' will return a new 'func2'
'''
'''
Closure: 1. DEFINE: def func1():
                       def func2():
                           pass
                       return func2
         2. DISCIPLINE: 1) The returned value (func2) is a inner function(Closure), doesn't execute right now till call for it.
                        2) 'func2' could use arguments of 'func1' which save in 'args'
                        3) Every call for 'func1' will return a new 'func2'
'''
# def func1(a,b=1,*args,**kwargs):
#     c = 3
#     def func2():
#         print(a,b,c,args,kwargs['d'])
#     return func2
# f = func1(1,2,4,5,d=6)
# print(f())

# def count(): # generate a list saving 3 function 'f'
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i  # the closure include the outer changeable variable 'i'
#         fs.append(f) # where 'f' is a closure will not execute right now till call for
#     return fs
# f1, f2, f3 = count()
# print(f1(),f2(),f3()) # execute 'f', but where i=3.

# def count_plus():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(f(i)) # where f(i) execute immediately, g is the closure.
#     return fs
# f1, f2, f3 = count_plus()  # where 'f1, f2, f3' are all Closure of 'g'
# print(f1(),f2(),f3())

'''
Anonymous Function: 1. DEFINE: lambda x: f(x)
                    2. QUALITY: 1) Only one f(x)
                                2) f2 = lambda x: f1(x)
                                3) def func2(): return lamdba x: f(x) # where the returned anonymous function is also a closure.
'''
# l = map(lambda x: x**2, list(range(1,6)))
# for x in l:
#     print(x)
#
# f = lambda x: abs(x)
# print(f(2))
#
# def area(r):
#     return lambda: r**2
# print(area(2)())

'''
Decorator: 1. DEFINE: not change the original function, and add some decorator qualities when the code running.
           2. STRUCTURE: 1) No para input:
                             Define Decorator:  def decorator(f):
                                                   @functools.wraps(f)        <--------so the function name is 'wraper', need to point to 'f'
                                                   def wrapper(*args, **kwargs):  ----                                            |
                                                       DECORATOR PART                |                                            |
                                                       return f(*args, **kwargs)     |<--- where wrapper as a closure to return---|
                                                   return wrapper                 ___|   
                             
                             Call For:         @decorator
                                               def f():
                                                   pass     # The essence is: 1) f = decorator(f), return 'wrapper'(closure)
                                               f()                            2) f(), call for 'wrapper()'
                                               
                        2) Para input:
                             Define Decorator:  def InputPara(a,b):
                                                    def decorator(f):
                                                       @functools.wraps(f)
                                                       def wrapper(*args, **kwargs):
                                                           CAN USE a,b
                                                           DECORATOR PART
                                                       return wrapper
                                                    return decorator
                             
                             Call For:   @InputPara(a,b)    # The essence is: 1) InputPara(a,b), return 'decorator'(closure)
                                         def f():                             2) f = decorator(f), return 'wrapper'(closure)
                                             pass                         
                                         f()                                  3) f(), call for 'wrapper()'
                                                    
                            
'''
# from functools import wraps
# def log(f):
#     @wraps(f)
#     def wapper(*args, **kwargs):
#         print('call %s' % f.__name__)
#         return f(*args, **kwargs)
#     return wapper
# @log
# def now():
#     print('2019-2-27')
# print(now.__name__)

# from functools import wraps
# def InputPara(d,e):
#  def decorator(f):
#     a, b , c = 1, 2, 3
#     k = {'a':0}
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         print(a,b,c,k['a'])
#         print(d,e)
#         return f(*args,**kwargs)
#     return wrapper
#  return decorator
# @InputPara(7,8)
# def f():
#     print('2019-2-27')
# f()

'''
Partial function: Preinstall the para into *arg or **kwargs
                  1. DEFINE: func2 = functools.partial(func,para, para=value) 
'''
# from functools import partial
# max10 = partial(max,10)
# print(max10(2,7,0))

