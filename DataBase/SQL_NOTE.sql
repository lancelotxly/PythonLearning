/*
1. 基本概念:
          表: 存放数据

          数据库: 存储表的仓库

          数据库管理软件(Database Management Software, DMS): 管理数据库的软件,如
                关系型数据库(基于关系表): sqlite, db2, oracle, sql server, mysql
                非关系型数据库(key-value存储数据, 没有表结构): redis, memcache, mongodb

          数据库服务器-：运行数据库管理软件

2. sql语法:  DDL (Data Definition Language) 针对数据库，表以及字段的操作
            DML  (Data Manipulation Language) 只是对表内部数据的操作，而不涉及到表的定义、结构的修改，更不会涉及到其他对象
*/

/*
DDL: CREATE, SHOW, ALTER, DROP, USE
     1. 数据库操作:
                 CREATE DATABASE [IF NOT EXISTS] database_name [CHARACTER SET GBK];  // 创建数据库

                 SHOW DATABASES;                                                    // 查看所有数据库
                 SHOW CREATE DATABASE database_name;                               // 查看创建过程

                 ALTER DATABASE database_name [CHARACTER SET UTF8];               // 修改数据库

                 DROP DATABASE [IF EXISTS] database_name;                         // 删库

                 USE database_name;                                              // 使用数据库
                 SELECT database();                                              // 查看当前使用的数据库

    2. 表操作: CREATE, ALTER+(ADD,MODIFY,CHANGE,DROP), DESC
            数据类型:
                    1>>.数值: TINYINT //1 BYTE, INT //4 BYTES, FLOAT //4 BYTES, DOUBLE //8 BYTES, DECIMAL(4,2) //总共四位, 一位小数
                             tips:  FLOAT(4,2)  // 34.56
                    2>>.时间: DATE //YYYY-MM-DD, TIME //HH:MM:SS, YEAR //YYYY, DATETIME //YYYY-MM-DD HH:MM:SS
                    3>>.字符串: CHAR(L), VARCHAR(L), TEXT, BLOB // 二进制

            1.>创建表:  CREATE TABLE [IF NOT EXIST] table_name (
                         field  type constraints,
                         ...
                       );
                       constraints:  PRIMARY KEY [AUTO_INCREMENT], UNIQUE, NOT NULL, DEFAULT
                                     PRIMARY KEY(field, field2,..) // 联合主键

           2.>查看表信息:    DESC table_name;                 // 查看表结构
                           SHOW CREATE TABLE table_name;    // 查看创建过程

           3.>修改表结构:  1>>. 增加列(字段):
                                    ALTER TABLE table_name
                                           ADD col_name type FIRST                 // 头插
                                           ADD col_name type AFTER col_1          // col_1之后插
                                           ADD col_name type;                     // 尾插
                                           ADD CONSTRAINT ..                      // 添加约束
                         2>>. 修改列(字段)类型，约束条件:
                                   ALTER TABLE table_name MODIFY col_name type constraints;
                         3>>. 修改列(字段)名:
                                   ALTER TABLE table_name CHANGE col_name new_name type;
                         4>>. 删除一列(字段):
                                   ALTER TABLE table_name DROP col_name;

          5.>删除表:      DROP TABLE table_name;

          *> 复制表结构和数据:  CREATE TABLE new_table select * from table_name
             复制表结构:       CREATE TABLE new_table select * from table where wrong_condition

          6>. 外键约束: 创建完charger_id后另起一行加FOREIGN KEY (charger_id) REFERENCES ClassCharger(id) ON 删除方式
               )ENGINE=INNODB;
              外键约束对子表的含义:   如果在父表中找不到候选键,则不允许在子表上进行insert/update
              外键约束对父表的含义:   父表进行DELETE时，取决与子表定义外键时指定的ON操作
                                  ON DELETE CASCADE;   // 父表删除，子表对应记录删除
                                  ON DELETE SET NULL;  // 父表删除，子表对应记录为NULL
 */

