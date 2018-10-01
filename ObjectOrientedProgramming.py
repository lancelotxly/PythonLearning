'''
Object oriented programming: module, class and instance, inheritance and polymorphism, multiple inheritance
'''
'''
modules: packages
            |--modules
                 |--classes
                   |--functions
'''

'''
class and instance:
                   class className(father):
                         # cls, belongs to class
                         Field
                         @classmethod
                         def function(cls):
                         
                         # self, belongs to instance
                         def __init__(self):
                         def function(self):    
                         
                  type of variables and functions:   __varable, __function   # private, visited only by the class
                                                     _varable, _function  # protected, visited only by the class or its children
                                                                       
'''
# class Student():
#     Name = 'Cindy'
#     @classmethod
#     def printName(cls):
#         print('xzq love %s' % cls.Name)
# Student.printName()

# class Student():
#     GradeNumber = 2
#     ClassNumber = 1
#     __StudentNumber = 50
#     @classmethod
#     def _printClassInf(cls):
#         print('There are %d students in class %d grade %d' % (cls.__StudentNumber, cls.ClassNumber, cls.GradeNumber))
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def _printStudentInf(self):
#         print('this is %s, %d years old' % (self.name, self.age))
#
# class Boy(Student):
#       def __init__(self,name,age):
#           Student.__init__(self,name,age)
#
# s = Student('Cindy',18)
# s._printStudentInf()
# Student._printClassInf()
# b = Boy('xzq',18)
# classNumber = Boy.ClassNumber
# gradeNumber = Boy.GradeNumber
# b._printStudentInf()

'''
inheritance and polymorphism:
                             class father():
                                  def __init__(self):
                                  def function(self):
                            
                             class child(father):
                                  def __init__(self):    # if father has __init__(), child must rewrite it, 
                                      father.__init__(self)   # furthermore if child wants use the father's __init__(), must calls it obvoiusly
                             
                             polymorphism:
                                 Claim the type of father class, and use its functions may perform different on the children classes.
                                 even the class isn't a child of father, if only it has the function, it could perform polymorphism.
'''
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printInf(self):
        print('this is %s, %d years old' % (self.name, self.age))

class Boy(Student):
    def __init__(self,hometown):
        self.hometown = hometown

    def printInf(self):
        print('his hometown is %s' % (self.hometown))

class girl():
    def printInf(self):
        print('Cindy comes from Zhangzhou, Fujian')

def printInf(a):
    a.printInf()

s = Student('Cindy',18)
b = Boy('Chongqing')
g = girl()
printInf(s)
printInf(b)
printInf(g)