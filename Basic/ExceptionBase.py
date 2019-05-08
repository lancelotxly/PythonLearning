'''
异常处理:
       1. 异常处理流程
       2. 自定义异常类
       3. 常见的异常类
       4. 断言: assert 
''' # 综述

'''
异常处理流程:
  1. 对于可预知的异常, 可用if处理
  2. 对于不可预知的异常, 用try..except处理
     try: 
        code1
        if condition:
           raise Exception          # 主动触发异常, 调转异常处理, 执行code3
        code2                       # 没有触发异常, 执行code2
     except Exception as e:         # 异常处理, 异常是一个类, 这里用了上下文管理
        code3  
     else:                          # try整个没有异常执行code4 
        code4
     finally:                       # 不管有没有异常都会执行code5
        code5            
''' # 异常处理流程

'''
自定义异常类: 继承Exception类, 不重写__init__()方法
''' # 自定义异常类: 继承Exception类

'''
常见异常类:
   AttributeError:  访问属性不存在
   IOError:         读写文件出错
   ImportError:     导入模块路径出错
   IndexError:      超出索引
   KeyError:        访问字典中不存在的键
   NameError:       变量未声明
   TypeError:       传入参数类型不对，或者数目不对
   ValueError:      传入值不对, 类型正确
''' # 常用异常类

'''
断言: assert
     # code1: return value
     assert value == exc_value
     # code2
     只有当code1返回期望值时, code2才会执行, 否则报错
''' # 断言

# 下一部分: Network