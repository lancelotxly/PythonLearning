'''
exception, unit test, debug
'''

'''
exception: try:
                code1
                raise Exception
                code2
           except Exception as e:   
                code3
           finally:
                code4
           
           # code1->code2->code3->code4
           # the essence of exception is a class, and e is a instance of this exception, 
             thus we can define our exception by inheriting from Exception
'''
# class OurException(Exception):
#     def printErro(self):
#         print('Denominator should not equal 0')
#
# try:
#     a = 10/0
#     raise OurException
#     print(a)
# except OurException as e:
#     e.printErro()
# finally:
#     print('End')

'''
unit test:  unittest.TestCase
'''
# class Dict():
#     def __init__(self,**kwargs):
#         for key,value in kwargs.items():
#             self[key] = value
#
#     def __getitem__(self, item):
#         try:
#             return self.__dict__[item]
#         except KeyError:
#             return AttributeError(r" 'Dict' object has no attr %s" % (item))
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value


class Dict(dict):

    def __init__(self, **kw):
        super(Dict,self).__init__(**kw)   # after initializing, __dict__={}

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value




import unittest

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == "__main__":
     unittest.main()