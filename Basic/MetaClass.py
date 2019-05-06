'''
元类:
    1. 定义:
         Python中一切皆对象, 类也是一个对象, 创建类的类, 就是元类(type)

    2. 创建类的过程: 利用class关键字
         class ClassName(father):
              # 类体
         1)获取类名'ClassName'
         2)获取所有父类（father,)
         3)执行类体, 获得类的命名空间 dict = {var=value,func=f,..}
         4)调用type.__init__()方法生成类 ClassName = type('ClassName',(father,),dict)
         
    3. 利用type方法生成类
       ClassName = type('ClassName',(father,),dict(var=value,func=f,..))     
''' # 元类定义,利用元类type()生成类

'''
用自定义的元类创建类:
    1. 继承type类
       class myMeta(type):
           def __init__(self,class_name,class_bases,class_dict):
               super(myMeta,self).__init__(class_name,class_bases,class_dict)
               # 扩展部分
               
    2. 用metaclass参数声明创建该类的元类, 默认为type 
       class Test(object,metaclass=myMeta):
           # 类体
    
    # 扩展: 类的格式验证
       if class_name.islower():
           raise TypeError('类名%s请改为驼峰体' % class_name)
       if '__doc__' not in class_dict or len(class_dict['__doc__']).strip('\n') == 0:
           raise TypeError('类中必须有文档注释, 且文档注释不能为空')                          
''' # 用自定义的元类创建类: 元类的__init__()方法

'''
用元类控制类创建实例: 元类的__call__方法
   1. 定义元类__call__方法
   class myMeta(type):
       def __call__(self,*args,**kwargs):              
          obj = self.__new__(self)                #1. 用Object.__new__(self)创建一个实例对象obj, 类调用实例方法必须手动传参, 
                                                      这里self是ClassName, 但ClassName中没有__new__方法,最后在Object中找到了
          self.__init__(obj,*args,**kwargs)       #2. 用ClassName.__init__(obj)初始化实例, 类调用实例方法必须手动传参
          # 扩展部分
          return obj                              #3. 返回初始化好了的obj
   
   2. 用该元类创建的类, 创建实例
   t = Test()                                     # 这里会调用元类的__call__()方法, 执行1,2,3创建实例并初始化 
   
   # 扩展: 将所有实例属性变为私有属性
   obj.__dict__ = {'_%s' % k for k in obj.__dict__.keys()}        
''' # 类创建对象的具体过程: 元类的__call__()方法

'''
完整的属性查找过程:
       1. 先按类的继承链查找(MRO)
       2. 没有找到再按元类查找, 即Test --> myMeta --> type
''' # 完整的属性查找过程

'''
单例模式:
      1) 定义: 同一个类实例化多次的结果指向同一个对象, 用于节省内存空间
              任意一个实例属性变化, 所有实例的属性都会变化
      2) 用途: 配置相同的对象, 可用单例模式实例化, 节省空间
   
类实现单例模式, 定义类方法实现
    HOST = '1.1.1.1'
    PORT = 3306
    
    class Test:
        __instance = None
        def __init__(self,host,port):
            self.host = host
            self.port = port    
        @classmethod
        def singe_type(cls):
            if not cls.__instance:                  # 如果实例不存在
                cls.__instance = cls(HOST,PORT)     # 则创建, cls == Test, 调用Test.__init__()方法
            return cls.__instance
    
    obj1 = Test.singe_type()
    obj2 = Test.singe_type()                        # obj1和obj2为同一个实例                          
''' # 单例模式: 类方法实现

'''
元类实现单例模式, myMeta.__init__()在定义类时就已经创建了一个实例
       class myMeta(type):
           def __init__(self,cls_name,cls_bases,cls_dict):
               self.__instance = object.__new__(self)                    # 创建一个实例
               self.__init__(self.__instance,HOST,PORT)                  # 为该实例初始化
               super(myMeta,self).__init__(cls_name,cls_bases,cls_dict)
           def __call__(self,*args,**kwargs):
               if args or kwargs:                                        # 如果有参数传入, 正常创建实例
                  obj = object.__new__(self)
                  self.__init__(obj,*args,**kwargs)
                  return obj
               return self.__instance                                    # 无参数传入, 返回唯一已经创建好的实例
       
       class Test(metaclass=myMeta):
           def __init__(self,host,port):pass         
''' # 单例模式: 元类实现

'''
类的装饰器实现: 在装饰部分创建实例
def single_type(cls):
    _instance = cls(HOST,PORT)        # 相当于Test(HOST,PORT)创建实例
    def wrapper(*args,**kwargs):
       if args or kwargs:
          obj = cls(*args,**kwargs)
          return obj
       return _instance
    return wrapper
    
@single_type                         # 执行Test = single_type(Test), 创建实例, 返回wrapper
class Test:
    def __init__(self,host,port): pass
''' # 单例模式: 类的装饰器实现

# 下一章: ExceptionBase.py