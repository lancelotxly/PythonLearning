'''
数据类型: 1. 包括: 
               基本数据类型: num(int, float), str, bool, None
               高级数据类型: list, tuple, dict, set, slice
         2. 操作:
                 isinstance(a,DataModel)  # 变量是否是某个类型的实例
                 type(a)                  # 变量类型
                 id(a)                    # 变量内存地址
''' # 综述

'''
Num: 1. 数值操作: +, -, *, /, //(取商), %(取余), **(次方)
     2. 数值方法: 
                 1) 进制转换: 
                          1>. int('str',[2,8,16])    # 二进制, 八进制, 十进制(默认),十六进制 字符串 转十进制数值
                          2>. bin(num)               # 十进制(10), 八进制(0o12), 十六进制(0xA) 数值 转二进制字符串
                          3>. oct(num)               # 二进制(0b1010), 十进制(10), 十六进制(0xA) 数值 转八进制字符串
                          4>. hex(num)               # 二进制(0b1010), 十进制(10), 八进制(0o12) 数值 转十六进制字符串
                 
                 2) float('str')              # 将数组str转为float, 有其他字符则报错
                 3) divmod(a,b)               # a/b返回一个tuple, 包括(商,余)
                 4）abs(num)
                 5) max(Iterable,[key=func]), min(Iterable,[key=func])
                 6) sum(Iterable)
''' # Num

'''
Str: 
     1. split: 字符串分割
               1) s.split('a')        # 从左边开始, 将字符串s按'a'分割, 存入list并返回(不包括'a')
               2) s.rsplit('a')       # 从右边开始, 
               3) s.partition('a')    # 从左边开始, 将字符串s按'a'分割成三部分, 存入tuple并返回(包括'a')
               4) s.rpartition('a')   # 从右边开始  
    
     2. strip: 跳过一些字符
               1) s.strip('a')      # 左右检测, 若有'a'则跳过
               2) s.lstrip('a')     # 左边检测, 
               3) s.rstrip('a')     # 右边检测   
               
     3. find: 查找字符串
            s.find('a',i,j)    # 在s中查找'a', 可设置查找的起止点[i,j), 从0开始, 返回'a'在s中的下标
            
     4. count: 计数
            s.find('a',i,j)    # 在s中查找'a'并计数, 可设置查找的起止点[i,j), 从0开始, 返回数值
                   
     5. replace: 替换
                 1) s.replace('a','b',i)            # 将s中的'a'替换为'b', 可设置替换i次 
                 2) replace_map = str.maketrans('a','b')     # 制作替换的规则
                    s.translate(replace_map)                 # 可多次利用
                     
     6. center/ljust/rjust: 字符填充
                 1) s.center(width,'a')       # 字符串's'居中, 其余填充为'a', 总长度为width
                 2) s.ljust(width,'a')        # 字符串's'居左
                 3) s.rjust(width,'a')        # 字符串's'居右
                 
     7. join: 字符连接
                a.join('s')               # 用'a'连接字符串's'的每一个字符 
                            
     8. encode/decode: 字符编码
                        1) 字符串 <--> encode/decode <--> 机器码
                        2) 字符编码的规则: Unicode(2B), ASCII(1B), UTF-8(英语1B, 中文3B)
                        3）用处:  1>>. 保存数据
                                 2>>. 传输数据: 
                                             发送方: 'ABC'.encode('utf-8') ---> b'ABC'
                                             接收方:  b'ABC'.decode('utf-8') ---> 'ABC' 
     
     9. format: 格式化
               1) %:  传递基本数据类型
                     %d int,  %f float,  %s str
                     e.g.  'hi, %s, you have %.2f dollars' % ('Chandler', 18000.509)
               
               2) format: 不光可以传递基本数据类型, 还可以传递对象
                     e.g. 'hi, {0}, you have {1:.2f} dollars'.format('xzq', 18000.509)
                     e.g.  s = Student('xzq',24) 
                          'I am {0.name}, {0.age} years old'.format(s) 
                               
     10. 判断字符串: 返回True/False
                   1) s.startwith('a',i,j)   # 's'是否以'a'开头, 可设置检索区间[i,j)
                   2) s.endswith('a',i,j)    # 's'是否以'a'结尾, 可设置检索区间[i,j) 
                   3) s.isdigit()            #  仅有数字
                   4) s.isalnum()            #  数字和字母
                   5) s.isalpha()            #  特殊字符和字母
                   6) s.isidentifier()       #  标识符
                   7) s.isspace()            #  空格 
                   
     11. 大小写转化: 
                   1) s.upper()            # 每个字母大写
                   2) s.lower()            # 每个字母小写
                   3) s.capitalize()       # 首字母大写
                   4) s.swapcase()         # 大小写转换  
                                    
     12. 字符串拼接:  会产生临时变量
                     'str1' + 'str2'
                     'str'*5
''' # Str: 正则表达式, re见Modules.py

