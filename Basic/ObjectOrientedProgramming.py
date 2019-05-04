'''
Object Oriented Programming: POP & OOD & OOP, Class and Instance, Inheritance & Polymorphism & Encapsulation, Get Information (Reflection)
'''

'''
POP & OOD & OOP:
               1. POP (Process Oriented Programming): Divide the Process into Sub-process to complete.
               2. OOD (Object Oriented Design): Define function to achieve 'obj = data + method'
                            
                            
               3. OOP (Object Oriented Programming):  Define class + OOD
'''
# # OOD
# def Object_func(attr1, attr2):
#     def init(attr1, attr2): v
#         obj = {
#             'func1': func1,
#             'func2': func2,
#             'attr1': attr1,
#             'attr2': attr2
#         }
#         return obj
#     def func1(): pass
#     def func2(): pass
#     return init(attr1, attr2)
#
# obj = Object_func('xzq', 12)
# obj['func1']()
# attr1 = obj['attr1']

'''
Class and Instance: 
          1. Define a class and Instantiate          
                    1) DEFINE:
                             class ClassName(father):
                                   class_var1 = value1
                                   class_var2 = value2
                                   ...
                                   
                                   def __init__(self,a,b):
                                        self.a = a
                                        self.b = b
                                   def func1(self): pass
                    
                    2) Instantiation:
                             obj = ClassName(a,b)      # 1. Call for '__init__(self,a,b)'
                                                         2. Running '__init__(self,a,b)'
                                                         3. '__init__(self,a,b)' will 'return obj'
                    
                    
          2. Visit Attrs:     
                    1) Object Visit Attrs:  Object ONLY have Data, DON'T have method
                       1>. obj.attr   # 1. Search in '__init__()'
                                        2. Search in the out class, Don't search in the outside
                                        3. obj.func1()
                                                      # When 'obj' call for 'func1(self)' [Belongs to class], will plunge 'self' automatically
                       
                       2> Bind Attrs: 1>>. Bind Data:     obj.data = value
                                      2>>. Bind Method:   
                                                          def func(self): pass
                                                          obj.func = func
                                                          # Call for
                                                          obj.func(obj)    # When 'obj' call for 'func(self)' [Belongs to instance], need plunge 'self'.
                                                    OR:   obj.func = types.MethodType(func,obj)  # Call for: obj.func()
                    
                    2) Class Visit Attrs:
                       1>. ClassName.attr   # 1. Can't Visit obj.attr
                                              2. ClassName.func1(obj)  # When 'class' call for 'func1(self)', need plunge 'self'
                       
                       2>. Bind Attrs: 1>>. Bind Data: ClassName.data = value
                                       2>>. Bind Method:
                                                        def func(self): pass
                                                        ClassName.func = func
                                                                            
                    **: class 中的属性， 只能通过self.attr  ClassName.attr 来调用
                                       直接调用variable : 1. 先在函数中找
                                                         2. 没有则在class外部找 
                                                          
                                                          
          3. Static property, ClassMethod, StaticMethod, Combine:
                    1) Static property:  Encapsulate the logic of function
                                      @property
                                      def func(self): pass       # Can visit 'self.attr' and 'class.attr'
                                      # Call for
                                      obj.func                   
                                      
                                      #1. property 本质是一个Data-Descriptor
                                      #2. @property  本质是在调用property.__get__()
                                      #3. @func.setter 本质是在调用property.__set__()
                                      #4. @func.deleter 本质是在调用property.__delete__()
                                      
                    2) ClassMethod:  Some method don't need obj, Can call for by class (and obj)
                                      @classmethod
                                      def func(cls): pass        # Can visit 'class.attr' ONLY
                                      # Call for                  
                                      ClassName.func()
                    
                    3) StaticMethod:  Some method no matter for 'class.attr' and 'self.attr', But can call for by 'class' and 'obj'
                                      @staticmethod
                                      def func(): pass           # Not operate 'class.attr' or 'self.attr'    
                                      
                   4) Combine: 类A与类B显著不同, 类A是类B的组件
                               class Object_C():
                                     def __init__(self,a,b):
                                         self.a = a
                                         self.b = b
                                     ...
                               class Object_A(): pass
                               class Object_B(): pass
                               
                               a = Object_A()
                               b = Object_B()
                               c = Object_C(a,b)
'''


