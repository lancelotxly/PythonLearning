'''
DataModel: 1. INCLUDE: int, float, str, bool, None
                       list, tuple, dict, set, slice
           2. OPERATION: isinstance(a, DataModel)
                         type(a)
'''

'''
list: 1.DEFINE: l = [value] # where value can be all of DataModel
      2. OPERATION: Get: a = l[i]
                    Add: l[new_i] = new_value, l.append(value), l.extend(iterable), l.insert(i,value)
                    Delete: l.remove(value), l.pop([i]), l.clear(), del l[key]
                    Rewrite: l[i] = new_value
                    Search: count_value = l.count(value), value_index = l.index(value)
                    
                    Sort: l.sort([key=function], [reverse=True]), l.reverse(), l_length = len(l)
      3. list(Seq): 1. translate Sequence(list, tuple, str) into list
                    2. Copy: l1 = [1,2,3]
                             l2 = list(l1)
'''
# A = [1, 2.4, 'xzq', True, None]
# A_length = len(A)
# a0, a1, an = A[0], A[1], A[-1]
# print(A, A_length, a0, a1, an)
# # Add
# A.append('Xiao')
# A.extend([7,8,9])
# A.insert(len(A),'John')
# print(A)
# # Search
# A.remove(True)  # True will equal 1 when count
# count_o = A.count(1)
# print(count_o)
# # Delete
# A.remove('Xiao')
# A.pop()
# print(A)
# A.clear()
# print(A)
# # Rewrite
# A.append('John')
# print(A)
# A[0] = 'xzq'
# print(A)

'''
tuple: READ ONLY, others same to list.
       Copy: t1 = (1,2,3)
             t2 = tuple(t1)
'''
# A = (1, 2.4, 'xzq', True, None)
# print(A[0])
# # A[0] = 2  # error!
# a = 1, 2, 3  # generate tuple package automatically.
# print(a)

'''
dict: 1. DEFINE: d1 = {key1: value1, key2: value2,...} # where 'key' are unchangeable, as number(int, float), str or tuple
                 d2 = dict(**kwargs) # dict(key1=value1, key2=value2,...)
                 d3 = dict([(key1, value1),(key2, value2),...])
      2. OPERATION: Get: a = d[key], a = d.get(key)
                    Add: d[new_key] = new_value
                    Delete: d.pop(key), del d[key]
                    Rewrite: d[key] = new_value
                    Search: a = d[key], a = d.get(key)
                    
                    Copy: d1 = {'a':1, 'b':2}
                          d2 = dict(d1)
                    
                    Traverse: for key in d.keys():
                              for value in d.values():
                              for key, value in d.items():
                              
'''
# d1 = {'a':1,'b':2,'c':3}
# d2 = dict(a=1,b=2,c=3)
# d3 = dict([('a',1),('b',2),('c',3)])
# print(d1,d2,d3)
# # Add
# d1['d'] = 4
# print(d1)
# # Delete
# d1.pop('c')
# print(d1)
# # Rewrite
# d1['a']='xzq'
# print(d1)
# # Search
# value = d1.get('b')
# print(value)

'''
set: NO REPEAT, DISORDER, NO TRAVERSE
     1. DEFINE: s = set(list/tuple)
                {value1, value2,...}
     2. OPERATION: Get: s.pop()
                   Add: s.add(key)
                   Delete: s.remove(key)
                   Get: s.pop()
                   Intersection: s1 & s2
                   Union set: s1 | s2
'''
# s1 = set([1,2,3])
# s2 = set(('a','b','c'))
# s3 = {None}
# s1.add(4)
# s2.add('d')
# print(s1, s2, s3)
# # Intersection & Union
# s1_inter_s2 = s1 & s2
# print(s1_inter_s2)
# s1_Union_s2 = s1 | s2
# print(s1_Union_s2)

