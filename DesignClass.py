'''
Design Class: Bind Attrs(var, func), Dunder Attr, Metaclass
'''
'''
Bind Attrs: 1. For Instance: Other instance or class don't have these attrs
                             1) Bind variable: s.var = value
                             2) Bind function: 
                                              def func(self): pass
                                              s.func = func   # Call for: s.func(s)   
                                     OR:      s.func = types.MethodType(func, s)  # Call for: s.func()
            2. For Class: The addition attrs belongs to class
                             1) Bind variable: ClassName.var = value
                             2) Bind function: 'def func(cls): pass' or 'def func(self): pass'
                                                ClassName.func = func
                                                
            3. Limitation: 1.DEFINE: ONLY the attrs in __slots__ can be bind.
                                     class Father():
                                        __slots__ = ('attr', )
                           2. DISCIPLINE: 1) Only for the current class, the instance of the ChildClass isn't limited
                                          2) If ChildClass has __slots__, the limitation are Father's + Child's __slots                                         
'''
# class Student(object):
#     __slots__ = ('name','age')
# # Bind for instance
# s1 = Student()
#
# s1.name = 'xzq'
# s1.age = 24
#
# def printInf(self):
#     print(self.name, self.age)
# def printHometown(self):
#     print('Hometown is CQ')
#
# s1.printInf = printInf
# s1.printInf(s1)
#
# from types import MethodType
# s1.printHometown = MethodType(printHometown,s1)
# s1.printHometown()
#
# # Bind for class
# Student.Hometown = 'CQ'
# print(s1.Hometown)
# def Welcome(cls):
#     print('Welcome to %s' % (cls.Hometown))
# Student.Welcome = Welcome
# Student.Welcome(Student)
# s1.Welcome()

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
'''
'''
Dunder Attrs: 1. Iterable/Iterator:
                 __iter__(): # return Iterable
                 __next__(Iterable): # 'for x in Iterable' ever step will call for '__next__(Iterable)' to return value, till 'raise StopIteration'.
              
              2. __dict__: 1) For Class: Class.__dict__    # save attrs of Class
                           2) For Instance: self.__dict__  # self.var = value --> self.__dict__ = {var: value}
                           
              3. Sequence Quality: The following __func__() will execute, when Seq operation.
                 __getitem__(key):    # Execute when 'obj[key]'
                    # code
                    return self.__dict__[key]
                    
                 __setitem__(key, value):    # Execute when 'obj[key] = value'
                    # code
                    self.__dict__[key] = value
                    
                 __delitem__(key):          # Execute when 'del obj[key]'
                    # code
                    self.__dict__.pop(key)
                    
                 __len__(): # len()
              
              4. Operate Attr: The following __func__() will execute, when class.attr operation
                 1) __getattr__(key):   # Execute when 'obj.key' not exist
                        # code
                        return value
                   
                   Using: # Return New attr, NOT Inherit
                          e.g.  class MyOpen():
                                   def __init__(self, filename, mode, encoding='utf-8')
                                      self.file = open(filename, mode, encoding)
                                      
                                   def __getattr__(self,item):
                                      return getattr(self.file, item)
                                
                                f = MyOpen()
                                f.read()  # The essence: f.read --> __getattr__(read) --> return getattr(self.file.read) --> call for 'self.file.read'
                                   
                 2) __setattr__(key, value):  # Execute when 'obj.key = value'
                        # code
                        self.__dict__[key] = value 
                   
                 3) __deliattr__(key):   # Execute when 'del obj.key'  
                        # code
                        self.__dict__.pop(key)
                   
              5. Callable Method:
                 __call___(): # s() call for directly
                 
              6. Print(ClassName):
                 __str__() / __repr__()
              
              7. Others:
                 Class.__name__: # The name of Class
                 Class.__bases__: # The Father of Class         
                 Class.__modules__ / Instance.__modules__ :  # modules
                 Class.__class__: # <class 'type'>     Instance.__class__:  # <class '__main__.Class'>
                 Class.__doc__ / Instance.__doc__:  # help document
'''

'''
metaclass: create a class  dynamically
           className = type('className', (father1,father2), dict(attr=value, function=f))
'''
'''
MetaClass: Create a Class dynamically
           1. DEFINE: 
                     ClassName = type('ClassName', (father1, ), dict(var=value, func=f, ))
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
