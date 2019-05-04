'''
Modules: Modules Structure
         time, random, os, sys, logging, hashlib
         re
         json, pickle, xml, configparser, io
'''
'''
Modules: 1. Structure: 
                     package
                       |-- __init__.py # necessary, also a 'Module'
                       |-- module1
                              |-- class
                              |-- function
                       |-- module2
                       |-- function

             module1.py:      __name__ == '__main__'
             module2.py:      import module1
                              module1.__name__ == 'module1'

        2. Import Module: module1.py
                  import module2.py               # abspath(module1.py) + module2.py
                  
                  import sys,os
                  BASE_DIR = os.path.dirname(os.path.dirname(__file__))
                  sys.path.append(BASE_DIR)
                  from module3 import module2     # abspath(module1.py) + module3/module2

'''

'''                 
time:  1. Three Types of Time:  1) Format         # Expression,  %Y年 %m月 %d日 %X时间(%H时 %M分 %S秒) %a星期
                                2) Struct_Time    # Save Info
                                3) Timestamp      # Calculate

       2. Transform: 1) Timestamp --> Struct_Time:  time.localtime([time.time()])
                     2) Struct_Time --> Timestamp:  time.mktime(time.localtime())
                     3) Struct_Time --> Format:  time.strftime(format,time.localtime())
                        Format --> Struct_time:  time.strptime('str',format)

                     4）Struct_Time --> Format(Static): time.asctime(time.localtime())
                     5) Timestamp --> Format(Static): time.ctime(time.time())

                     *) datatime.datatime.now()

       3. time.sleep(num)
'''

'''
random:  .random()         # [0,1] float
         .randint(a,b)     # [a,b] int
         .randrange(s)     # (0,s) int
         .choice(Seq)      # select x from Seq
         .shuffle(Seq)     # Shuffle Seq

         .uniform(a,b)             #  Uniform distribution
         .expovariate(lambda)      #  Exponent distribution
         .gauss(mu,sigma)          #  Gaussian distribution
         .lognormvariate(mu,sigma) #  Lognormal distribution
'''

'''
os: 与操作系统交互
    1. 基本操作
            1. 操控系统
               os.chdir('path')                  # cd: path
               os.chdir('..')                    # 返回上一级
               os.system('bash cmd')             # 运行shell命令
               
            2. 操作目录/文件
               os.mkdir('dirname')                                   # 创建目录
               os.rmdir('dirname')                                   # 删除目录(目录为空)
               os.makedirs('dirname1/dirname2')                      # 递归创建目录
               os.removedirs('dirname1/dirname2')                    # 递归删除目录(目录为空)
               
               os.list('dirname')                                    # 列出该目录下的所有文件, 返回列表
               os.remove('filename')                                 # 删除文件
               os.rename('old_name', 'new_name')                     # 重命名文件/目录
            
            3. 操作路径
               os.getcwd()                       # 当前工作路径
               os.curdir                         # 当前目录   '.'
               os.pardir                         # 上一级目录  '..'
               os.sep                            # 路径分隔符  \\
               os.linesep                        # 行终止符    \t\n
               os.pathsep                        # 文件分隔符  ;
               
               os.path.abspath(path)             # 返回规范化绝对路径
               os.path.split(path)               # (上一级目录, 最后一级目录)
               os.path.dirname(path)             # 上一级目录
               os.path.basename(path)            # 最后一级目录
               os.path.splitext(file)            # (文件名, 文件格式)
               os.path.join(path1, path2)        # 连接路径
               
               os.path.exists(path)              # 判断路径是否存在
               os.path.isdir(path)               # 判断是否为目录
               os.path.isfile(path)              # 判断是否为文件
               
               os.path.normcase(path)            # 路径格式规范化
               
               
               os.urandom(n)                  # 生成n位二进制字符串
               
    2. 应用
      POSSIBLE_DIR = os.path.normcase(os.path.join(
                    os.path.abspath(__file__),
                    os.pardir,
                    os.pardir,
                    os.pardir
      ))
      sys.path.insert(0,POSSIBLE_DIR)
       
'''