/*
DML: INSERT, UPDATE, DELETE, SELECT
     1. 增加记录:  INSERT INTO table_name (field1, field2,...) VALUES
                        (value1, value2,...),
                        (value1, value2,...);
                 * field 非必要的可缺省
                 * 全部添加，field整个可缺省
                 INSERT INTO table_name SET field1=value1,..;
    2. 修改记录:   UPDATE table_name SET field1=value1,...  WHERE;
    3. 删除记录:   DELETE FROM table_name WHERE;
                 TRUNCATE TABLE table_name;             // 建一个新表覆盖
    4. 查询(单表): SELECT [DISTINCT] * [field1,..] FROM table_name
                         WHERE 条件
                         GROUP BY field
                         HAVING 筛选
                         ORDER BY field [DESC/ASC][LIMIT start,row_count]
                 **SQL语句处理顺序: from -> where -> select -> group by -> having -> order by -> limit row1,row2. (row1,row2)
                                  select JS as JS成绩 from ExamResult where JS成绩 >70; ---- 不成功
                                  select JS as JS成绩 from ExamResult having JS成绩 >90; --- 成功

                1>. SELECT * FROM table_name;                       //查全部
                2>. SELECT field1,field2 FROM table_name;           //查部分
                3>. SELECT DISTINCT field1, field2 FROM table_name; //过滤field1,field2中重复部分
                4>. SELECT field1 AS new_name, field2表达式 FROM table_name;  // AS 重命名， field可用表达式(对null处理--->IFNULL(field,0))

                // 条件过滤
                5> SELECT * FROM table_name WHERE condition
                   condition:  1. 比较 >,<,>=,<=,!=,=
                               2. between 80 and 100;   // [80,100];
                               3. in (80,90,100);
                               4. like="yuan%", "yuan_"   // %多字符匹配,  _单字符匹配
                               5. field IS NULL;          // 数据为空
                               6. REGEXP 'dec'            // 正则匹配

                // 将找到的表记录排列
                6> SELECT * FROM table_name WHERE condition ORDER BY field [DESC/ASC]

                // 分组
                7>. SELECT field1 FROM table_name GROUP BY field1;      //  将表单按field分组(没有分组的表单相当于是按主键分组的)
                8>. SELECT field1 FROM table_name WHERE 条件 GROUP BY field1 HAVING 筛选 // WHERE 分组前筛选， HAVING 分组后筛选
                9>. // 聚合函数配合分组使用，对分组后的表记录进行处理(也可以直接用于表单，没有分组的表单相当于是按主键分组的)
                       COUNT(field2);  // 按field2统计分组有几项
                       SUM(field2);   // 按field2累和,处理null
                       AVG(field2);   // 求field2的平均，处理null
                       MAX(field2), MIN(field2); //最大最小，处理null



   5. 多表联查: 1>. 笛卡儿积: SELECT * FROM table_A, table_B;
              2>. 内连接: 两表联查相当于从笛卡尔积中筛选出正确的结果
                         SELECT * FROM table_A, table_B where table_A.id = table_B.id;
                         SELECT * FROM table_A INNER JOIN table_B ON table_A.id = table_B.id;
              3>. 左连接: 在内链接的基础上，以左边为主，增加右边没有的结果
                         SELECT * FROM table_A LEFT JOIN table_B ON table_A.id = table_B.id;
                  右连接: 与左连接相反
                         SELECT * FROM table_A RIGHT JOIN table_B ON table_A.id = table_B.id;
              4>. 全连接: 取左右连接的并集
                         SELECT * FROM table_A LEFT JOIN table_B ON table_A.id = table_B.id
                         UNION
                         SELECT * FORM table_A RIGHT JOIN table_B ON table_A.id = table_B.id;


             5>.  子查询:  SELECT * FROM table_A WHERE table_A.col_1 IN (SELECT table_B.col_1 FROM table_B);
                                                                    NOT IN
                                                                    EXISTS  内表为真时，外表开始查询，否则不查询

 */

/*
数据的三大范式和五大约束:
   1. 三大范式
      1) 保证每一列的原子性
      2) 表中的所有列都依赖于主键,即一张表只描述一件事
      3) 表中的每一列都和主键直接相关,不是间接相关, 即一张表只能有另一张表的主键,不能有其他信息(其他信息一律用该主键在另一只表中查询)

   2. 五大约束
      1） primary key
      2) unique
      3) default
      4) not null
      5) foreign key
*/

