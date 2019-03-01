'''
Object Oriented Programming: Module, Class and Instance, Get Information,  Encapsulation, Inheritance, Polymorphism, Multi-Inheritance.
'''
'''
Anaconda, git, pycharm base
'''

'''
Modules: package
            |-- __init__.py # necessary, also a 'Module'
            |-- module
                  |-- class
                        |-- function
                  |-- function
'''

'''
Get Info of Class:  1. GET Type:          type(obj)
                    2. GET Inheritance:   isinstance(obj, Class)
                    3. GET all Attr:      dir(obj)
                    4. OPERATE Attr:  Reflect
                                          hasattr(obj, 'attr')
                                          getattr(obj, 'attr')
                                          setattr(obj, 'attr')
                                          delattr(obj, 'attr') 
                                          
                                      Import modules dynamically('str')
                                          1) m = __import__('module.class')    # m = module
                                          2) m = importlib.import_module('module.class')   # m = module.class
'''
'''
Class and Instance: 1. DEFINE:
                       class ClassName(father):
                           # cls, belongs to class
                           variable
                           @classmethod
                           def func(cls):
                           
                           # self, belongs ot instance
                           def __init__(self,a,b):  # Instance variable
                           def func(self): # Instance method
                    
                    2. BUILD INSTANCE:
                       c = ClassName(a, b)
'''
# class Student(object):
#     Hometown = 'CHONG QING'
#     @classmethod
#     def printWelcome(cls):
#         print('Welcome to Njupt')
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def printInf(self):
#         print('This is %s, comes from %s, %d years old' % (self.name, Student.Hometown, self.age))
#
# xzq = Student('xzq',24)
# xzq.printInf()
# xzq.printWelcome()
# print(Student.Hometown)
# xzq.printInf()

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
Inheritance: 1. DEFINE:
                       class Father(object):
                           # cls
                           def __init__(self, a, b):
                                pass
                           def func1(self):
                                pass
                        
                       class Child(Father):
                           # cls
                           def __init__(self, a, b, c):
                              super(Child, self).__init__()
                              self.c = c
             
             2. DISCIPLINE: 1) Child has all attr and func of the Father
                            2) Child can add its own attr and func
                            3) When Initialize, plunge paras into the Father attr primarily.
                          
'''
# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def printInf(self):
#         print('This is %s, %d years old' % (self.name, self.age))
#
# class Boy(Student):
#     def __init__(self, name, age, hometown):
#         super(Boy, self).__init__(name, age)
#         self.hometown = hometown
#     def printHometown(self):
#         print('The boy comes from % s' % self.hometown )
#
# s = Student('xzq', 24)
# s.printInf()
# b = Boy('John',23,'CQ')
# b.printHometown()

'''
Polymorphism: 1. DEFINE: 1) Define a function: 'def func(Father): Father.attr'
                         2) Call for: 'func(Child1)' or 'func(Child2)'
                         3) Execute: 'Child1.attr' or 'Child2.attr'
              
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
Multi-Inheritance: 1. DEFINE:
                             class A(): def __init__(self)
                             class B(): def __init__(self)
                             
                             class C(A, B): 
                                  def __init__(self):
                                     super(C, self).__init__(?) 
                   2. DISCIPLINE: Nearby principle to find the '__init__(self)' of Father
                   
                   3. MIXIN: 1) Decide a main inheritance threading
                             2) Maxin other properties.
'''
# class A():
#     # def __init__(self,a):
#     #     print(a)
#     pass
#
# class B():
#     def __init__(self, a, b):
#         print(a+b)
#
# class C(A, B):
#     def __init__(self,a,b):
#         super(C,self).__init__(a,b)
# c = C(1,2)

# class Animal():
#     pass
#
# # the main inheritance threading
# class Mammal(Animal):
#     pass
#
# class Bird(Animal):
#     pass
#
# # define perporties
# class Runable():
#     pass
# class Flyable():
#     pass
#
# # Mixin properties
# class Dog(Mammal,Runable):
#     pass
# class Parrot(Bird, Flyable):
#     pass

