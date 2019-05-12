'''
面向对象编程:
           1. POP, OOD, OOP
           2. 类与实例
           3. 继承: 单继承, 接口继承与多态, 多继承
           4. 封装
           5. 反射(获取信息, 命令分发, 动态加载模块)
''' # 综述

'''
POP & OOD & OOP:
              1. POP(Process Oriented Programming, 面向过程编程): 将一个过程分为几个子过程来完成
              2. OOD(Object Oriented Design, 面向对象设计): 通过定义函数实现'obj = data + method'
              3. OOP(Object Oriented Programming): 定义类 + OOD 
''' # POP & OOD & OOP
# OOD
def Object_func(attr1, attr2):
    def init(attr1, attr2):
        obj = {
            'func1': func1,
            'func2': func2,
            'attr1': attr1,
            'attr2': attr2
        }
        return obj
    def func1(): pass
    def func2(): pass
    return init(attr1, attr2)

obj = Object_func('xzq', 12)
obj['func1']()
attr1 = obj['attr1']

'''
类和实例:
       1. 定义类
           class ClassName(father):
                class_v1 = v1               # 类属性
                class_v2 = v2
                def __init__(self,a,b):     # 实例属性
                    self.a = a
                    self.b = b
                def func1(self): pass       # 实例方法, 所有实例共有
       
       2. 实例化
          obj = ClassName(a,b)
          实例化过程:  执行元类__call__()方法, 详细见MetaClass.py
                     1.  调用tObject.__new__(self)方法创建一个实例t
                     2.  调用ClassName.__init__(t)方法初始化实例
                     3.  返回初始化好的t, 赋值给obj                        
                    
       3. 访问属性: 只能通过obj或ClassName访问
             1) obj访问属性(data+method): 
                    obj.attr: 1> 搜索__init__()内部
                              2> 然后在class内部搜索
                              *当obj调用func(self,a,b)类内部方法时, 会自动传参self            
            
            2. Class访问属性(data+method):
                   ClassName.attr: 1> 不能访问obj.attr, 即不会在__init__()中搜索, 直接在class内部搜索
                                   * 当ClassName调用func(self,a,b)类方法时, 需要手动传入self, 也就是需要手动传入一个对象obj           
                     
       4. 绑定属性:
            1)obj绑定属性: 对象应该只有data, 不应该有自己独立的method
                  1> 绑定data:   obj.data = value
                  2> 绑定method:
                                        def func(self): pass
                                方式一:  obj.func = func
                                        obj.func(obj)           # 调用时需要手动传入self, 因为该方法是属于当前obj的, 只有实例方法才会自动传入self
                                方式二:  obj.func = types.MethodType(func,obj)
                                        obj.func()              # 可正常调用                      
            2)Class绑定属性
                  1> 绑定data:  ClassName.data = value
                  2> 绑定method:
                               # 绑定实例方法
                               def func(self): pass
                               ClassName.func                  # 绑定后所有实例都可以使用, 包括绑定前生成的实例   
                                                    
       5. 静态属性, 类方法, 静态方法            
          1) 静态属性: 将method打包成data, 封装了内部细节
                      @property
                      def func(self):pass
                      obj.func          # 访问时不再需要调用
                                                    
          2) 类方法: 不要实例对象, 通过ClassName可直接访问的方法
                    @classmethod
                    def func(cls):pass     # 类方法只能访问类属性, 没有self
                    ClassName.func()       # 通过类名直接调用
                                      
          3) 静态方法: 不能操作类属性, 实例属性, 但可以被class或obj直接调用
                    @staticmethod
                    def func():pass          
''' # 类和实例

'''
组合: 类A与类B显著不同, 类A是类B的组件
          class Object_C(object):
              def __init__(self,a,b):
                 self.a = a
                 self.b = b
              ...
          class Object_A(object):pass
          class Object_B(object):pass
          
          a = Object_A()
          b = Object_C()
          C = Object_C(a,b)
''' # 组合