'''
sys: 1. DEFINE: sys operation
     2. OPERATE:
             .argv    # Return List = [ModuleName.py, para1, para2..]  includes paras in Command line.
             .path    # Return List = [path1, path2,..]  includes paths for searching modules
             .exit()  # End 'ModuleName.py'
             .stdout.write('str')  # Write into memory
             .stdout.flash()       # Flash memory
'''

'''
logging: 1. DEFINE: log record
         2. Config:
                  1> Config file:
                     Config_file = {'level':logging.DEBUG,
                                     'format': '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                     'datefmt':'%Y年 %m月 %d日 %X时间(%H时 %M分 %S秒) %a星期',
                                     'filename': 'test.log',
                                     'filemode': '[a]w'
                     }
                     logging.basicConfig(**Config_file)

                  2> logger obj
                      def logger():
                             logger = logging.getLogger(['Child_logger'])

                             fh = logging.FileHandler('filename')               # 记录到文件
                             sh = logging.StreamHandler()                       # 显示到屏幕

                             fmt = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
                             fh.setFormatter(fmt)
                             sh.setFormatter(fmt)

                             logger.addHandler(fh)
                             logger.addHandler(sh)
                             logger.setLevel('DEBUG')
                             return logger

                  Tips: 1. Child_logger's name unique.
                        2. Child_logger will log father_logger record.

         3. Log:
           logging.debug('debug message')
           logging.info('info message')
           logging.warning('warning message')
           logging.error('error message')
           logging.critical('critical message')


'''
# import logging
# Config_file = {'level':logging.DEBUG,
#                'format':'%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                'filename':'test_log.log',
#                'filemode':'w'}
# logging.basicConfig(**Config_file)
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')


import logging
def logger():
    logger = logging.getLogger()
    fh = logging.FileHandler('test_log')
    sh = logging.StreamHandler()

    fmt = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    fh.setFormatter(fmt)
    sh.setFormatter(fmt)

    logger.addHandler(fh)
    logger.addHandler(sh)
    logger.setLevel(logging.DEBUG)
    return logger

logger = logger()
logger.debug('hello')


'''
hashlib: 1. DEFINE: Hash encode
         2. OPERATE: 
                    md5 = hashlib.md5()
                    md5.update('str'.encode('utf-8'))    
                    str_hash = md5.hexdigest()      # 返回摘要， 十六进制字符串
                    byte_hash = md5.digest()        # 返回摘要， 二进制字符串

hmac: 1. DEFINE: key-encode
      2. OPERATE:
                 h = hmac.new('key'.encode('utf-8'))
                 h.update(b'msg')
                 or:
                 h = hmac.new(b'key',b'msg')
                 
                 str_encode = h.hexdigest()         # 返回摘要， 十六进制字符串
                 byte_hash = h.digest()             # 返回摘要， 二进制字符串
                 True/False = hmac.compare_digest(b'abc',b'123')    # 比较两个二进制字符串是否相同

'''

'''
正则表达式:
              1) 常规的: 写啥匹配啥
              2) 元字符: 
                        1>  .     # 通用匹配符, 但只能代表一个字符
                        2>  ^a    # 字符串必须以'a'开头 
                        3>  a$    # 字符串必须以'a'结尾
                        4>  |     # 表示'or'
                        
                        贪婪匹配: 按最多的来
                        5>  d*     # [0,inf), 最少匹配空字符(字符串结尾的空字符也匹配), 最多匹配无穷多个'd'字符 
                        6>  d+     # [1,inf), 最少匹配一个'd'字符, 最多匹配无穷多个'd'字符  
                        7>  d?     # [0,1], 最少匹配空字符, 最多匹配一个'd'字符
                        8>  d{n,m} # [n,m], 最少匹配n个'd'字符, 可设置上限为m个'd'字符
                        
                        惰性匹配: 按最少的来
                        9>  d*?   # 匹配空字符
                        10>  d+?  # 匹配一个'd'字符 
                        
                        字符集        
                        11> [abc]   # 字符集每一个字符都会依次匹配
                            在字符集中: 
                                      -    # 从...到...
                                      ^    # 取反
                            \: 表示转义字符, 即将原来有特殊意义的字符变为没有特殊意义, 将原来有特殊意义的字符变为没有特殊意义
                               在翻译字符时, python先解释, 再执行re模块的解释
                               如: 
                                   (1)在正则表达式\b表示字符边界, 但'\b'在python中有特殊意义, 因此正则表达式应写为
                                      r'\\b'
                                   (2)正则表达式想表示'\v',应写为
                                      r'\\\\v'          
                            常用字符集:
                                      \d: [0-9]          \D: ^[0-9]
                                      \s: [\t\n]         \S: ^[\t\n]
                                      \w: [a-zA-Z0-9]    \W: ^[a-zA-Z0-9]      
                        
                        分组
                        12> (abc)          # 以整体匹配
                        13> (?P<name>abc)  # 分组命名
                        14> (?:abc)        # 去分组      
''' # 正则表达式