'''
Inheritance: 类之间相同，共同功能做基类
            1. DEFINE:
                       class Father(object):
                           # cls
                           def __init__(self, a, b):
                                pass
                           def func1(self):
                                pass

                       class Child(Father):
                           # cls
                           def __init__(self, a, b, c):
                              super(Child, self).__init__(a,b)
                              # Father.__init__(self,a,b)         # Not better, ClassName.func(self), 'self' is necessary
                              self.c = c

                           def func_new(self):
                               super(Child,self).func1()
                               # Father.func1(self)


            2. Visit Attr:
                          1) child.attr (Order of Visit):  # 引入描述符的情况见DesignClass.py  
                                   1>. child.data: 
                                                 child.__init__() --> father.__init() --> Child.class --> Father.class
                                                 
                                   2>. child.method:
                                                 Child.class --> Father.class                                          
                          2) Child.attr: 
                                       Child.class -->  Father.class
               
                                       
            3. Interface-Inheritance: 1) The Interface doesn't need to instantiate
                                      2) The methods of Interface must complete
                                      
                                      import abc
                                      class Interface(metaclass=abc.ABCMeta):
                                           @abc.abstractmethod
                                           def func(self): pass
                                      
                                      class Child(Interface):
                                           def func(self): # code
           
           
            4. Multi-Inheritance:  1) DEFINE:
                                         class A(): def __init__(self)
                                         class B(): def __init__(self)
                                         
                                         class C(A, B): 
                                              def __init__(self):
                                                 super(C, self).__init__(?) 
                                                 
                                      *DISCIPLINE: Nearby principle to find the '__init__(self)' of Father
                                   
                                   2) Search Inherited tree:  
                                              C.__mro__   # Return a List
                                                                           
                                   3) MIXIN: 1> Decide a main inheritance threading
                                             2> Maxin other properties.
'''


'''
Polymorphism: 1. DEFINE: 不同对象调用相同属性，结果不同

              2. DISCIPLINE: OPEN: For a Father class, we can add some attr by inheriting
                             CLOSED: For a operation function, it can perform polymorphism without changing code. 
'''
# class Animal(object):
#     pass
#
# class Dog(Animal):
#     def run(self):
#         print('The dog is running')
# class Cat(Animal):
#     def run(self):
#         print('The cat is running')
#
# def Run_twice(animal):
#     animal.run()
#     animal.run()
#
# Run_twice(Dog())
# Run_twice(Cat())


'''
Encapsulation: 1. Type of attr(variable, function) in class:
                  __variable__, __function__(): Dunder Method
                  __variable, __function(): Private, can't call for by the outer # __variable -->  _ClassName__variable

               2. Encapsulate: 1) Design attr Privately
                               2) Expose set() and get() to outer for setting or getting attr
                                  def set_name(self, name):
                                      self.__name = name
                                  def get_name(self):
                                      return sefl.__name

                                  @property
                                  def name(self):
                                      return self.__name
                                  @name.setter
                                  def name(self, name):
                                      self.__name = name
                                      
                               OR:   Attr_name = property(get_func,set_func,delete_func)

'''
# class Student(object):
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#     @property
#     def age(self):
#         return self.__age
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#     @age.setter
#     def age(self,age):
#         self.__age = age
#
#     def printInf(self):
#         print('This is %s, %d years old' % (self.__name, self.__age))
#
# s = Student('xzq', 24)
# s.printInf()
# s.name = 'John'
# s.age = 24
# s.printInf()


'''
Get Info of Class:  1. GET Type:                           type(obj)
                    2. GET Inheritance:                    isinstance(obj, Class)  issubclass(child, father)
                    3. GET all Attr (with out value):      dir(obj)  # List
                    4. OPERATE Attr:  Reflect
                                          hasattr(obj, 'attr')
                                          getattr(obj, 'attr', ['default'])
                                          setattr(obj, 'attr')
                                          delattr(obj, 'attr') 
                                          
                                      # Use reflection: 
                                            if hasattr(f1,'get'):
                                                func_get = getattr(f1,'get')
                                                func_get()
                                            else:
                                                # Running other code
                                          
                                      Import modules dynamically('str')
                                          1) m = __import__('module.class')    # m = module
                                          2) m = importlib.import_module('module.class')   # m = module.class
'''