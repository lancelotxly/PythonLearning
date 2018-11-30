'''
Function as the 'Primary object': 1) build during program running
                                  2) can plunge into 'variable', 'Sequence','Dict','Set'
                                  3) as paras be transmitted into another 'Function'
                                  4) return a 'Function'
                                  # e.g. 'num','str','sequence','dict','set' are all 'Primary object'

Higher-order function: accept a function as para, and return anther function
                       Iterable = map(func, iterable)
                       Iterable = filter(func, iterable)
                       # where 'map' and 'filter' are equivalent to '[func(x) for x in iterable if func]' in listcomps or generator
                       Iterable = sorted(iterable, key=func, reversed=[False/True])

                       functools.reduce(func, iterable)  # f(f(f(x1),x2),x3) for x1,x2,x3...in iterable
                       functools.partial()
                       functools.partialmethod()

                       sum(list/tuple)  # calculate the sum
                       max(list/tuple)
                       min(list/tuple)

                       A subtle 'func' to recommend: 'lambda x: f(x)'

callable: all objects which have implemented __call__
         1) functions and anonymous functions ('lambda')
         2) build-in functions
         3) functions defined in 'Class'
         4) Class(), calls for 'Class': #1. __new__ build a object, and calls for __init__
                                        #2. __init__ initialize the object and return it
         5) object of the 'Class' which has implemented __call__
         6) generate function
         # To judge a object whether or not callable, callable(object)

Definition:
          def func(a,b=2,*args,c=3,**kwargs): pass
                   ^  ^    ^     ^    ^
                   |  |    |     |    |__ other kws: reserved in kwargs: {}
                   |  |    |     |__ keyword-only: reserved in __kwdefaults__: {'c':3}, can omit,but when without default must write in
                   |  |    |__ other args: reserved in args: (, )
                   |  |__ default arg: reserved in __default__: (2, ), can omit or revise
                   |__ args: can't omit
          # if plunge paras like: **kwargs or *arg: 1) reserved a,b,c
                                                    2) then reserved the remains into corresponding 'arg (tuple)' or 'kwarg (dict)'

'''
# # __call__
# import random
#
# class BingoCage():
#     def __init__(self,items):
#         self._items = list(items)
#         random.shuffle(self._items)
#
#     def pick(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('pick from empty BingCage')
#
#     def __call__(self, *args, **kwargs):
#         return self.pick()

# __default__, __kwdefault__, arg= (, ), kwarg = {}
# def tag(name, *content, cls=None, **attrs):
#     '''generate html tag'''
#     if cls is not None:
#         attrs['class'] = cls
#     if attrs:
#         attr_str = ' '.join('%s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
#     else:
#         attr_str = ''
#     if content:
#         return '\n'.join('<%s %s>%s<%s>' % (name, attr_str, c, name) for c in content)
#     else:
#         return  '<%s%s />' % (name,attr_str)
# print(tag('br'))
# print(tag('p','hello','world',id=3,cls='sidebar'))
#
# def f(a,b=2,*args,c=3,**kw):
#     print(a,b,args,c,kw)
# kws = dict(a=1,b=2,c=3,d=6)
# f(**kws)