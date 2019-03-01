'''
Function: Definition, build-in functions
'''
'''
Definition & Call For Function: 
          def func(a, b=2, *arg, c=3, **kwargs):pass
                   a: POSITIONAL, can't omit when call for
                   b: KEYWORD(default): reserved in __defaults__: (2, ), can omit or revise when call for
                   *arg: VAR_POSITIONAL: reserved in arg: (, )
                   c: KEYWORD_ONLY: reserved in __kwdefaults__: {'c': 3}, can omit or revise but must be rewrite clearly, e.g. 'c=5' or {'c':5}
                   **kwargs: reserved in kwargs: dict
          
          if plunge paras into function as 'args'(tuple) or 'kwargs'(dict): 1) reserved a, b, c first
                                                                            2) reserved the remains into corresponding 'arg' or 'kwargs'
'''
def func(a, b=1, *args, c=3, **kwargs):
    print(a, b, c)
    print(args)
    print(kwargs)

args = ('xzq','love','Cindy')
kws ={'name':'xzq','c':4, 'age': 18}
func(*args, **kws)
print(func.__defaults__)
print(func.__kwdefaults__)

'''
Function Error: TypeError: 1) plunge wrong number of arguments
                           2) plunge wrong type of arguments
'''
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('Wrong type of argument')
#     if x >= 0:
#          return x
#     else:
#         return -x    # function will return a tuple
# print(my_abs('-99'))
