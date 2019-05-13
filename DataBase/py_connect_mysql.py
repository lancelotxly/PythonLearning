'''
1. 连接数据库
   config = {
      'host': '127.0.0.1',
      'port':3306,
      'user':'root',
      'password':'123456',
      'db':'test'
   } 
   conn = pymsql.connect(**config)

2. 创建游标
   cursor = conn.cursor()                           # 默认返回为tuple组成的tuple
   cursor = conn.cursor(pymsql.cursors.DictCursor)  # 返回dict组成的list

3. 执行sql语句
   row = cursor.execute('sql')                      #  最后一条数据的自增ID
   # 对于增删改必须要提交事务才能生效
   conn.commit()                                    
   # 对于查
   data = cursor.fetchall()   # 取所有
   data = cursor.fetchone()   # 取一个, 没有外部的数据结构包装
   data = cursor.fetchmany(3) # 接着上一次游标位置继续取三个

4. 结束关闭游标, 关闭连接
   cursor.close()
   conn.close() 

''' # pymsql操作步骤

import pymysql
'''
连接到已有的数据库
'''
config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'test'
}

conn = pymysql.connect(**config)

'''
操作基于cursor游标，基于事务，要提交事务才生效(insert delete update), 不能用with语句
'''
cursor = conn.cursor()  # 取数据返回tuple组成的tuple, 数据不可更改
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)   # 取数据返回dict组成的list, 数据可更改; 默认为tuple组成的tuple

sql = '''
CREATE TABLE IF NOT EXISTS py_table(
id int primary key,
name varchar
)
'''
row_affected = cursor.execute(sql)        # 执行后会返回游标位置
conn.commit()                             # 增删改需要提交(事务)才能生效

cursor.execute('select * from py_table')
data = cursor.fetchone()                  # 取一个
data = cursor.fetchmany(3)                # 接着取三个
data = cursor.fetchall()                  # 取完

cursor.scroll(-1,mode='relative')         # cursor游标向上移动一个，“+1” 为向下移动一个
cursor.scroll(1,mode='absolute')          # cursor游标移动到位置1

cursor.close()
conn.close()

