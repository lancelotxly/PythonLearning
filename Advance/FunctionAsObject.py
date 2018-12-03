'''
Function as the 'Primary object': 1) build during program running
                                  2) can plunge into 'variable', 'Sequence','Dict','Set'
                                  3) as paras be transmitted into another 'Function'
                                  4) return a 'Function'
                                  # e.g. 'num','str','sequence','dict','set' are all 'Primary object'

important methods or attrs of func: __call__():  # method, callable
                                    __code__: object, __defaults__: tuple, __kwdefaults__: dict # saving about params
                                    __annotations__: # dict, annotations about params

                                    __globals__: dict, global variable
                                    __name__: name of the func
                                    __doc__: help document
                                    __dict:  dict, attrs of func

callable: all objects which have implemented '__call__()'
         1) functions and anonymous functions ('lambda')
         2) build-in functions
         3) functions defined in 'Class'
         4) Class(), calls for 'Class': #1. __new__ build a object, and calls for __init__
                                        #2. __init__ initialize the object and return it
         5) object of the 'Class' which has implemented __call__
         6) generate function
         # To judge a object whether or not callable, 'callable(object)'

Definition:
          def func(a,b=2,*args,c=3,**kwargs): pass
                   ^  ^    ^     ^    ^
                   |  |    |     |    |__ VAR_KEYWORD: reserved in kwargs: {}
                   |  |    |     |__ KEYWORD_ONLY: reserved in __kwdefaults__: {'c':3}, can omit,but when default absent, you must write in clearly
                   |  |    |__ VAR_POSITIONAL: reserved in args: (, )
                   |  |__ KEYWORD(default): reserved in __defaults__: (2, ), can omit or revise
                   |__ POSITIONAL: can't omit
          # if plunge paras like: **kwargs or *arg: 1) reserved a,b,c
                                                    2) then reserved the remains into corresponding 'arg (tuple)' or 'kwarg (dict)'

Saving about params:
          __code__: an object, reserve attrs: __code__.covarnames # all inclusive params of the func, and the first 'argcount' are plunged args
                                              __code__.argcount # the number of plunged args
          __defaults__: a tuple, reserve the defaulted args
          __kwdefaults: a dict, reserve the keyword-only args

          sig = inspect.signature(func)
          sig.parameters: a dict, {'name':'param'}, where 'param' is an object include: 1. param.kind
                                                                                        2. param.default
          sig,bind(**params) # the framework can use this method to verify the params and introspect the required params

__annotations__: def clip(text:str, max_len:'int > 0'=80) -> str
                 which will be reserved in __annotations__, a dict, i.e
                 {'text':<class 'str'>, 'max_len':'int > 0', 'return':<class 'str'>}

__dict__: for 'Class', reserve methods and attrs
          for 'object', reserve attrs in __init__
          for 'function', reserve the attrs of func, e.g  def func():pass;  func.name='xzq' # where '__dict__={'name':'xzq'}'

##
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

    operator: 1) calculate: add, iadd, sub, isub, mul, imul, mod, imod, pow,
              2) get data or attr value: itemgetter(index), attrgetter(attr)
              3) methodcaller('methodname') # where the method must be in the object

    functools: functool.partial(func,para)
'''
# # __call__()
# import random
# class BingoCage():
#     def __init__(self,items):
#         self._items = list(items)
#         random.shuffle(self._items)
#
#     def pick(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('pick from empty BingoCage')
#
#     def __call__(self, *args, **kwargs):
#         return self.pick()

# # __dict__ of func
# def upper_case_name(obj):
#     return ('%s %s' % (obj.first_name, obj.last_name)).upper()
# upper_case_name.short_description = 'Custormer name'
# print(upper_case_name.__dict__)

# # Definition
# def tag(name, *content, cls=None, **attrs):
#     '''generate html tags'''
#     if cls is not None:
#         attrs['class'] = cls
#     if attrs:
#         attrs_str = ''.join (' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
#     else:
#         attrs_str = ''
#     if content:
#         return '\n'.join('<%s%s>%s</%s>' % (name,attrs_str,c,name) for c in content)
#     else:
#         return '<%s%s />' % (name,attrs_str)
# print(tag('br'))
# print(tag('p','hello','world'))
# # inspect.signature.bind()
# import inspect
# sig = inspect.signature(tag)
# my_tag = {'name':'img','title':'Sunset','src':'sunset.jpg','cls':'framed'}
# bound_args = sig.bind(**my_tag)


# # __defaults__, __kwdefaults__, __code__
# def clip(text, max_len=80,*,c=3,**kwargs):
#     end = None
#     if len(text) > max_len:
#         space_before = text.rfind(' ',0,max_len)
#         if space_before >= 0:
#             end = space_before
#         else:
#             space_after = text.rfind(' ', max_len)
#             if space_after >= 0:
#                 end = space_after
#     if end is None:
#         end = len(text)
#     return text[:end].rstrip()
# print(clip.__defaults__, clip.__code__, clip.__code__.co_varnames, clip.__code__.co_argcount)
# # inspect.signature
# from inspect import signature
# sig = signature(clip)
# for name, param in sig.parameters.items():
#     print(param.kind, ':', name, '=', param.default)

