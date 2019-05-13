'''
事务:
    1, 事务的特性
        1> 原子性, 不可分割，要么提交(发生)，要么不提交(不发生)
        2> 一致性,  事务前后数据的完整性必须保持一致。  所有记录都能保证满足当前数据库中的所有约束，则可以说当前的数据库是符合数据完整性约束
        3> 隔离性, 多并发事务之间数据相互隔离
        4> 持久性, 事务对数据的改变是永久的 

    2. mysql中的事务操作
        start transaction  // 开启一个事务
        rollback           // 事务回滚，回滚到上次提交之后
        commit             // 提交事务结束
        savepoint          // 设置回滚点
           insert into test2 (name)values('wu');
           savepoint insert_wu;
           ###...

           rollback to insert_wu;                // 返回到 insert into test2 (name)values('wu'); 执行之后 
    
    3. pymysql中的事务操作
       try:
           cursor.execute('sql')               // 可能出错的sql语句
           raise Exception
       except Exception:
           conn.rollback()                    // 数据库中回滚到上一次commit之后 
           conn.commit()                      // 回滚也要提交
''' # 事务


import pymysql

config = {
    'host':'127.0.0.1',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'test2'
}

conn = pymysql.connect(**config)

cursor = conn.cursor()

try:
    create_table_SQL = '''CREATE TABLE Account(name varchar, balance int)'''
    insertSQL0 = "INSERT INTO ACCOUNT (name,balance) VALUES ('oldboy',4000)"
    updateSQL1 = "UPDATE Account set balance=balance-30 WHERE name='yuan'"
    updateSQL2 = "UPDATE Account set balance=balance+30 WHERE name='xialv'"

    cursor.execute(create_table_SQL)
    cursor.execute(insertSQL0)
    conn.commit()

    cursor.execute(updateSQL1)
    raise Exception                  # 若执行出错，则抛出异常
    cursor.execute(updateSQL2)       # rollback回滚后, 取消上一次操作，执行该sql语句
    conn.commit()

except Exception as e:
    conn.rollback()                     # 回滚到上一次commit之后
    conn.commit()                       # rollback() 也需要提交到数据库
finally:
    cursor.close()
    conn.close()

