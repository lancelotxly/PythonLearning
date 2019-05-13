import pymysql

config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'reviewer'
}
conn = pymysql.connect(**config)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = '''
select * from students
'''
rot = cursor.execute(sql)
data = cursor.fetchone()
print(data)
print(rot)