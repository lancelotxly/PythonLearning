'''
Data Model: int float str bool
            list tuple dict set

isinstance(a, DataModel)
type(a)
'''
'''
list: len(A), A[i],
      A.append(DataModel), A.extend(iterable), A.insert(i, DataModel), A.remove(DataModel), A.count(e), A.clear(), A.index(e)
      A.pop([p]), A.reverse(), A.sort([key=function], [reverse])
      list()  # translate sequence into list
'''
# A = [1, 2.4, 'xzq', True]
# l_A = len(A)  # l_A = 4
# a1, a2 = A[1], A[-1]  # a1 = 2.4, a2 = True
# print(A, l_A, a1, a2)
#
# A.append(['Cindy'])  # A = [1, 2.4, 'xzq', True, ['Cindy']]
# print(A)
#
# a3 = A.pop()  # a3 = ['Cindy']
# print(a3)
#
# A.extend(['Cindy'])  # A = [1, 2.4, 'xzq', True, 'Cindy']
# print(A)
#
# A.insert(-2, 'love')  # A = [1, 2.4, 'xzq', 'love', True, 'Cindy']    A.insert(i,value) insert 'value' before i
# print(A)
#
# A.remove(2.4) # A = [1, 'xzq', 'love', True, 'Cindy']
# print(A)


'''
 tuple: read only
        len(A), 
        list(tuple)  translate tuple to list
'''
# A = (1, 2.4, 'xzq', True)
# l_A = len(A)
# print(A, l_A)
#
# list_A = list(A)
# print(list_A)

'''
dict:  D = {key1: value1, key2: value2,...},
       d = D[key1], D.pop(key1), D[key_new] = value_new
       for key, value in D.items():
       for key in D.keys():
       for value in D.values():
       
       d1 = dict(a=1, b=2, c=3)  # d1 = {'a':1, 'b':2, 'c':3}
       d2 = dict([('a',1), ('b',2), ('c', 3)]) # d2 =  {'a':1, 'b':2, 'c':3}
'''
# D = {1: 'a', 2: 'b', 'xzq':'Cindy'}
# d_value = D['xzq']     # d_value = 'Cindy'
# d_value2  = D.get(1)   # d_value2 = 'a'
# print(D, d_value, d_value2)
#
# D.pop(2)     # D = {1:'a', 'xzq':'Cindy'}
# print(D)
#
# D[2] = 'b'  # D = {1: 'a', 'xzq': 'Cindy', 2: 'b'}
# print(D)
#
# for key, value in D.items():  # 1 = a; xzq = Cindy; 2 = b
#     print(key, '=' , value)
#
# for key in D.keys():
#     print(key, end=' ')
#
# for value in D.values():
#     print(value, end = ' ')
#
# d1 = dict(a=1, b=2, c=3, d='xzq', e='Cindy')
# print(d1)
#
# d2 = dict([('a', 1), ('b',2), ('c',3)])
# print(d2)

'''
set:  s = set(list/tuple)
      s.add(key)
      s.remove(key)
      s1 & s2  # intersection
      s1 | s2  # union set

'''
# s1 = set([1,2,2,3])  # s = {1,2,3}
# print(s1)
#
# s1.add(0)  # s = {0, 1, 2, 3}
# print(s1)
#
# s1.remove(1)  # s = {0, 2, 3}
# print(s1)
#
# s2 = set(list(('xzq','love','Cindy')))
# s = s1 & s2    # s = set{}
# print(s)
#
# s = s1 | s2  # s = {0, 'xzq', 2, 3, 'Cindy', 'love'}
# print(s)

