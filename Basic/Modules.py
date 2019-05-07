'''
Modules: 模块
       1) module的基本常识
       2) 常用的modules:
          time. random, os, sys, logging, hashlib, re
          json, pickle, xml, configparser, io            
       
''' # 综述

'''
module的基本常识:
         1. 结构:
            package
               |-- __init__.py   # 必须的, 也是一个module
               |-- module1
                      |-- class
                      |-- function
               |-- module2
                   
         2. __name__ 属性:
                在module1.py中,  module1.__name__ == "__main__"
                在module2.py中,  module2.__name__ == "module1"  
         
         3. 模块的导入: 
            import:                               
            1) 同一个模块只导入一次, 并加载到内存中
            2) 模块的第一次导入: 
                             1> 为模块创建新的命名空间
                             2> 顺序执行模块中的代码
                             3> 创建变量来引用该命名空间
                             
            from.. import..: 与import不同的是, 直接将module导入到当前的命名空间, 可能会存在执行冲突
            from.. import..as: 模块重命名, 解决冲突
            
         4. 模块的用途: 
                     1) 脚本: 导入时运行
                     2) 调用: 后面调用                         
         
         5. 模块的搜索顺序:
               内存中已经加载的模块 --> 内置模块 --> sys.path中的模块 
               sys.path设置:
                           BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # 退回到根目录, __file__ 为当前文件的目录
                           sys.path.append(BASE_DIR)                                                       
''' # modules的基本常识

'''                 
time: 时间模块
      1. 三种形式的时间:
                     1) Format          # 用于表示  %Y %m %d %X(%H %M %S) %a星期
                     2) Struct_time     # 用于存储信息, 结构体, 可通过属性拿到
                     3) Timestamp       # 用于计算
      2. 转化:
             1) Timestamp --> Struct_time:  time.localtime([time.time()])
             2) Struct_time --> Timestamp:  time.mktime(time.localtime())
             3) Struct_time --> Format:     time.strftime(format,time.localtime())
                Format --> Struct_time:     time.strptime('str',format)
             
             4) Struct_time --> Format(固定格式):  time.asctime(time.localtime())
             5) Timestamp --> Format(固定格式):    time.ctime(time.time()) 
      
      * datetime.datetime.now()        # 获取当前时间                                 
''' # time: 时间模块

'''
random: 生成随机数
        1. 方法: 
               random()        # [0,1] float
               randint(a,b)    # [a,b] int
               randrange(d)    # (0,d) int
               choice(Seq)     # 从Seq随机取一个元素
               shuffle(list)   # 原地打乱list
               
               uniform(a,b)              # 均匀分布
               expovariate(lambda)       # 指数分布
               gauss(mu,sigma)           # 高斯分布
               lognormvariate(mu,sigma)  # lognormal分布
                       
''' # random: 生成随机数

'''
os: 与操作系统交互
    1. 基本操作
            
os: 与操作系统交互
    1. 路径标识符:
            os.curdir            # 当前相对目录, '.'
            os.pardir            # 相对父目录, '..'
            os.sep               # 路径分隔符, '\\'
            os.linesep           # 行终止符, '\r\n'
            os.pathsep           # 文件分隔符, ';'     
    
    2. 操作路径: os.path
            __file__                        # 当前.py文件相对路径
            os.path.abspath(path)           # 规范化绝对路径
            os.path.split(path)             # (上一级目录, 最后一级目录)
            os.path.dirname(path)           # 上一级目录
            os.path.basename(path)          # 最后一级目录
            os.path.splitext(file.py)       # (文件名, 文件格式)
            os.path.join(path1, path2)      # 连接路径    
            
            os.path.exists(path)            # 判断路径是否存在
            os.path.isdir(path)             # 判断是否为文件夹
            os.path.isfile(path)            # 判断是否为文件
            
            os.path.normcase(path)          # 路径格式化 
    
    3. 操控系统
           os.getcwd()                       # 当前工作绝对路径, __file__上一级目录
           os.chdir('path')                  # 进入下级目录 cd: path
           os.chdir('..')                    # 返回上一级
           os.system('bash cmd')             # 运行shell命令  
                               
    4. 操作目录/文件
       os.mkdir('dirname')                                   # 创建目录
       os.rmdir('dirname')                                   # 删除目录(必须目录为空)
       os.makedirs('dirname1/dirname2')                      # 递归创建目录
       os.removedirs('dirname1/dirname2')                    # 递归删除目录(必须目录为空)
       
       os.listdir('dirname')                                 # 列出该目录下的所有文件, 返回列表
       os.remove('filename')                                 # 删除文件
       os.rename('old_name', 'new_name')                     # 重命名文件/目录
   
    5. 应用
      POSSIBLE_DIR = os.path.normcase(os.path.join(
                    os.path.abspath(__file__),
                    os.pardir,
                    os.pardir,
                    os.pardir
      ))
      sys.path.insert(0,POSSIBLE_DIR) 
      
    其他方法:
          os.urandom(i)      # 生成i位随机二进制字符串        
''' # os模块: 操作路径, 文件夹, 文件操作见I_O.py

