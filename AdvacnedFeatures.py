'''
Advanced features: slice, iterable, list generation, generator, iterator
'''
'''
slice: A_new = A[n:m:i]  # [n,m) step-length: i; A: list/tuple
'''
# A = list(range(0,5,1))  # A = [0, 1, 2, 3, 4]
# print(A)
# A_new  = A[0:2:1] # A = [0, 1]
# print(A_new)

'''
iterable: list, tuple, dict, set, str, 
          for x in iterale:
          from collection import Iterable
'''
# A = list(range(0,5))
# for x in A:
#     print(x)
#
# A = tuple(A)
# for x in A:
#     print(x)
#
# d = dict(a=1,b=2,c=3)
# for x in d:
#     print(x)
#
# for key_value in d.items():
#     print(key_value)
#
# s = set(A)
# for x in s:
#     print(x)
#
# strs = 'xzq loves Cindy'
# for x in strs:
#     print(x)
#
# from collections import Iterable
# b = isinstance(A,Iterable)
# b1 = type(A)
# print(b,b1)

'''
list generation: [func(x) for x in iterable]
'''
# def func(x):
#     return x*x
#
# A = [0,1,2,3]
# A_new = [func(x) for x in A]
# print(A_new)


'''
generator: g = (func(x) for x in iterable)     # next(g);  for x in g:
           def func():
               yield value
               
           for x in iterator
'''
# def func(x):
#     return x*2
# A = [0,1,2,3]
# G = (func(x) for x in A)
# g1 = next(G)
# g2 = next(G)
# print(g1, g2)
# for x in G:
#     print(x)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b  = b, a + b
#         n = n + 1
#     return 'Done'
# g1 = next(fib(5))
# print(g1)
# for x in fib(6):
#     print(x)

'''
Iterator: generator, generator function, range()
          from collections import Iterator
          
          translate iterbable(list, tuple, dict, set, str):  __iter()__---iterable-->__next(iterable)__
                                                             for x in iterable(or iterator):
'''