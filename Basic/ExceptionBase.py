'''
Exception: Flow, assert

'''
'''
Exception: 1. DEFINE:
                     try:
                         code1
                         if condition: 
                              raise Exception      # 主动触发异常
                         code2
                     except Exception as e:
                         code3
                     else:
                          code4                    # try 没有异常执行code4
                     finally:
                         code4

                     Tips: # Flow: code1 -> code2 -> code3 -> code4
                           # The essence of 'Exception' is a Class, and 'e' is a instance of this 'Exception'
                             Thus we can define 'OurException' by inheriting from 'Exception'
'''
class OurException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def printError(self):
        print('Denominator should not equal 0')


try:
    b = 0
    if b == 0:
        raise OurException
    a = 10 / b
    print(a)
except OurException as e:
    e.printError()
finally:
    print('End')


'''
assert:  1. Using:
                  code1 :return value
                  assert value == exc_value
                  code2
                  
         2. Flow:  if 'code1' return exc_value, then execute 'code2'
'''