'''
sys: 操作系统
    1. 属性:
          sys.argv   # 是一个list, 用于存储命令参数 [module.py, p1, p2] 
          sys.path   # 是一个list, 用于存储modules的搜索路径
    2. 方法:
          sys.exit()               # 直接终止程序
          sys.stdout.write('str')  # 写值到内存中
          sys.stdout.flash()       # 刷新内存          
''' # sys模块: 操作系统

'''
logging: 日志模块
         1. 配置日志文件
            方式一: Config_file
                  Config_file = {
                     'filename': 'test.log'                                   # 日志文件名
                     'filemode': 'a/w'                                        # 文件的打开方式: a追加, w重新写
                     'format': ''                                             # 日志格式
                     'datefmt': '%Y年 %m月 %d日 %X时间(%H时 %M分 %S秒) %a星期'   # 时间格式
                     'level': logging.DEBUG                                   # 日志级别
                  } 
                  logging.basicConfig(**Config_file)
                  *'format': 
                            %(asctime)s    # 日志时间, 可用datetime设置
                            %(filename)s   # 调用日志的.py文件
                            %(pathname)s   # .py文件的完整路径
                            %(lineno)s     # .py文件的第几行调用日志
                            %(levelname)s  # 日志级别
                            %(message)s    # 日志内容
            
            方式二:  logger obj          
                  2> logger obj
                      def logger():
                             logger = logging.getLogger(['Child_logger'])

                             fh = logging.FileHandler('filename')               # 记录到文件
                             sh = logging.StreamHandler()                       # 显示到屏幕

                             fmt = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
                             fh.setFormatter(fmt)
                             sh.setFormatter(fmt)
                  def logger():
                        logger = logging.getLogger()            # 创建logger对象 
                        fh = logging.FileHandler('filename')    # 记录到文件
                        sh = logging.StreamHandler()            # 记录到屏幕
                        fmt = logging.Formatter('format')       # 定义日志格式
                        fh.setFormatter(fmt)                    # 传入格式
                        sh.setFormatter(fmt)
                        logger.addHandler(fh)                   # 添加到logger对象
                        logger.addHandler(sh)
                        logger.setLevel('DEBUG')                # 设定日志等级
                        return logger                           # 返回logger对象

         2. 记录日志:
           logging/logger.debug('debug message')
           logging/logger.info('info message')
           logging/logger.warning('warning message')
           logging/logger.error('error message')
           logging/logger.critical('critical message')
''' # logging模块: 开发日志, 运维中的错误信息
# import logging
# Config_file = {
#                'level':logging.DEBUG,
#                'format':'%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                'filename':'test_log2.log',
#                'filemode':'w',
#                'datefmt':'%Y-%m-%d'
#                }
# logging.basicConfig(**Config_file)
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')


# import logging
# def logger():
#     logger = logging.getLogger()
#     fh = logging.FileHandler('test_log')
#     sh = logging.StreamHandler()
#
#     fmt = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
#     fh.setFormatter(fmt)
#     sh.setFormatter(fmt)
#
#     logger.addHandler(fh)
#     logger.addHandler(sh)
#     logger.setLevel(logging.DEBUG)
#     return logger
#
# logger = logger()
# logger.debug('hello')
# logger.critical('critical')