'''
re: 
    1. 方法:
           查找:
           1) re.findall(r'', 'strs')                       # 返回一个list, 包含所有满足正则表达式的结果
           2) ret = re.search(r'', 'strs')                  # 返回分组,  搜索匹配, 只匹配一个
           3) ret = re.match(r'', 'strs')                   # 返回分组, 从头开始匹配, 只匹配一个
           4) ret_iter = re.finditer(r'', 'strs')           # 返回一个iterator, 匹配所有, 每一项是分组
           * 对于返回分组的取值:
             ret.group()         # 获取全部分组
             ret.group(i)         # 获取第i个分组, i从1开始
              
           修改:   
           5) re.split(r'', 'strs')       # 返回list, 按正则表达式对'strs'进行字符串分割, 同str.split()
           6) re.sub(r'','str1','str2')   # 返回str, 按正则表达式搜索'str2',将第一次匹配到的字符替换为'str1'
           7) re.subn(r'','str1','str2')  # 返回(new_str,n), 按正则表达式搜索'str2',将所有匹配到的字符替换为'str1'
           
           制作re对象: 可调用所有re方法
           8) re_operator = re.compile(r'')                                            
''' # re模块


'''
json & pickle: 
              1. json: 
                      1) DEFINE: Operate Base on 'dict', Can't Save 'obj'
                      2) OPERATE:
                                 1> Write into: 
                                              with open('filename','w',encoding='utf-8') as f:
                                                        # data
                                                        data_json = json.dumps(data)       # str --> str_json
                                                        json.dump(data,f)                  # 1) str --> str_json  2) f.write(str_json)
                                 2> Loading:
                                              with open('filename','r',encoding='utf-8') as f:
                                                        data = json.loads(data_json)       # str_json --> str
                                                        data = json.load(f)                # 1) f.read() --> str_json  2) str_json --> str


              2. pickle: 
                      1) DEFINE: ONLY python, Can save 'obj'
                      2) OPERATE:
                                 1> Write into:
                                              with open('filename','wb') as f:
                                                        # data
                                                        pickle.dump(data,f)

                                 2> Loading:
                                              with open('filename','rb') as f:
                                                        data = pickle.load(f)    
'''
# import pickle
# with open('data.pickle','rb',) as f:
#       data = pickle.load(f)
#       print(data)
#
# with open('data.json','wb') as f:
#       data2 = {'John':123}
#       pickle.dump(data2,f)


