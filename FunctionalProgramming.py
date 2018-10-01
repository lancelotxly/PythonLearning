'''
Functional Programming: Features of functions, closure, anonymous function, decorator, partial function
'''

'''
Features of functions: 1. variable could be function:  x = abs
                       2. function could be variable:  abs = 10
                       3. function could accept other functions as parameters: def func2(x,y,func1)
                       4. function could return another function: 
                            def func1():
                                 return func2                                      
'''
# a = abs(-10)
# print(a)
# x = abs
# print(x(-10))
#
# a = abs(-10)
# abs = 10
# print(a, abs)
#
# def func(x,y,f):
#     return f(x)+f(y)
# sum = func(-10,9,abs)
# print(sum)

'''
iterator = map(f, iterable) 
iterator = filter(f,iterable)
iterator = reduce(f,iterable)
sorted(iterable, key = f, reverse = False)
'''
# A = [0,1,2,3]
# def f(x):
#     return x*2
# A_new = map(f, A)
# a=next(A_new)
# print(a)

# def f(x):
#    return x > 0
# A_new = filter(f,A)
# for x in A_new:
#     print(x)

# from functools import reduce
# Digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# def str2int(strs):
#     def char2num(s):
#         return Digits[s]
#     def f(x,y):
#         return x*10+y
#     return reduce(f,map(char2num,strs))
# num = str2int('123456')
# print(type(num))

# A = [-8,-3,-1,0,1]
# print(A)
# A_new = sorted(A,key=abs,reverse=True)
# print(A)

'''
closure: def func1():
            paras;
            def func2():
                pass
            return func2

         tips: 1. the returned function(closure) is a inner function, which could use the paras of the outer, and the paras were saved in args
               2. the closure could use other inner functions to achieve its purpose
               3. the closure doesn't execute right now untill call it
'''
# def lazy_sum(max):
#     def sum():
#         ax, n = 0, 0
#         while n < max:
#             ax = ax + n
#             n = n + 1
#         return ax
#     return sum
#
# f = lazy_sum(5)
# print(f())

'''
anonymous function:  lambda x: f(x)
'''
# l = map(lambda x:x*x, list(range(0,6)))
# for x in l:
#     print(x)

'''

'''