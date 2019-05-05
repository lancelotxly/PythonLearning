'''
Design Class: Bind Attrs(var, func), Dunder Attr, Metaclass
'''
'''
定制类: 
      1. 双下划线属性__attr__
      2. 元类metaclass
''' # 综述

'''
iterable/iterator:
1. __iter__(): return iterable_obj
   1) 实现了该方法的对象叫iterable
   2) iter(obj)会调用该方法, 生成一个迭代器iterator

2. __next__(): 指明迭代器怎么返回值
   1) next(iterator)会返回一个值, 直到所有的值都返回了报错StopIteration
   2) for.. in iterable/iterator 会自动调用该方法, 迭代结束后不会报错
''' # 迭代器: __iter__(), __next__()

'''
__dict__: 是一个字典, 包含属性和值
         1) ClassName.__dict__             # 保存class中的所有data和method
         2) self.__dict__/obj.__dict__     # 保存该对象data
                                           # self.var = value 实质上就是把数据存入该字典中, 即 self.__dict__ = {'var':value}
''' # 属性字典: __dict__

'''
Seq特性:
1. __getitem__(key): return self.__dict__[key]            # obj[k]获取数据值执行
        
2. __setitem__(key,value): self.__dict__[key] = value     # obj[k]=value修改数据时执行

3. __delitem__(key): self.__dict__.pop(key)               # del obj[key]删除数据时执行

4. __len__():                                             # len(obj)获取长度时执行                            
''' # Seq特性: __getitem__(), __setitem__(), __delitem__(), __len()

'''
属性操作: obj.attr
1. __getattr__(attr):         # 当obj.attr不存在时会执行, attr为字符串
   用途:
       1) 不通过继承, 添加新的属性
          class MyOpen:
              def __init__(self,filename,mode,encoding='utf8')
                  self.file = open(filename,mode=mode,encoding=encoding)
              def __getattr__(self,item):
                  return getattr(self.file,item)
          f = MyOpen('test','r')
          f.read()   
          # 执行过程为: 
                    1> f.read 不存在
                    2> __getattr__(read): return getattr(f.file,'read')
                    3> f.read() --> getattr(f.file,'read')()

2. __getattribute__(attr):  
   1) obj.attr时总会执行 
   2) 当raise AttributeError时, 执行__getattr__(attr)

3. __setattr__(key,value): self.__dict__[key] = value    # 当obj.key = value时执行

4. __delattr__(key): sefl.__dict__.pop(key)              # 当del obj.key时执行                                                
''' # 属性操作: __getattr__(),__getattribute__(), __setattr__(), __delattr__()

'''
Callable方法: obj()对象可直接调用的方法
__call__():
          1. obj()               # 对象调用时执行
          2. obj = Class()       # 生成实例时, Class()会执行abc.__call__()方法, 进而调用__init__()生成实例返回对象                                 
''' # Callable方法: __call__()

'''
对象的字符串显示:
1. __str__()        # str(obj)或者print(obj)时执行

2. __repr__()       # repr(obj)或者解释器执行

3. __format__()     # format(obj)执行
   实例:
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
''' # 对象的字符串显示: __str__(), __repr__(), __format__()

'''
__slots__:
          1. 类属性, 即所有实例公有的属性
          2. __slots__ = ('attr', )  限定obj.attr只能为__slots__中的值
          3. obj.__dict__不存在, 但Class.__dict__存在
          
          * 省内存, 不用给每一个实例配__dict__, 但实例的数据还是独立的 
          * 适用于data很少,但实例很多的类
          * __slots__属性不继承, 但子类若重写__slots__会包含父类的__slots__
''' # 限制实例属性: __slots__

'''
__del__():  module运行结束后执行, 释放空间
''' # 释放内存: __del__()

'''
上下文管理: __enter__()/__exit__()
    1. with 代码块中无异常
        class Test:
             def __init__(self):pass
             def __enter__(self):
                  # code1          # 出现with语句时执行
                  return self      # 若有返回值则赋值给as声明的变量
             def __exit__(self,exc_type,exc_val,exc_tb):
                  # code2          # with中代码块执行完毕时执行
        with Test() as f:
             # code3
        执行顺序为:  code1 -> code3 -> code2
    
    2. with 代码块中抛出异常
       class Test:
             def __init__(self):pass
             def __enter__(self):
                  # code1          # 出现with语句时执行
                  return self      # 若有返回值则赋值给as声明的变量
             def __exit__(self,exc_type,exc_val,exc_tb):
                  # code2          # with中代码块执行完毕时执行
       with Test() as f:
             # code3
             raise Exception
             # code 4
       # code5                            
       执行顺序为: code1 -> code3 -> code2, with之后的代码都不会执行
       异常信息为:   exc_type: 异常类型
                   exc_val: 异常值
                   exc_tb: 异常对象
''' # 上下文管理: __enter__()/ __exit__()

'''
类型:
 1) class类型: ClassName.__class__  # type(ClassName)会返回该属性, 值为 <class 'type'>
 2) obj类型: obj.__class__          # type(obj)会返回该属性, 值为<class '__main__.ClassName'> 
''' # 类型: __class__