/*
Mysql:
    1. Mysql登录:
      -u username -p password                       // 本地登录
      -h server_ip -P port -u username -p password  // 远程登录

    2. Mysql服务器架构:
              API(C,JDBC,Python)
        --------------------------------
                    连接池
        --------------------------------
        SQL接口, SQL解析器, SQL优化器,缓存池
        --------------------------------
                可插入式存储引擎
                   各种数据库
        --------------------------------

    3. Mysql存储引擎: 如何增删查改数据, 建立表
       InnoDB: 支持事务, 支持B-tree, 不支持Hash
       MyISAM: 不支持事务, 支持B-tree, 不支持Hash
       Memory: 存储的数据都放在内存中, 支持B-tree和Hash

 */

/*
视图:
    1. 特性:
       1) 是一张虚拟的表, 其本质是sql语句获得的动态数据集
       2) 可以直接当成表来用, 视图也是存储在数据库中的
       3) 过分依赖视图会造成程序强耦合

    2. 操作
       1) create view 视图名称 as sql查询语句   // 创建视图
       2) alter view 视图名称 as sql查询语句    // 修改视图
       3) 使用视图同使用表(修改视图会导致原表修改)
       4) drop view 视图名称                  // 删除视图
 */

/*
触发器:
     1. 作用:
        可以定制用户对表增、删、改操作前后的行为
     2. 用法:
        1) 创建触发器
        delimiter//
        CREATE TRIGGER 触发器名称 BEFORE/AFTER INSERT/DELETE/UPDATE ON 表名称 FOR EACH ROW
        BEGIN
              NEW  # 表示即将新增的行, 可通过NEW.field访问属性
              OLD  # 表示即将删除的行
              # 函数 + sql语句
        END//
        delimiter;

        2) 删除触发器
        DROP TRIGGER 触发器名称
*/

/*
事务:
    1. 事务的特性
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
 */

/*
存储过程:
   1. 程序与数据库结合使用的方式:
      1) mysql: 存储过程 + 程序: 调用存储过程
         优点:
              #1 传输数据量小
              #2 实现程序逻辑与sql语句的解耦
         缺点: 扩展不方便

      2) mysql: 存储数据 + 程序: sql语句

   2. 无参存储过程
      1) 创建
         delimiter//
         CREATE PROCEDURE func()
         BEGIN
              # sql语句
         END//
         delimiter;
      2) 调用
         CALL func();                   # mysql中调用
         cursor.callproc('func')        # pymysql中调用

   3. 有参存储过程
      1) 仅用于传入参数: in
          delimiter //
          create procedure p2(
              in n1 int,
              in n2 int
          )
          BEGIN
              select * from blog where id > n1;
          END //
          delimiter ;

          #在mysql中调用
          call p2(3,2)

          #在python中基于pymysql调用
          cursor.callproc('p2',(3,2))
          print(cursor.fetchall())

     2) 仅用于返回参数: out
        delimiter //
        create procedure p3(
            in n1 int,
            out res int
        )
        BEGIN
            select * from blog where id > n1;
            set res = 1;
        END //
        delimiter ;

        #在mysql中调用
        set @res=0;                   # 设置初始值
        call p3(3,@res);
        select @res;                  # 获取返回参数

        #在python中基于pymysql调用
        cursor.callproc('p3',(3,0))     #0相当于set @res=0
        print(cursor.fetchall())

        cursor.execute('select @_p3_0,@_p3_1;') # 获取返回参数
        print(cursor.fetchall())

     3) 用于传入传出的参数: inout
        delimiter //
        create procedure p4(
            inout n1 int
        )
        BEGIN
            select * from blog where id > n1;
            set n1 = 1;
        END //
        delimiter ;

        #在mysql中调用
        set @x=3;
        call p4(@x);
        select @x;

        #在python中基于pymysql调用
        cursor.callproc('p4',(3,))
        print(cursor.fetchall())

        cursor.execute('select @_p4_0;')    # 获取返回值
        print(cursor.fetchall())

  3. 删除存储过程
     DROP PROCEDURE proc_name;
 */