'''
hashlib: 
        方法一: MD5, 一个md5对象只能编码一个字符串
               md5 = hashlib.md5()
               md5.update('str'.encode('utf8'))
               str_hash = md5.hexdigest()         # 返回摘要, 十六进制字符串
               byte_hash = md5.digest()           # 返回摘要, 二进制
        
        方法二: sha1, sha224, sha256, sha384, sha512
               sha = hashlib.sha256('key'.encode('utf8'))     # 生成时添加盐
               sha.update('str'.encode('utf8))                # 其余同md5
               
hmac: 
      方法一:     h = hmac.new(b'key')
                 h.update(b'msg')
      方法二:     h = hmac.new(b'key',b'msg')                            
                 str_encode = h.hexdigest()         # 返回摘要， 十六进制字符串
                 byte_hash = h.digest()             # 返回摘要， 二进制字符串
                 True/False = hmac.compare_digest(b'abc',b'123')    # 比较两个二进制字符串是否相同
''' # 加密算法: hashlib(md5,sha), hmac

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
    1. json: 序列化为字符串
             1）能json序列化的: 基本数据类型, list, tuple, dict
             2) 操作:
                    1> 序列化
                          data_json = json.dumps(data)                          # 直接序列化
                          with open('filename','w',encoding='utf8) as f:
                             json.dump(data,f)                                  # 序列化存入文本
                    2> 读取
                          data = json,loads(data_json)
                          with open('filename','r', encoding='utf8') as f:
                             data = json.load(f)         

    2. pickle: 序列化为二进制文件, 仅python能用
       1) 能序列化的类型: 基本数据类型, list, tuple, dict, set, obj
       2) 操作:
              1> 序列化
                    data_pickle = pickle.dumps(data)
                    with open('filename','wb') as f:
                         pickle.dump(data)
              2> 读取
                    data = pickle.loads(data_pickle)
                    with open('filename','rb') as f:
                         pickle.load(f)                                                                       
''' # json & pickle: 序列化

'''
xml: 操作xml文件 import xml.etree.ElementTree as ET
     1. 特点: 
             1) 基于节点对象操作
             2) 每一个节点有如下属性:
                 node.tag        # 'str' 节点名
                 node.attrib     # dict = {'attr':'value'} 节点属性值
                 node.text       # 'str' 节点值
     2. 操作:
            1) 生成xml文件
               father_node = ET.Element('father_node')                                      # 生成父节点
               child_node = ET.SubElement('father_node','child_node',attrib={'attr':value}) # 生成子节点
               child_node.text = 'str'
               et = ET.ElementTree(father_node)                                 # 生成document对象
               et.write('filename.xml',encoding='utf8',xml_declaration=True)    # 生成xml
                       
            2) 访问xml文件
                tree = ET.parse('filename.xml')                               # 获取document对象
                root = tree.getroot()                                         # 获取根节点
                1> 遍历
                      for child in root:            # child也是一个节点对象, 若要获取内部元素要继续遍历
                2> 搜索
                      node.findall('node_name')     # 在node的内部子节点中搜索所有node_name
                      node.find('node_name')        # 在node的内部子节点中搜索一个node_name
                      node.getchildren()            # 获取node的所有子节点     
                3> 重写
                      node.tag = new_tag   
                      node.attrib = {'attr':'attr_value'}
                      node.text = new_value
                      tree.write('filename.xml')    # 重新生成xml文件
                4>> 删除
                      node.remove(node obj)         # 删除子节点                                     
''' # xml模块

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
''' # configparser模块: 配置文件

'''
StringIO and ByteIO: StringIO 
                     1. f = io.StringIO(' ') <--> f.read(), f.readline(), for item in f:
                     2. f = io.StringIO()
                        f.write(' ')    <-->  f.getvalue()

                    BytesIO
                    1. f = io.BytesIO(b' ')   <--> f.read(), f.readline(), for item in f:
                    2. f = io.BytesIO()
                       f.write(b' ')  <--> f.getvalue()
''' # StringIO, ByteIO

# 下一章: ObjectOrientProgramming.py

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