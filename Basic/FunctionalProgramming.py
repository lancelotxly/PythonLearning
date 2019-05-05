'''
函数式编程: 
           1) 函数的特性 Features of function
           2) 高阶函数   High-Order function
           4) 闭包      Closure
           5) 匿名函数   Anonymous function
           6) 装饰器     Decorator
           7）偏函数     Partial function
''' # 综述

'''
函数的特性: 
         1. 变量可作函数: x = abs
         2. 函数可作变量: abs = 10
         3. 可以将一个函数func1作为参数传给func2: def func2(x, y, func1)
         4. 函数func1可以作为func2的返回值:  def func2(): return func1
''' # 函数的特性

'''
高阶函数: 同样符合函数的基本特性
        1. map:     iterator = map(func, iterable)       # 返回一个迭代器, 将func函数作用到iterable_obj的每个元素上
        
        2. filter:  iterator = filter(func, iterable)    # 返回一个迭代器, 仅包含func返回值为True的元素
        
        3. reduce:  f(f(x1,x2),x3) = functools.reduce(f,[x1,x2,x3])     
        
        4. sorted:  list = sorted(Iterable,key=func,reverse=True) # 返回一个list, 不改变原来的数据; list.sort(key=func)会改变
        
        5. max/min:  num = max(iterable, key=func)     # 返回最大值
                     num = min(iterable, key=func)     # 返回最小值
        
        6. zip:   iterator = zip(Seq1, Seq2)  # 输入两个Seq, 合上拉链, 返回一个迭代器, 每项是一个tuple
                  iterator = zip(*list_tuple) # 返回一个迭代器, 打开拉链                
                     
        7. pow:  num = pow(a,b)        # num = a**b
        
        8. round: num = round(3.5)     # 四舍五入
        
        9. slice: s = slice(n,m,i)     # 生成切片对象              
                    
        10. eval:  r = eval('str')     # 将'str'作为表达式运行, 返回运行结果             
        
        11. enumerate(Seq):            # 返回一个迭代器, 每一项是一个tuple包括(i,value)
        
        12. input('str')               # 输入值, 返回一个字符串            
''' # 高阶函数

'''
闭包:
    1. 定义:
           def func1():
              def func2():pass
              return func2
    2. 规则:
           1) 返回一个内部函数, 不会立即执行, 直到调用才执行
           2) func2可以向上使用func1的参数
           3) 每一次调用func1都会返回一个新的func2, 内存地址不同          
''' # 闭包

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
匿名函数: 
        1.定义:  lambda x: f(x)
        
        2.特点:  
               1) 只能有一个函数f(x)
               2) 匿名函数同样满足函数的基本特性
               3) 匿名函数也可以作为闭包返回, 性质一样
               4) 使用一次就释放, 命名后不释放, 一般不命名, 一次性使用
        
        3. 应用场景: 高阶函数中
                    map, filter, reduce, sorted, max, min
''' # 匿名函数

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
    装饰器: 
       1. 定义: 
              1) 不改变原有的代码
              2) 不改变原来的调用方式
              3) 添加了新的功能
       
       2. 结构: 
             1) 无参数传入的装饰器
                定义: 
                    def decorator(f):
                      @functools.wraps(f)    <----   所以这里将wrapper闭包的内存地址重新指向了f
                      def wrapper(*args, **kwargs):
                         # 新功能                     <--- 执行新的功能(可交换) 
                         value = f(*args, **kwargs)  <--- 执行原生的f(可交换)
                         return value                <--- 返回值一定要是原来的, 不能改变原来函数的执行结果
                      return wrapper      <--- 这里返回的是wrapper的闭包给f, 因此f的内存地址与原来不同了       
                调用:  
                     @decorator
                     def f(*args,**kwargs): pass        #1. @decorator -->  执行f = decorator(f), 返回wrapper闭包
                     f(*args,**kwargs)                  #2. f() = wrapper() 执行wrapper()                   
                                                
             2) 有参数输入的装饰器
                定义:
                    def InputPara(a,b):
                       def decorator(f):
                         @functools.wraps(f)
                         def wrapper(*args, **kwargs)
                             # 新功能,可以使用a,b
                             value = f(*args,**kwargs)
                             return value
                         return wrapper
                       return decorator
                调用:
                    @InputPara(a,b)                      #1. 执行InputPara(a,b), 返回decorator闭包
                    def f(*args,*kwargs):pass            #2. @decorator(f) --> 执行f = decorator(f), 返回wrapper闭包
                    f(*args,**kwargs)                    #3. f() = wrapper() 执行wrapper()         
''' # 装饰器

# from functools import wraps
# def log(f):
#     @wraps(f)
#     def wapper(*args, **kwargs):
#         print('call %s' % f.__name__)
#         return f(*args, **kwargs)
#     return wapper
# @log
# def now(str):
#     print(str)
#     print('2019-2-27')
# now('execute')




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


# # Authenticate
# import  functools
# def auth_func(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         username = input('username: ').strip()
#         password = input('password: ').strip()
#         if username == 'xzq' and password == '123':
#             return func(*args, **kwargs)
#         else:
#             print('Wrong username or password')
#     return wrapper
# @auth_func
# def home():
#     print('Welcome')
# home()

# Session
# user_dict = {'xzq':123,'Jerris':456}
# current_user = {'username':None, 'status':None}
# import functools
# def auth(f):
#     @functools.wraps(f)
#     def wrapper(*args,**kwargs):
#         if current_user['status'] == 'login':
#             return f(*args,**kwargs)
#         else:
#             username = input('username: ').strip()
#             if username in user_dict:
#                 password = input('password: ').strip()
#                 if user_dict[username] == int(password):
#                     current_user['status'] = 'login'
#                     current_user['username'] = username
#                     return f(*args,**kwargs)
#             else:
#                 print('用户名不存在')
#     return wrapper
#
# @auth
# def home():
#     print('Welcome %s' % current_user['username'])
#
# @auth
# def index():
#     print('Session success')
#
# home()
# index()

'''
偏函数: 提前将部分参数存入*arg或**kwargs中
       1. 定义:
              func2 = functools.partial(func, a, b=2)
''' # 偏函数

# from functools import partial
# max10 = partial(max,10)
# print(max10(2,7,0))


# 下一章: Modules.py