/*
函数:
    1. 常见内置函数
       聚合函数:  AVG, COUNT, MIN, MAX, SUM
       日期格式转化函数: DATE_FORMAT(datetime, '%Y %m %d %H %M %S %X %a')
       控制流函数:
                CASE WHEN test THEN t ELSE f END  # 如果test为真,执行t,否则执行f
                IF (test,t,f)                     # 如果test为真,返回t,否则返回f
                IFNULL(arg1,arg2)                 # 如果arg1不为NULL返回arg1, 否则返回arg2
                NULLIF(arg1,arg2)                 # 如果arg1==arg2返回NULL, 否则返回arg1
    2. 定义函数
       delimiter //
       create function f1(
           i1 int,              // 函数初始化
           i2 int2
       )
       returns int             //  返回类型
       BEGIN                   // BEGIN..END不要写sql语言, 否则为存储过程
           declare num int;    // 声明变量 变量名 类型
           set num = i1 + i2;  // 赋值
           return (num)        // 返回
      END//
      delimiter;

    3. 调用函数
       select f1(11,nid) ,name from tb2;

    4. 删除函数
       DROP FUNCTION func_name;

    5. 流程控制
       1) IF... THEN
          ELSEIF.. THEN
          ELSE..
          END IF

       2) WHILE..DO
          END WHILE

       3) REPEAT
             ...
             UNTIL ..
          END REPEAT
 */

/*
索引:
     1. 索引的数据结构: B+树
        二分查找 + 平衡二叉树

     2. 索引的最左匹配原则: 按照从左到右的顺序建立搜索树
        (name,age,sex) 先比较name, 如果name相同则继续比较age和sex, 直到得到数据
        (age,sex)      不会按照最左匹配原则
        (name,sex)     找到name, 然后获得该name的所有age值, 再匹配sex

     3. 聚集索引和辅助索引
        聚集索引: 按照每张表的主键来构造搜索树, 每张表只有一个聚集索引
                优点: 它对主键的排序查找和范围查找速度非常快
                     范围查询（range query）
        辅助索引: 非聚集索引, 辅助索引的叶子节点不包含行记录的全部数据
                每张表上可以有多个辅助索引, 但只能有一个聚集索引

     4. 常用的索引
        1>>. 普通索引: 加速查询  INDEX (charger_id);
        2>>. 唯一索引:
                    主键索引: 加速查找 + 约束(不能为空, 不能重复)
                            PRIMARY KEY
                    唯一索引: 加速查找 + 约束(不能重复)
                            UNIQUE INDEX (charger_id);

        3>>. 组合索引:    INDEX(id, name, age);        // 效率比唯一索引低


     5. 索引未命中:
        1) like '%xx'
        2) 定位条件使用函数
        3） or: 从左到右依次执行
        4) 定位条件与创建索引的类型不一样
        5) !=, 定位范围过大
        6) >
        7) order by 选择的映射如果不是索引，则不走索引
        8) 组合索引最左前缀失效

    6. 覆盖索引:
        即从辅助索引中就可以得到查询记录，而不需要查询聚集索引中的记录。 辅助索引大小远小于聚集索引, 因此可以减少大量的IO操作


                  索引设计原则:
                       1. 最适合的索引列, 出现在WHERE中和连接句子中的列
                       2. 使用唯一索引，索引列的基数越大，索引效果越好，因此往往用unique列做索引
                       3. 使用短索引，尽量缩短index(col(length))的length
                       4. 使用组合索引
    7. 索引合并:
       索引合并，让一条sql可以使用多个索引。对这些索引取交集，并集，或者先取交集再取并集。
       从而减少从数据表中取数据的次数，提高查询效率
 */

/*
数据库的优化方案:
    1. 创建数据表时把固定长度的放在前面
    2. 将固定数据放入内存： 例如：choice字段
    3. 联合索引遵循最左前缀(从最左侧开始检索)
    4. 避免使用 select *
    5. 读写分离:利用数据库的主从进行分离：主，用于删除、修改更新；从，用于查
    6. 分库: 当数据库中的表太多，将某些表分到不同的数据库
    7. 分表:
           水平分表：将某些列拆分到另外一张表，例如：博客+博客详情
           垂直分表：讲些历史信息分到另外一张表中，例如：支付宝账单
    8. 加缓存: 利用redis、memcache （常用数据放到缓存里，提高取数据速度）
*/




