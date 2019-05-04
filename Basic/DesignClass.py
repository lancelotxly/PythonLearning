'''
Design Class: Bind Attrs(var, func), Dunder Attr, Metaclass
'''

'''
Dunder Attrs: 1. Iterable/Iterator:
                 __iter__(): # return Iterable
                 __next__(Iterable): # 'for x in Iterable' ever step will call for '__next__(Iterable)' to return value, till 'raise StopIteration'.
              
              2. __dict__: 1) For Class: Class.__dict__    # save attrs and values of Class
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
                                    f.read()  # The essence: f.read --> __getattr__(read) --> return getattr(self.file.read) --> self.file.read() # call for
                        
                补充:
                __getattribute__(key):   
                 # 1. Always Execute
                 # 2. raise Exception, execute __getattr__(key)
                                   
                 2) __setattr__(key, value):  # Execute when 'obj.key = value'
                        # code
                        self.__dict__[key] = value 
                   
                 3) __deliattr__(key):   # Execute when 'del obj.key'  
                        # code
                        self.__dict__.pop(key)
                   
              5. Callable Method:
                 __call___(): 
                            #1. obj = Class()  # 产生一个实例, 过程: 1> Class()执行abc.__call__() 2> __call__()调用__init__生成并返回一个对象
                            #2. obj()          # 执行Class.__call__()
                 
              6. Print(ClassName):
                 __str__() / __repr__()
              
              7. Format obj info as 'fmt':
                 __format__(str):
                    return str.format(self)    # <type 'str'>
                    
                    Using:  
                         class TimeType():
                            Format_dic = {
                                'ymd1':'{0.year}:{0.month}:{0.days}',
                                'ymd2':'{0.year}-{0.month}-{0.days}'
                            }
                            def __init__(self,year,month,days):
                                self.year = year
                                self.month = month
                                self.days = days
                        
                            def __format__(self, format_spec):
                                fmt = TimeType.Format_dic[format_spec]
                                return fmt.format(self)
                        
                        time = TimeType(2019,3,20)
                        print(format(time,'ymd2'))
              
              8. __slots__: 省内存, 实例不再具有__dict__属性，obj.attr只能访问__slots__中的变量，涉及__dict__的方法也失效
                            适用于属性很少，但生成实例很多的类
                          #1. Class.__slots__ = ('attr',)
                          #2. obj doesn't have obj.__dict__
                          #3. obj.__slots__ --> Class.__slots
              9. __del__(): module运行结束, 触发该函数，释放空间
              
              10. Content Manage: __enter__()/__exit__()
                                  class Test():
                                      def __init__(self): pass
                                      
                                      def __enter__(self):
                                          # code_enter
                                          return self
                                      
                                      def __exit__(self, exc_type, exc_val, exc_tb):
                                          # code_exit
                                  
                                  with Test() as f:
                                      # code_f
                                      
                    # Flow: 1. No Exception: 1> __init__()
                                             2> __enter__(): return self
                                             3> code_f
                                             4> __exit__():  end with code
                            
                            2. Exception: 1> __init__()
                                          2> __enter__(): return self
                                          3> __exit__(): end with code, exc_type exc_val exc_tb are Exception info. 
                              
                                      
              11. Descriptor: 1) DEFINE: 描述符是一个类, 实例调用它作为属性
                                        class Type():
                                             def __init__(self): 
                                             def __get__(self,instance,owner):    # instance为拥有该描述符作为属性的实例, owner为该实例的类
                                             def __set__(self,instance,value):    # value为该实例设置的值
                                             def __delete__(self,instance):
                              
                              2) Classify:  
                                        1> Data Descriptor: __get__(), __set__(), [__delete__()]
                                        2> Non-Data Descriptor: __get__() [__delete__()]
                              
                              3) Format: 
                                       class People():
                                            name = Type()
                                            def __init__(self,name):
                                                self.name = name
                                            def func(self): pass
                                       
                                       1> Can only as 'Class.attr', save in 'Class.__dict__'
                                       2> name = Type() is running Type.__init__() now
                                       
                              4) Priority of Visiting attr:
                                       Class.attr > Data Descriptor > self.attr > Non-Data Descriptor > __getattr__()
                                       1>. People.name             # 1. Type.__get__(): instance is None
                                           People.name = value     # 2. Now 'name' will not be a descriptor, but as a Class.attr
                                           People.name             # 3. Therefore, it will call for Class.attr
                                       
                                       2>  p = People('xzq')       # 1. People.__init__() --> self.name --> Type.__set__()
                                           p.name                  # 2. Now 'name' is a descriptor, so it will call for Type.__get__()
                                           def p.name              # 3. It will call for Type.__delete__()
                                           
                                       3>  p.func                  # 1. func is a Non-data descriptor obj 
                                                                   # 2. it will call for Func.__get__(), and return an address of the func
                                           p.func = value          # 3. Not 'func' is self.attr
                                           p.func                  # 4. Therefore, it will call for self.attr
                              
                              5) Using: 1> Limit type of arguments
                                           class Typed():
                                                def __init__(self, attr_name, exc_type):
                                                      self.attr_name = attr_name
                                                      self.exc_type = exc_type
                                                      
                                                def __get__(self, instance, owner):
                                                      if instance is None:
                                                          return self
                                                      return instance.__dict__[self.attr_name]
                                                
                                                def __set__(self, instance, value):
                                                      if not isinstance(value, self.exc_type):
                                                            raise TypeError('Please input %s' self.exc_type)
                                                      instance.__dict__[self.attr_name] = value
                                                
                                                def __delete__(self, instance):
                                                      instance.__dict__.pop(self.attr_name)                                           
                                           
                                           class People():
                                                name = Typed('name',str)
                                                age = Typed('age',int)
                                                salary = Typed('salary',float)
                                                def __init__(self, name, age, salary):
                                                    self.name = name 
                                                    self.age = age
                                                    self.salary = salary
                    
                    补: 类的装饰器
                        1. 无参输入
                           def decorate(cls):
                               # code
                               return cls
                           
                           @decorate                           # People = decorate(People)
                           class People():
                               def __init__(self): pass    
                               
                        2. 有参输入
                           def input_para(*args, **kwargs):
                               def decorate(cls):
                               # code
                               return cls
                           return decorate
                           
                           @input_para(*args, **kwargs)        # 1. input_para(*args, **kwargs): return decorate    2. People = decorate(People)
                           class People():
                               def __init__(self):pass              
                                       
                                        2>. Limit type of arguments (Completely) 
                                            class Typed():
                                                def __init__(self, attr, exc_type):
                                                    self.attr = attr
                                                    self.exc_type = exc_type
                                            
                                                def __get__(self, instance, owner):
                                                    if instance is None:
                                                        return self
                                                    return instance.__dict__[self.attr]
                                            
                                                def __set__(self, instance, value):
                                                    if not isinstance(value, self.exc_type):
                                                        raise TypeError('Please input %s' % self.exc_type)
                                                    instance.__dict__[self.attr] = value
                                            
                                                def __delete__(self, instance):
                                                    instance.__dict__.pop(self.attr)
                                            
                                            def Typedasset(**kwargs):
                                                def wrapper(cls):
                                                    for attr_name, exc_type in kwargs.items():
                                                        setattr(cls, attr_name, Typed(attr_name, exc_type))
                                                    return cls
                                                return wrapper
                                            
                                            @ Typedasset(name=str, age=int, salary=float)
                                            class People():
                                                def __init__(self,name, age, salary):
                                                    self.name = name
                                                    self.age = age
                                                    self.salary = salary
                                                    
                                        3>. Using Descriptor complete '@property'
                                            #1. The essence:    
                                                           @property
                                                           def func(self):pass
                                                    when 'obj.func' will return the value immediately.
                                            #2. 
                                                class lazyproperty():
                                                      def __init__(self,func):
                                                         self.func = func
                                                      
                                                      def __get__(self, instance, owner):
                                                          if instance is None:
                                                             return self
                                                          value = self.func(instance)
                                                          instance.__dict__[self.func.__name__, value]
                                                          return value
                                                
                                                class Room():
                                                      def __init__(self,name, width, length):
                                                           self.name = name
                                                           self.width = width
                                                           self.length = length
                                                      
                                                      @lazyproperty                       # area = lazyproperty(area)  相当于定义了一个非数据描述符
                                                      def area(self):
                                                           return self.width * self.length
                                                
                                                r = Room('alex',1,1)
                                                r.area                                  #1. lazyproperty.__get__()
                                                                                        #2. return self.func(instance), where 'self.func = area', 'instance=obj of Room'
                                                                                        #3. Therefore equivalent to call for 'def area(self)'
                                                r.area                                  #4. Now 'obj.area' has saved into obj.__dict__, so according to the priority,
                                                                                            while visit 'obj.area', not Non-data descriptor.      
                                          
                                        
                                        3> Using Descriptor complete '@classmethod'
                                           #1. The essence: 
                                                           @classmethod
                                                           def func(cls,*args,**kwargs): pass
                                                when 'Class.func()' and 'obj.func()' will call for 'func()'
                                           
                                           #2.  class ClassMethod():
                                                     def __init__(self,func):
                                                         self.func = func
                                                    
                                                     def __get__(self, instance, owner):                 # where 'owner' is 'ClassName'
                                                         def feedback(*args, **kwargs):
                                                             # code
                                                             return self.func(owner, *args, **kwargs)
                                                         return feed back
                                                
                                                class People():
                                                     name = 'xzq'
                                                     @ClassMethod                      # func = ClassMethod(func)
                                                     def func(*args, **kwargs): pass
                                                     
                                        
                                        4> Using Descriptor complete '@staticmethod'
                                           class StaticMethod():
                                                 def __init__(self,func):
                                                     self.func = func
                                                 
                                                 def __get__(self, instance, owner):
                                                     def feedback(*args, **kwargs):
                                                         # code
                                                         return self.func(*args, **kwargs)
                                                     return feedback
                                           
                                           class  People():
                                                 @StaticMethod
                                                 def func(*args, **kwargs): pass
              11. Others:
                 __name__: #1. In the module '__main__'  #2. In other module 'modulename'
                 Class.__name__: # The name of Class
                 Class.__bases__: # The Father of Class         
                 Class.__modules__ / Instance.__modules__ :  # modules
                 Class.__class__: # <class 'type'>     Instance.__class__:  # <class '__main__.Class'>
                 Class.__doc__ / Instance.__doc__:  # document, Can't be inherited
'''


'''
MetaClass: Create a Class dynamically
           1. DEFINE: 
                     一切皆对象, 类也是一个对象, 创建类(obj)的类, 就是元类
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