'''
xml: 1. DEFINE:  import xml.etree.ElementTree as ET

     2. OPERATE: Operate base on Node obj,
                 Node attr:  node.tag          #   'str', Node name
                             node.attrib      #   dict = {'attr':'attr_value'}
                             node.text         #   'str', Node value

                1> Generate .xml file:
                   father_node = ET.Element('father_node')
                   child_node = ET.SubElement(father_node, 'child_node',attrib={'attr':'attr_value'})
                   child_node.text = 'value'

                   et = ET.ElementTree(father_node)                                   # Generate document obj 
                   et.write('filename.xml',encoding='utf-8',xml_declaration=True)     # Generate  document

                2> tree = ET.parse('filename.xml')                                    # Get document obj
                   root = tree.getroot()                                              # Get root obj
                   1>> Traverse:
                               for child in root:                                     # child is also an obj
                   2>> Search: 
                              node.findall('node_name')                               # Find out all children nodes named 'node_name'
                              node.find('node_name')                                  # Find out a child node named 'node_name'
                              node.getchildren()                                      # Return all children nodes
                   3>> Rewrite:
                              node.tag = new_tag
                              node.attrib = {'attr':'attr_value'}
                              node.text = new_value
                              tree.write('filename.xml')

                   4>> Delete:
                             node.remove(node obj)                                    # Delete child node                 
'''
# import xml.etree.ElementTree as ET
# data = ET.Element('data')
# Score_table1 = ET.SubElement(data, 'Score_table',attrib={'name':'Class_1'})
# Student_xzq = ET.SubElement(Score_table1,'Student',attrib={'name':'xzq'})
# Student_xzq.text = '100'
# Student_John = ET.SubElement(Score_table1,'Student',attrib={'name':'John'})
# Student_John.text = '90'
# Score_table2 = ET.SubElement(data, 'Score_table',attrib={'name':'Class_2'})
#
# et = ET.ElementTree(data)
# et.write('data.xml',encoding='utf-8',xml_declaration=True)

# import xml.etree.ElementTree as ET
# tree = ET.parse('data.xml')
# root = tree.getroot()
# children = root.getchildren()
# print(children[1].attrib)
# root.remove(children[1])
# tree.write('new.xml')


'''
configparser: 1. DEFINE: Generate config file
                                [DEFAULT]
                                ServerAliveInterval = 45
                                Compression = yes
                                CompressionLevel = 9
                                ForwardX11 = yes

                                [bitbucket.org]
                                User = hg

                                [topsecret.server.com]
                                Port = 50022
                                ForwardX11 = no
              2. OPERATE: Base on dict
                          1.Generate config file:
                                config = configparser.ConfigParser()          # Generate config obj
                                config["DEFAULT"] = {'ServerAliveInterval': '45',
                                                      'Compression': 'yes',
                                                      'CompressionLevel': '9'}
                                config['bitbucket.org'] = {'User':'hg'}
                                config['topsecret.server.com'] = {'Port': '50022', 'ForwardX11':'no'}

                                with open('filename','w') as f:
                                   config.write(f)

                          2. Operate as a dict:
                             1> GET
                                config.read('filename')                      # Load
                                config[section_name][attr_name]              # Get info
                                config.sections()                            # Return a List, includes all sections except [DEFAULT]
                                config.options(section_name)                 # Return a list, includes all attr_name of 'section_name' and [DEFAULT]
                                config.items(section_name)                   # Return a tuple, includes all items of 'section_name' and [DEFAULT]

                             2> Add
                                config.add_section(new_section)
                                config.set(new_section,attr,value)
                             3> Rewrite
                                config[section_name][attr_name] = new_value
                             4> Delete
                                config.remove_section(section_name)
                                config.remove_option(section_name,attr)
                                with open('filename','w/a') as f:
                                   config.write(f)
'''

'''
StringIO and ByteIO: StringIO 
                     1. f = io.StringIO(' ') <--> f.read(), f.readline(), for item in f:
                     2. f = io.StringIO()
                        f.write(' ')    <-->  f.getvalue()

                    BytesIO
                    1. f = io.BytesIO(b' ')   <--> f.read(), f.readline(), for item in f:
                    2. f = io.BytesIO()
                       f.write(b' ')  <--> f.getvalue()
'''
# from io import StringIO
# f = StringIO('''John loves Cindy, but he never told her.
# What a pity thing!
# But he thinks it's a pure love.
# ''')
# for item in f:
#     print(item)

#
# f = StringIO()
# f.write('''John loves Cindy, but he never told her.
# What a pity thing!
# However, he thinks it's a pure love.
# ''')
# data = f.getvalue()
# print(data)

# from io import BytesIO
# f = BytesIO('''
# John loves Cindy, but he never told her.
# What a pity thing!
# However, he thinks it's a pure love.
# '''.encode('utf-8'))
#
# for item in f:
#     print(item.decode('utf-8'))

# f = BytesIO()
# f.write(b'''John loves Cindy, but he never told her.
# What a pity thing!
# However, he thinks it's a pure love.
# ''')
#
# data = f.getvalue().decode('utf-8')
# print(data)