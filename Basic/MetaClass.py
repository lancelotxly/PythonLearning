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
'''