'''
List: 1. 定义: l = [value, ]              # value可以是任意的数据类型: num,str,bool,list,tuple,dict,obj
      2. 操作: 
             get:     a = l[i]              # i从0开始
             
             add:     l.append(value)       # 尾插
                      l.extend(iterable)    # 合并尾插
                      l.insert(i,value)     # 指定位置插, 超过索引则尾插
             
             delete: l.remove(value)    # 删除指定元素
                     l.pop(i)           # 删除指定位置元素，不指定则默认删除末尾
                     l.clear()          # 删除所有元素
                     del l[i]           # 删除指定位置元素, 不指定则删除整个list
             
             rewrite: l[i] = new_value  # 超过所有则报错
             
             search:  i = l.index(value) # 查元素下标
                      count = l.count(value) # 统计元素个数 
      3. 方法:
             list(Seq): 1. 将其他Seq(list, tuple, str)转为List
                        2. 拷贝, 生成新的List对象, 属于深拷贝
                           l1 = [1,2,3]
                           l2 = list(l1)
             
             ** 拷贝的方式: 
                          1. 按对象引用: l1 = [1,2,3], l2 = l1
                          2. 浅拷贝, 不拷贝内部对象: l2 = l1.copy()
                          3. 深拷贝:   l2 = copy.deepcopy(l1)
                                      l2 = list(l1)                               
                     
                           
                
''' # List

'''
Tuple: 不可变类型(hashable), 其他与List类似
       1. 定义: t = (value, )         # value也可以是任意数据类型
       2. 操作: 只有get: a = t[i]
       3. 方法: tuple(Seq): 1.转化
                           2.数据拷贝
''' # Tuple: 只读的List

'''
Dict: 1. 定义: 
              d1 = {k1:v1, k2:v2,...}      # k为不可变数据类型(hashable), 如num, str, tuple, v可以是任意数据类型
              d2 = dict(**kwargs)
              d3 = dict([(k1,v1),(k2,v2),...])
      2. 操作:
             get: a = d[k]       # k不存在会报错  
                  a = d.get(k)   # k不存在返回None
             add: d[new_k] = new_v
             delete: d.pop(k),   del d[k]
             rewrite: d[k] = new_v
      3. 方法:
             dict():  1> 拷贝: dict(Dict)
                      2> 创建: dict(**kwargs), dict([(a,b),])
      4. 遍历:
             for k,v in dict.items():
             for k in dict.keys():
             for v in dict.values():                                             
''' # Dict

'''
Set: 无重复元素, 无序, 不可遍历, 不可变(hashable)
     1. 定义: 
            s = set(list/tuple) # 元素去重
            s = {v1,v2,...}     # v只能是num,str,tuple
     2. 操作: 一般是用来判断数据是否在集合中, 不是用来取值的
            add: s.add(v)
            delete: s.remove(v)     # 删除指定元素
                    a = s.pop()     # 弹出首元素，默认顺序为tuple,str,num
            交集:  s1 & s2
            并集:  s1 | s2
            差集:  s1 - s2           # s1有s2没有的元素          
''' # Set

'''
四大数据类型: List, Tuple, Dict, Set
共有操作: in, not in
         len()
''' # List, Tuple, Dict, Set基本操作

# 下一章: AdvanceFeatures.py

