class myclassmethod:
    def __init__(self,func):
        self.func = func

    def __get__(self, instance, owner):
        def feedback(*args,**kwargs):
            print('额外功能')
            return self.func(owner,*args,**kwargs)
        return feedback

class Test:
    @myclassmethod
    def func1(cls):
        print('hhh')

Test.func1()
t = Test()
t.func1()
print(Test.mro())