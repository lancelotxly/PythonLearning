'''
Design class: bind attrs and functions, special attrs and functions, metaclass
'''
'''
bind attrs and functions: 1. for instance:
                              bind attrs:  s.attr = value
                              bind functions:  def function(self):
                                                    pass
                                               s.function = function
                                               s.function(s)  # call for
                                    or：
                                               from types import MethodType
                                               s.function = MethodType(function,s)
                                               s.function() # call for
                                               
                         2. for class:
                              bind attr: Student.attr = value   # attrs belong to class
                              bind function: Student.function = function      # for all instances have this function
                              
                         3. __slots__ = ('attrs','functions')  # limits the attrs and functions what instance can define
                            tips: 1. only limit in current class, the instance to child class isn't limited(if no __slots__ in child class)
                                  2. if child class has __slots__, then the limitation are father's + child's __slots__
'''
# class Student():
#     pass
#
# s = Student()
# s.age = 20
# s.name = 'xzq'
# def printInf(self):
#     print('this is %s, %d years old' % (self.name, self.age))
#
# def printHometowm(self, hometowm):
#     print('his hometown is %s' % (hometowm))
#
# s.printInf = printInf
# s.printInf(s)
# from types import MethodType
# s.printHomtwon = MethodType(printHometowm,s)
# s.printHomtwon('Chongqing')

# class Student():
#     pass
#
# s = Student()
#
# def set_age(self,age):
#     self.age = age
#
# Student.set_age = set_age
# s.set_age(25)
# print(s.age)

# class Student():
#     __slots__ = ('name', 'age', 'gender','printInf')
#
# class Boy(Student):
#     __slots__ = ('hometowm')
#     pass
#
# b = Boy()
# b.name = 'CQ'
# print(b.name)


'''
special attrs and functions: 
                            __len__():  return length of instance data
                            __str__()/ __repr__():  print(Student()) output str
                            
                            __iter__():   return iterable
                            __next__():   __next__() define how to get the next value of iterable, until 'raise StopIteration' breakout
                            
                            __dict__:  1. for class, Class.__dict__ will save attrs which belongs to class and functions
                                       2. for instance, self.__dict__ = kwargs
                                                        self.attr = value -->  self.__dict__={attr: value}
                                                        
                                       tips: 1. then we can use dict operation to operate item,
                                                eg.  __dict__[key], __dict__[key_new] = value_new, __dict__.pop(key)
                                             2. args # tuple
                                                kwargs # dict
                                                __dict__ # dict
                                       
                            # define how to operation by using class[key]
                            __getitem__(): return self.__dict__[item]   # get item class[key] 
                            __setitem__(): self.__dict__[key] = value   # set item class[key] = value
                            __delitem__(): self.__dict__.pop(key)       # del item class[key]
                                   
                            # define how to operation by using class.attr
                            __getattr__():  return self.__dict__[item]      # get attr class.key
                            __setattr__():  self.__dict__[key] = value    # set attr class.key = value 
                            __delattr__():  self.__dict__.pop(key) = value    # del attr class.key
                            
                            __call__():  define a callable function of class  #  instance()  call for
                            
                            
                            Class.__name__:  the name of class, instance doesn't have the attr
                            Class.__bases__:  the super class of this class
                            Class.__modules__ / instance.__modules__:  modules
                            Class.__class__ : # <class 'type'>    instance.__class__: # <class '__main__.Class'>
                            
                            Class.__doc__ / instance.__doc__: help document
                            
                            
                            
                            
                            
'''
# class Student():
#     '''
#     this is a test example
#     '''
#     def __init__(self, name, age, **kwargs):
#         self.__dict__ = kwargs
#         self.name = name
#         self.age = age
#
# s = Student('xzq',18, gender = 'man')
# print(s.__dict__)
# print(Student.__dict__)
#
# print(Student.__doc__)
# print(s.__doc__)
#
# class Boy(Student):
#     pass
# print(Boy.__bases__)
#
# print(Student.__module__)
# print(s.__module__)
#
# print(Student.__class__)
# print(s.__class__)


# class Fib():
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a , self.b = self.b, self.a + self.b
#         if self.a > 1000:
#             raise StopIteration
#         return self.a
#
#     def __getitem__(self, item):
#         self.a, self.b = 1, 1
#         if isinstance(item, int):
#             for i in range(item):
#                 self.a, self.b = self.b, self.a + self.b
#             return self.a
#         elif isinstance(item,slice):
#             start = item.start
#             stop = item.stop
#             if start is None:
#                 start = 0
#             L = []
#             for i in range(stop):
#                 if i >= start:
#                     L.append(self.a)
#                 self.a, self.b = self.b, self.a + self.b
#             return L
#
# f = Fib()
# for x in f:
#     print(x, end = ' ')
# print()
# print(f[0])
# print(f[:5])

# class Foo():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def __getitem__(self, item):
#         return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         self.__dict__.pop(key)
#
# f = Foo(2,2)
# f.x = 1
# print(f['x'])
# print(f.__dict__)
#
# f['b'] = 2
# print(f.b)
# print(f.__dict__)
#
# del f['x']
# print(f.__dict__)

# class Fib():
#     def __getitem__(self, item):
#         self.a, self.b = 1, 1
#         for i in range(item):
#             self.a, self.b = self.b, self.a + self.b
#         return self.__dict__['a']
#
# f = Fib()
# print(f[10])

# class Student():
#     def __getattr__(self, item):
#         try:
#             return self.__dict__[item]
#         except KeyError as e:
#             return '%s isn\'t exists' % item
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#
#     def __getitem__(self, item):
#         try:
#             return self.__dict__[item]
#         except KeyError as e:
#             return '%s isn\'t exists' % item
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
# s = Student()
# print(s.name)
# s.age = 18
# print(s.age)
# print(s['age'])
# s['name'] = 'xzq'
# print(s.name)

# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __call__(self, *args, **kwargs):
#         print('this is %s, %d years old' % (self.name, self.age))
#
# s = Student('xzq',18)
# s()



'''
metaclass: create a class  dynamically
           className = type('className', (father1,father2), dict(attr=value, function=f))
'''
# class Student():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# def __init__(self,name,age,gender):
#     Student.__init__(self,name,age)
#     self.gender = gender
#
# def printInf(self):
#     print('this %s names %s, %d years old' % (self.gender, self.name, self.age))
#
# Boy = type('Boy',(Student, ),dict(__init__ = __init__, printInf = printInf))
# b = Boy('xzq',18,'man')
# b.printInf()
