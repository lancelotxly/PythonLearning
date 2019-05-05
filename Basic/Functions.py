'''
函数: 
      1) 定义
      2) 全局变量和局部变量
      3) 函数的错误
''' # 综述

'''
定义:
     def func(a, b=2, *arg, c=3, **kwargs): pass
         a: POSITIONAL, 调用时不能缺省
         
         b: KEYWORD(default), 保存在内部__defaults__元组中(2, ), 调用时可缺省, 
                              b可修改, 修改后__defaults__中元素不变
                              修改: 1> b = new_v,  不能再使用*arg
                                   2> 通过arg修改: *arg传入
                                                  1,2,*arg 不明确指出  
         
         *arg: VAR_POSITIONAL, 调用时生成arg元组, 将参数保存在其中, 可缺省
                               传参时, 会将除a,b以外的位置参数存入arg
                              
         c: KEYWORD_ONLY, 保存在内部__kwdefaults__字典中{'c':3}, 调用时可缺省, 
                          修改明确指出, 修改后__kwdefaults__中元素不变
                          
         **kwargs: 键值对, 调用时生成kwargs字典, 将参数保存在其中, 可缺省
         
直接通过*arg, **kwargs传参: 1) 先匹配a,b,c
                          2) 再将剩余参数各自存入arg,kwargs中          
''' # 定义和传参

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
全局变量和局部变量:
                1. locals()     # 返回局部变量, {'变量名':值}
                   globals()    # 返回全局变量, {'变量名':值}
                2. global var   # 声明var为全局变量
''' # 全局变量和局部变量

'''
函数的错误类型:  TypeError
            1) 输入参数类型错误
            2）输入参数数目错误 
''' # 函数的错误类型

# 下一章: FunctionProgramming.py






# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('Wrong type of argument')
#     if x >= 0:
#          return x
#     else:
#         return -x    # function will return a tuple
# print(my_abs('-99'))