'''
描述符: 是一个新式类, 实例调用它作为属性
     1. 定义描述符 Type
        class Type:
             def __init__(self):
             def __get__(self,instance,owner)  # instance为将该描述符作为属性的实例, owner为该实例的类
             def __set__(self,instance,value)  # value为该实例属性的值
             def __delete__(self,instance)     
     
     2. 描述符的分类:
          数据描述符: 实现了__get__(),__set__() [__delete__()可选]
          非数据描述符: 实现了__get__() [__delete__()可选]  
                      函数实质上是一个非数据描述符
     3. 使用描述符:
          class People:
              name = Type()
              def __init__(self,name):
                self.name = name
              def func(self):pass  
          1) 描述符只能作为类属性Class.attr, 保存在类字典中Class.__dict__
             People.__dict__ = {'name':'Type Object'}
             self.__dict__ = {}
          2) name = Type() 会在定义类时立即执行Type.__init__()方法, 创建一个描述符obj  
     
     4. 对含有描述符的属性访问优先级:
        类属性 > 数据描述符 > 实例属性 > 非数据描述符 > __getattr__()
        1) 类属性 > 数据描述符
           People.name          # 此时name为描述符, 触发Type.__get__()方法
           People.name = value  # 此时name变为了类属性
           People.name          # 再次调用时, name为类属性, 不会触发Type.__get__()方法
        
        2) 数据描述符 > 实例属性
           p = People('xzq')    # 实例化People.__init__() --> self.name --> 触发Type.__set__()
           p.name               # 此时name为数据描述符, 触发Type.__get__()方法
           del p.name           # 此时name为数据描述符, 触发Type.__delete__()方法   
        
        3) 实例属性 > 非数据描述符
           p.func               # 函数实质上是一个非数据描述符, 触发Func.__get__()返回func的地址
           p.func = value       # 此时func变为一个实例属性
           p.func               # 再次调用时, func为实例属性, 不会触发Func.__get__()方法                 
''' # 描述符: __get__()/__set__()/__delete__()

'''
描述符的应用: 限制输入类型
1. 限制输入类型
   class Typed:
       def __init__(self,attr_name,exc_type):      # 初始化, 输入instance属性名, 期望类型
          self.attr_name = attr_name
          self.exc_type = exc_type
       def __get__(self,instance,owner)            # instance属性取值时调用此方法
          if instance is None:                     # 防止用类名访问描述符时报错, 即 People.name此时, instance为None 
             return self
          return instance.__dict__[self.attr_name]
       def __set__(self,instance,value):           # instance属性赋值时调用此方法, 限制输入类型
          if not isinstance(value,self.exc_type):
             raise TypeError('Please input %s' % self.exc_type)
          instance.__dict__[self.attr_name] = value
       def __delete__(self,instance):              # 删除instance属性时调用此方法 
          instance.__dict__.pop(self.attr_name) 
   
   class People:
        name = Typed('name',str)
        age = Typed('age',int)
        salary = Typed('salary',float)
        def __init__(self,name,age,salary):
          self.name = name
          self.age = age
          self.salary = salary

2. 限制输入类型, 类的装饰器 + 反射
def limit_type(**kwargs):
   def decorate(cls):
     @functools.wrapper(f)
     def wrapper(*args):
        for attr_name, exc_type in kwargs.items():
           setattr(cls,attr_name, Typed(attr_name,exc_type))    # 通过反射添加描述符属性
        obj = cls(*args)
     return wrapper
   return decorate

@limit_type(name='str',age='int',salary='float')
class People:
    def __init__(self,name,age,salary)
       self.name = name
       self.age = age
       self.salary = salary

p = People('xzq',24,18000.00)       
                                         
''' # 描述符的应用: 限制输入类型

'''
描述符实现@property
   1. @property的功能: obj.func能立即返回函数值
   2. 实现:  
        class myproperty:
            def __init__(self,func):
                self.func = func
        
            def __get__(self, instance, owner):
                print('__get__')
                if instance is None:
                    return self
                value = self.func(instance)
                instance.__dict__[self.func.__name__] = value
                return value
        
        class test:
            @myproperty                  #1. 执行 func = myproperty(func), 调用myproperty.__init__()
            def func(self):              #2. 将func设为非数据描述符
                return 'hhh'
        
        t = test()
        print(t.func)                    #3. 首次调用func, 执行myproperty.__get__()方法, 将instance.func作为实例属性存入属性字典
        print(t.func)                    #4. 再次调用func, 为实例属性, 从t.__dict__中取值, 不执行myproperty.__get__()方法
''' # 描述符的应用: 实现@property

'''
描述符实现@classmethod
 1. @classmethod的功能: Class.func(), obj.func()可以调用func()
 2. 实现:
        class myclassmethod:
            def __init__(self,func):
                self.func = func
        
            def __get__(self, instance, owner):
                def feedback(*args,**kwargs):
                    print('额外功能')
                    return self.func(owner,*args,**kwargs)
                return feedback
        
        class Test:
            @myclassmethod                #1. 执行 func = myclassmethod(func), 调用myclassmethod.__init__()
            def func(cls):                #2. 将func设为非数据描述符
                print('hhh')
        
        Test.func()                       #3. Test.func调用myclassmethod.__init__()返回的包含func的闭包
        t = Test()
        t.func()                          #4. t.func调用myclassmethod.__init__()返回的包含func的闭包
''' # 描述符的应用: 实现@classmethod

'''
描述符实现@staticmethod                                    
1. @staticmethod的功能: Class.func(), obj.func()可以调用func(), 但func()不能操作类或实例数据
2. 实现: 同@classmethod只是不能操作类属性, 不传入cls             
''' # 描述符应用: 实现@staticmethod

'''
其他属性:
    1) __name__: 在本模块中为'__main__'
                 在其他模块中为'模块名'
    
    2) Class.__name__/func.__name__: 类名或函数名
    
    3) Class.__bases__: 父类名
    
    4) Class.__modules__/obj.__modules__: 模块名
    
    5) Class.__doc__/obj.__doc__: 说明文档, 不能继承
    
    8) Class.__mro__: 返回一个tuple, 继承链
       Class.mro(): 返回一个list,继承链
''' # __name__, __bases__, __modules__, __doc__, __mro__

# 下一章: MetaClass.py
