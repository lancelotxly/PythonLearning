/*
1. 基本概念:
          数据库: 存储数据的仓库
          数据库管理软件(Database Management Software, DMS): 内部包含多个数据库，数据库中又有多个表(class)，表的各项(实例对象)存储了数据
                                                          oracle, db2, mysql
          mysql: -u username -p password   // 本地登录
                 -h server_ip -P port -u username -p password  // 远程登录

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
                         2>>. 修改列(字段)类型，约束条件:
                                   ALTER TABLE table_name MODIFY col_name type constraints;
                         3>>. 修改列(字段)名:
                                   ALTER TABLE table_name CHANGE col_name new_name type;
                         4>>. 删除一列(字段):
                                   ALTER TABLE table_name DROP col_name;
          5.>删除表:      DROP TABLE table_name;


          6>. 外键约束: 创建完charger_id后另起一行加FOREIGN KEY (charger_id) REFERENCES ClassCharger(id) ON 删除方式
               )ENGINE=INNODB;
              外键约束对子表的含义:   如果在父表中找不到候选键,则不允许在子表上进行insert/update
              外键约束对父表的含义:   父表进行DELETE时，取决与子表定义外键时指定的ON操作
                                  ON DELETE CASCADE;   // 父表删除，子表对应记录删除
                                  ON DELETE SET NULL;  // 父表删除，子表对应记录为NULL

          7>. 索引:
                  1>>. 普通索引(默认主键索引):  INDEX (charger_id);
                  2>>. 唯一索引:    UNIQUE INDEX (charger_id);
                  3>>. 组合索引:    INDEX(id, name, age);        // 效率比唯一索引低
                  索引设计原则:
                       1. 最适合的索引列, 出现在WHERE中和连接句子中的列
                       2. 使用唯一索引，索引列的基数越大，索引效果越好，因此往往用unique列做索引
                       3. 使用短索引，尽量缩短index(col(length))的length
                       4. 使用组合索引


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


