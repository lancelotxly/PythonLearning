'''
def function(a, b=1, *args, **kwargs)
        a: 位置参数, 必须有
        b: 默认参数, 默认参数提前存入args中。因此当使用args时要把默认参数预先存入args中，不然会造成重复定义
        *args: 可变参数, 将输入数目可变的变量 存入名为args的tuple中
        **kwargs: 关键字参数，将输入的数目可变的 键值对 存入名为kwargs的dict中
'''
def func(a, b=1, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)

args = (1,'xzq','love','Cindy')
kws ={'name':'xzq', 'age': 18}
func(0,*args, **kws)

def func2(a,b=1):
    print(a,b)
func2(1,2)