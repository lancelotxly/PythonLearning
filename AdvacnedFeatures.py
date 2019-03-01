'''
Advance features: slice, iterable/iterator, list generation, generator
'''
'''
slice: l_new = l[n:m:i] # where l is a Seq(list, tuple, str, dict), and be sliced into a new SubSeq from [n,m) with the Step-length: s
'''
# l = [0,1,2,3,4]
# l_new = l[0:3:1]
# print(l)
# print(l_new)


'''
Iterable: 1. DEFINE: an object called 'Iterable object' who implements '__iter__()'
          2. INCLUDE: list, tuple, str, dict, set, range(), generator, generator function
          
Iterator: 1. DEFINE: a 'Iterable object' who further implements '__next__(iterable)' called 'Iterator'
                     Specially, __iter__() --> Iterable object --> __next__(Iterable)
                     So, 'Iterator' must be 'Iterable'
          
          2. INCLUDE: generator, generator function
          
          3. Iterable to Iterator: Can use 'next(Iterator)'
                                   Iterator = iter(Iterable)

To distinguish: from collections import Iterable, Iterator
                isinstance(a, Iterable)
                isinstance(a, Iterator)

Traverse: for x in Iterable: # Iterable --> Iterator
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
#      print(x)
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
list generation: 1. DEFINE: def func(x): pass
                            [func(x) for x in iterable]
'''
# def func(x):
#     return x**2
# A = [-1,1,2,3]
# A_new = [func(x) for x in A]
# print(A, A_new)

'''
generator: 1. DEFINE: 1) def func(x): pass
                         g = (func(x) for x in Iterable)
                      2) def func(x): 
                            var = yield value1
                            yield value2
                         g = func(x)
           
           2. OPERATION: ONLY FOR ONCE
                         Get value: 
                                    1) next(g)  # return 'value1'
                                       # code  : can operate data right now.
                                       next(g)  # return 'value2'
                                    2) for x in g:
                         Get and Send value:
                                    3) g.send(None): return 'value1'
                                       g.send(value3): return 'value2', send 'value3' to 'var'
           
           3. Quality of yield: 1) Return value
                                2) Save status
                                3) Receive value 
           
           Using: 1)  Loading File Info: Save memory (based on Q1, Q2)
                  2)  Producer & Consumer Model: Concurrence (based on Q2, Q3)
'''
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