'''
继承: 类和类之间大部分功能相同
单继承:             
    1. 定义  
           父类: class Father(object):
                    def __init__(self,a,b):
                        self.a = a
                        self.b = b
                    def func1(self):pass
           
           子类: class Child(Father)
                1. 子类完全继承父类所有属性和方法
                2. 子类可对父类方法进行重写
                    * 重写__init__()方法时, 必须实现父类方法, 即添加新的实例属性时, 必须先确保父类实例属性
                      def __init__(self,a,b,c):
                         super(Child,self).__init__(a,b)
                         self.c = c
                3. 子类可部分继承父类方法, 对方法进行添加
                      def func1_plus(self):
                         super(Child,self).func1()     # 调用时, 这里会执行父类func1()
                         # 新功能
                4. 子类可定义自己的方法和属性         
                                    
    2. 子类访问属性:          # 引入描述符的情况见DesignClass.py
          1) 子类对象obj访问属性
              obj.attr(data+method): 1> 搜索子类__init__()
                                     2> 搜索父类__init__()
                                     3> 子类中搜索
                                     4> 父类中搜索
          2) 子类ClassName访问属性
              ClassName.attr(data+method): 1> 子类中搜索            
                                           2> 父类中搜索  
''' # 单继承: 定义, 访问属性

'''
接口继承: 归一化设计
       1. 定义:
            1) 接口不能实例化
            2) 接口中的方法必须要实现
       
       2. 操作:
           import abc
           class Interface(metaclass=abc.ABCMeta)    # 定义接口
               @abc.abstractmethod
               def func(self): pass
           
           class Child(Interface):                   # 继承接口并重写所有方法
              def func(self):
                 # code 

多态: 不同对象调用相同方法, 结果不同                             
''' # 接口继承: 归一化设计, 多态

'''  
多继承:
     1. 定义
           class A(): 
              def __init__(self)
           class B(): 
              def __init__(self)
           class C(A,B):
              def __init__(self):
                 super(C,self).__init__(?)      # 传参按继承的就近原则
     
     2. 访问属性的搜索顺序:
         经典类 class A(object): 深度优先, 会沿着第一条继承链搜到A
         新式类 class A:    广度优先, 沿着第一条继承链搜索到A之前一个类, 然后最后一条链搜索到A
     
     3. 继承链存在 C.__mro__中, 是一个list, 查找时从左到右搜索到基类             
''' # 多继承

'''
封装: 
    1. 属性(data+method)的类型:
         _var, _func(): 对外部不可见, 可继承
         __var, __func(): 对外部不可见, 且不可继承
    
    2. 数据封装
       1) 设置为__var
       2) 通过静态属性访问和设置
           @property
           def var(self): return self.__var
           @var.setter
           def var(self,a): self.__var = a                  
''' # 封装

'''
获取类信息:
      1. 获取对象类型:  type(obj)
      2. 获取继承信息:  isinstance(obj,Class),  issubclass(Child, Father)
      3. 获取所有属性:  dir(obj)          # 返回一个list, 包含所有属性, 不包括属性值
                      cls/obj.__dict__  # 返回一个dict, 所有属性和值
      
      4. 反射: 操作实例属性或类属性
             hasattr(obj/cls,'attr')
             getattr(obj/cls,'attr',默认值[可选])
             setattr(obj/cls,'attr')
             delattr(obj/cls,'attr')
             用途:
                 1. 操作属性
                 2. 命令分发
                 3. 动态运行方法
                 e.g. 
                     if  hasattr(f1,'get'):
                         getattr(f1,'get')()
                     else:
                         # 运行其他代码    
             

动态加载模块: 通过字符串加载
   1) m = __import__('module')                                          
   2) m = importlib.import_module('module')                                                                           
''' # 反射(获取信息, 命令分发, 动态加载模块)