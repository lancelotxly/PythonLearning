'''
dict:
     1. API (collections.abc)
        MutableMapping: __setitem__, __delitem__, clear, pop(k,[default]), popitem, setdefault(k,[default]), update(m,[**kargs]), popitem, fromkey(iterable,[initial])
            Mapping:  __getitem__, __eq__ =, __ne__ !=, get(k,[default]), items, keys, values
               Container: __contains__ in
               iterable: __iter__
               Sized:  __len__
        # this is a formal document, in practice we define 'dict' always by extending 'dict()' or 'collections.User.Dict()'

     2. hashable & unhashable
        hashable:  implement __hash__, __eq__; if a == b is true, hash(a) == hash(b) must be true.
                   NotMutableSequence atomically (i.e tuple, str, bytes, num)
                   my_class
        unhashable: DataModel which contains MutableSequence (i.e. list, array.array, memoryview)
        * the keys of dict or the elements of set must be hashable

     3. definition
        dict(key1=value1,...)
        {'key1':value1,...}
        dict(zip(iterable_keys, iterable_values))
        dict([(key1, value),...])
        dict({'key1':value1,...})

     4. dict comprehension:
        { key: value for value in values for key in keys if condition}  # where 'values' and 'keys' are iterable sequence
        or {key:value for key, value in iterable}  # where 'iterable' is a list which composed by tuples

To avoid  KeyError, we always get key-value by: d.get(k,default)
However, When key-value doesn't find by  __getitem__ d[k], there are two method to avoid KeyError and return default value:
1) define a child my_dict which inherits from dict(), and implements __missing__() that generates default value when key not found.
2) collections.defaultdict(d.default_factory, key=value)
   where d.defaul_factory is callable or None which is used to generate default value for returning, when __missing__() calls for
   and the operation flow is:  1. __getitem__() d[k] not found,
                               2. calls for __missing__(),
                               3. __missing__() calls for d.default_factory
                               4. d.default_factory is a callable object(function) to generate default value
   for collections.defaultdict, other operations same to dict()

Other dictionary:
   collections.OrderedDict:  1. definition same to dict
                             2. operation:
                                1) d.move_to_end(k,[last=True/False]) # move the k-v to the head or tail
                                2) __reversed__()  # d_new = reversed(d)
                                others same to dict
   collections.ChainMap: combing some dicts and search integrally, when the first satisfied 'key' be find out and return corresponding value
                            C = ChainMap(d1,d2,..)
                         operations same to dict
   collections.Counter:
   collections.UserDict: a convenient super class than dict(), which has a field, i.e. UserDict.data = d, where d is a object of dict()
                         Other operations same to dict

NotMutableDict: from types import MappingProxyType
                d = {1:'A'}
                d_proxy = MappingProxyType(d)
                where 'd_proxy' is read only, and 'd' can be read and written.

set:  Iterable, unhashable
     1. definition
        1) set(Iterable)  # where Iterable must be hashable
        2) {1,2,3..} and empty set must be 'set()'  # more efficient
     2. set comprehension
        {i for i in iterable if condition}
     3. API
        MutableSet: add(e), discard(e), remove(e)[# raise KeyError], pop(e) [# raise KeyError], clear, __ior__(S |= N), __iand__(S &= N), __ixor__(S ^= N), __isub__(S -= N)
            Set: S.isdisjoint(Z), __le__(S <= Z), __lt__(S < Z) , __ge__(S >= Z), __gt__(S > Z), __eq__(S == N), __ne__(S != N), __and__(S & N), __or__(S | N), __sub__(S - N), __xor__(S ^ N)
              Container: __contains__
              Iterable:  __iter__
              Sized: __len__

The performance of searching in dict > set >> list, because the essence of dict or list is 'hash table'
Hash Table:
          1. is a  sparse array (always has empty buckets)
          2. where bucket is the element of the hash table, which is composed by 'key-reference' and 'value-reference'
          3. Python will ensure the third of array be empty, and when the data reach the threshold, Python will copy the existing data into a bigger array.
   write into the hash table: 1. compute the hash value, by the implemented __hash__
                              2. make sure that if a == b is true, then (__eq__) hash(a) == hash(b)
                              3. make sure the similar value reserved in distant places
   get data:  d[k]
              1. calculate k's hash value, h_k = hash(k)
              2. search by parts of h_k --> found_k: found_value, if found_value empty, return KeyError; or check whether k == found_k
              3. if right, return found_value; or 'hash conflict' return 1 and add more h_k to search
   advantages: efficient in time
   disadvantages: not efficient in space, and add new key will change the existing order of key.

'''
# # dict.pop(k,[default])
# d = dict(a=1,b=2,c=3)
# d.pop('d',None)   # pop d[k], if not exists return 'default'
# # dict.get(k,[default])
# d.get('d',None)   # get d[k], if not exists return 'default'
# # dict.setdefault(k,[default])
# e = d.setdefault('d',[])  # set d[k] = default, whenever 'k' exists or not, and return d[k], can be used to update key-value
# # dict.update(m,[**kargs])
# d.update(a=3)  # update d['a']=3
# d.update(d,a=4)
# d.update(d,new_key=10) # add new_key
# # dict.fromkey(iteable,[initial])
# d1 = d.fromkeys(list(range(3)),1)  # return a new initialized dict
#
#
# # # inherits from dict and implements __missing__()
# class my_dict(dict):
#     def __init__(self,**kwargs):
#         super().__init__(**kwargs)
#
#     def __missing__(self, key):
#         return None
# d = my_dict(a=1,b=2)
# print(d['d'])
# # inherits from dict
# class my_dict(dict):
#     def __missing__(self, key):
#         if isinstance(key,str):   # if the key is already str, raise to KeyError and return 'default'.
#             raise KeyError(key)   # Because, when __missing__ is called for which means the 'key' not exist or 'key' is not a str.
#         return self[str[key]]
#
#     def get(self, key, defualt=None):
#         try:
#             return self[key]   # where d.get(k) return __geitem__ d[k], ensure which can call for __missing__()
#         except KeyError:
#             return defualt
#
#     def __contains__(self, key):
#         return key in self.keys() or str(key) in self.keys()  # judge __contains__ in dict

# inherits from collections.UserDict
# from collections import UserDict
# class my_dict(UserDict):
#     def __missing__(self, key):
#         if isinstance(key,str):
#             raise KeyError
#         return self[str(key)]
#
#     def __contains__(self, item):
#            return str(item) in self.data
#
#
#     def __getitem__(self, item):
#         try:
#            return self.data[str(item)]
#         except KeyError:
#             return None
#
#     def __setitem__(self, key, value):
#         self.data[str(key)] = value
# d = my_dict(a=1,b=2)


# # used collections.defaultdict
# from collections import defaultdict
# def func():
#     return 'Cindy'
# d_d = defaultdict(func, a=1,b=2)
# print(d_d[0])
#
# # collections.ChainMap
# from collections import ChainMap
# d1 = dict(a=1)
# d2 = {'a':2, 'b':2}
# d3 = dict([('a',2),('b',2),('c',3)])
# C = ChainMap(d1,d2,d3)
# print(C['a'])
