'''
Sequence:
         Classified by function:
                  Container:  # contain the reference of arbitrary object
                            list, tuple
                  Flat:  # only include one type data
                         str, array.array, memoryview, bytes
         Classified by mutable or not:
                  MutableSequence: list, array.array, memoryview, bytearray
                  NotMutableSequence: tuple, str, bytes
         MutableSequence has: __setitem__, __delitem__, __iadd__ +=, __imul__, insert(i,v), append(i), reverse(), extend(v), pop([v]), remove(v)
            NotMutableSequence has: __getitem__, __reversed__, __add__ +, __mul__ *, index(v), count(v), sort([key],[reverse])
                  Container:  __contains__
                  iterable:  __iter__  (iterator: __next__(iterable))
                  Sized:     __len__

         Slice:  1. define
                    s[n:m:step]
                    1). exclude s[m], because that can calculate data_length easily, i. e.  data_length = m-n
                    2). step can be negative, which means slicing reversed
                    3). 's' is a slice(start, stop, step) object, and we can name the slice to make simply to following.
                 2. operation
                    s[n:m] = iterable
                    del s[n:m]
                 there is a note that for any slices of sequence still are sequence object, even for the slice with only one element, e.g. s[:1]

         Joint: '+','+=' # the two sides must have the same DataStructure, e.g all 'list','tuple','str' or 'array'
                '*', '*=' # copy and extend the original sequence to n-folds
                where __iadd__ +=, __imul__ *= are original address operation, more efficient, but the operation doesn't have atomic.
                __add__ +, __mul__ * don't change the original data, and assign a new address to the new sequence
                e.g. build a list which makes up by lists
                    board = [[] * 3 for i in range(3)]


         Sort and Search:
               Sort:
                   sequence.sort([key=func], [reverse=True/False])  operation on original address
                   sorted(sequence, [key=func],[reverse=True/False])  return a new sequence
               Search:  import bisect

'''
'''
Tuple:  1. as a not mutable list, only focus on 'data' unchanged
        2. as a record, the 'location' and 'total' of the 'data' are also important

unpacking: 1. parallel assignment paras
           2. 'for var_1, var_2,.. in iterable:' unpacking, the type of var_n must follow the iterable object type
               means: 1. the number of vars must same the the counterpart in iterable object. If the var_i is not necessary, use '_' to instead.
                      2. for nested unpacking, 
                         e.g  IterableObject = [a,b,(c,d),[e]]
                         then the vars must be organized by
                              var_1, var_2, (var_3, var_4), [var_5]
           3. as the paras tuple plunge into the function
              paras = (a,b,c..)
              function(*paras)
           4. organize the rest paras, which can lies on any locations
              a, b, *rest
              a, *rest, b
              
numedtuple (packing): 1. define
                         Tuple_name = namedtuple('Tuple_name', iterable) 
                         # where iterable object includes the fields info of the tuple, could be
                         'attr1 attr2 .. attrn' or
                         ['attr1', 'attr2',...'attrn']
                      2. methods and attr exclude the attrs inherited from Tuple
                         Tuple_name._fields   # the field info of the namedtuple, i.e. 'attr1, attr2,...attrn'
                         info_data; Tuple_name._make(info_data)  # same as definition
                         namedtuple._asdict()  # the  fields and corresponding info data
                         
operation: see NotMutableSequence
'''
# # unpacking, parallel assignment
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# traveler_id = [('USA','123456'),('BRA','CE54879')]
# # 'for i in iterable' means unpacking (the list)
# for passport in sorted(traveler_id):
#     print('%s %s' % passport)
#  # enforce unpacking (the tuple), and the number of variables (where 'country', '_') must follow the iterable object.
# for country, _ in traveler_id:
#     print(country)
# # unpacking, *tuple as the parameters into the function
# t = (20,8)
# p = divmod(*t)
# print(p)
#
# a, b, *rest = range(5)  # packing rest paras, *args
# print(a, b, rest)
# a, * rest, b = range(5)  # and can lies in any location
# print(a, rest, b)
#
# # unpacking in nested case, the variables must follow the iterator object.
# metro_areas = [('Tokyo','JP','36.933',('35.12458','68.15821'))]
# for name, cc, pop, (latitude, longitude) in metro_areas:
#     print(name, cc, pop, latitude, longitude)

# from collections import namedtuple
# City = namedtuple('City',['name', 'country', 'population', 'coordinates'])
# tokyo = City('Tokyo','JP', 36.265, (35.264,154.6))
# print(tokyo)
# delhi_data = ('Delhi', 'IN', 5484, (65, 215))
# delhi_data = City._make(delhi_data)
# print(delhi_data._fields)
'''
List comprehension (listcomps):  [ f(x) for x in iterable if condition] ==  list(filter(condition, map(f, iterable)))
                        can only generate a complete list, not other type sequence
'''
# # Cartesian product
# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# tshirts = [(color, size) for color in colors
#            for size in sizes]
# print(tshirts)

# # Listcomps == filer, map
# symbols = '$&*^#'
# ascii_liscomps = [ord(s) for s in symbols if ord(s) > 0 ]
# ascii_filtermap = list(filter(lambda x: x > 0, map(ord, symbols)))
# print(ascii_liscomps, ascii_filtermap)

'''
Generator :  Iterator, Iterable
             1. generator expression (genexps)
             2. generator function
'''
# import  array
# # make a generator
# # 1. genexps
# symbols = '$#%@'
# ascii_g = (ord(s) for s in symbols)
# # 2. generator function
# def generator_fun(symbols):
#     data_length = len(symbols)
#     for i in range(0,data_length):
#         yield ord(symbols[i])
#     return 'Done'
# # Generate any type of data, based on the generator(Iterator), whose essence is to get the data by using 'next(generator)', then generator is StopIterable
# A = array.array('I', generator_fun(symbols))
# ascii = tuple(ascii_g)

'''
array: more efficient than list, tuple 
       1. define
          array('d', iterable)  # float array
          array('b', iterable)  # signed int -128~127
          array('I', iterable)  # unsigned int
          array('h', iterable)  # array_length = 2**15, signed int
       2. operation see MutableSequence and the new
          the file operation:
          .tofile(fp), .fromfile(fp, data_length)
'''
# from array import array
# from random import random
# floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])
# fp = open('floats.bin','wb')
# floats.tofile(fp)
# fp.close()
# floats2 = array('d')
# fp = open('floats.bin','rb')
# floats2.fromfile(fp,10**7)
# fp.close()
# print(floats2[-1])

'''
memoryview: share the memory of the original array, can operate the slices of the array without copying it.
            1. define
               memo = memoryview(array)
            2. operation same to array
               and more:  memo_new = memo.cast('d/b/I/B')  # transform type   
               
            struct: package bytes into tuple 
                   struct.unpack(fmt, memoryview/bytes/bytearray)            
'''
# from array import array
# num = array('h',list(range(7)))
# memo = memoryview(num)
# memo_new = memo.cast('B')
# del memo, memo_new