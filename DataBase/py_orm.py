'''
SQLAlchemy:
           1. 架构和流程
           2. 建表
           3. 操作
''' # 综述

'''
SQLAlchemy架构和操作流程:
   1. 架构
                ORM(Object Relational Mapper)
      ----------------------------------------------------------
      Schema/Types, SQL Language, Engine(Connection Pool,Dialect)
      ----------------------------------------------------------
               DBAPI (pymysql,mysqldb,mysqlconnector)
   2. 流程
      #1 通过ORM提交命令
      #2 翻译成SQL语句
      #3 调用ENGINE执行
         #3.1 获得连接
         #3.2 调用指定的DBAPI去执行SQL语句 ---> SQLAlchemy可执行纯的SQL语句: engine.execute('sql')            
''' # SQLAlchemy架构和操作流程

'''
建表:
    1. 创建模板
       from sqlalchemy.ext.declarative import declarative_base
       Base = declarative_base()
    
    2. 继承模板创建表
       Class myTable(Base)
       from sqlalchemy import Column
       数据格式有: Integer, Float, DECIMAL, String, Boolean, Date, DateTime
       表名: __tablename__ = ''
       约束有: ForeignKey(ondelete='CASCADE'), ForeignKeyConstraint(), PrimaryKeyConstraint, UniqueConstraint(), Index()
       额外约束: __table_args__ = ()  除了ForeignKey()之外
    
    3. 创建连接engine
       from sqlalchemy import create_engine
       engine = create_engine(mysql + pymysql:// username:password@host:port/dbname)
    
    4. 调用engine建库
       Base.metadata.create_all(engine)
       #  删库
       Base.metadata.drop_all(engine)      
''' # 建表
from sqlalchemy.ext.declarative import declarative_base       # 创建模板的函数
from sqlalchemy import Column,Integer,String,DATETIME         # 数据类型
from sqlalchemy import ForeignKey,UniqueConstraint,Index
from sqlalchemy import create_engine                          # 创建引擎的函数

Base = declarative_base()       # 1. 创建模板

# 创建单表                        # 2. 继承模板创建表
class Business(Base):
    __tablename__ = 'business'
    id = Column(Integer, primary_key=True,autoincrement=True)
    bname = Column(String(32),nullable=False,index=True)

# 创建多对一
class Service(Base):
    __tablename__ = 'service'
    id = Column(Integer,primary_key=True,autoincrement=True)
    sname = Column(String(32),nullable=False,index=True)
    ip = Column(String(15),nullable=False)
    port = Column(Integer,nullable=False)

    business_id = Column(Integer,ForeignKey('business.id'))  # 外键约束: 多对一

    __table_args = (                                  # 其他约束
        UniqueConstraint(ip,port,name='uix_ip_port'),
        Index('ix_id_sname',id,sname)
    )

# 创建一对一
class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer,primary_key=True,autoincrement=True)
    rname = Column(String(32),nullable=False,index=True)
    priv = Column(String(64),nullable=False)

    business_id = Column(Integer,ForeignKey('business.id'),unique=True) # 外键约束: 一对一

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    uname = Column(String(32),nullable=ForeignKey,index=True)

class User2Role(Base):
    __tablename__ = 'user2role'
    id = Column(Integer,primary_key=True,autoincrement=True)
    uid = Column(Integer,ForeignKey('user.id'))
    rid = Column(Integer,ForeignKey('role.id'))
    __table_args = (
        UniqueConstraint(uid,rid,name='uix_uid_rid')
    )

engine =  create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test2',max_overflow=5)

def init_db():
    Base.metadata.create_all(engine)

def drop_db():
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    init_db()

'''
操作:  
    1. 创建session
       from sqlalchemy.orm import sessionmaker
       Session = sessionmaker(bind=engine)
       session = Session()
    
    2. 增加
       row_obj = myTable(field=var)
       session.add(row_obj)
       session.add_all([
           myTable(field=var1),
           myTable(field=var2)
       ])
       session.commit()                    # 基于事务, 增删改必须提交
    
    3. 删除
       session.query(Dep).filter(Dep.id>3).delete()
       session.commit()
    
    4. 修改
       session.query(Dep).filter(Dep.id > 0).update({'dname':'哇哈哈'})     # 修改传入一个dict
       session.commit()
              
    
    5. 查询: 单表
        res = session.query(Dep).all()   # 返回List, 每项为obj
        print(res[1].dname)              # obj.attr 获得值
        
        from sqlalchemy import distinct
        res = session.query(distinct(Dep.dname)).all()   # distinct 去重
    
        res = session.query(Dep.id,Dep.dname).all()  # 查询指定field, 返回list,每项为tuple
        print(res)
    
        sql = session.query(Dep).filter(Dep.id >1, Dep.id<1000)  # 条件查询, 返回sql语句对象
        print(sql.all())                                         # 返回List, 每项为obj
    
        sql = session.query(Emp).filter_by(ename='林海峰')        # 条件查询只能传等于条件, 返回sql语句对象
        print(sql.first().ename)
    
        res = session.query(Emp).filter(Emp.id.between(1, 3)).all() # .bewteen(a,b)
        print(res)
    
        res = session.query(Emp).filter(Emp.id.in_([1, 3, 99, 101])).all() # .in_([1,2,3])
        print(res)
    
        res = session.query(Emp).filter(~Emp.id.in_([1, 3, 99, 101]))  # not
        print(res)
    
        from sqlalchemy import and_, or_
        res = session.query(Emp).filter(and_(Emp.id > 0, Emp.ename == '林海峰')).all()  # and
        res=session.query(Emp).filter(or_(Emp.id < 2,Emp.ename=='功夫熊猫')).all()      # or
    
        res = session.query(Emp).filter(Emp.ename.like('%海_%')).all()   # like('%_')
    
        res = session.query(Emp)[0:5:2]   # limit [start:end:step]
    
        res = session.query(Emp).order_by(Emp.dep_id.desc(), Emp.id.asc()).all() # order_by(.desc(),.asc())
    
        from sqlalchemy.sql import func
        res = session.query(
            func.max(Emp.dep_id),                    # 聚合函数
            func.min(Emp.dep_id),
            func.sum(Emp.dep_id),
            func.avg(Emp.dep_id),
            func.count(Emp.dep_id),
        ).group_by(Emp.dep_id).all()                 # group_by()      
''' # 操作: 增删改, 单表查询

'''
多表查询:
   连接查询: 
       1. 内连接: 默认内连接, 自动关联foreign_key
          res=session.query(Emp.id,Emp.ename,Emp.dep_id,Dep.dname).join(Dep).all()
       
       2. 左连接: isouter = True
          res=session.query(Emp.id,Emp.ename,Emp.dep_id,Dep.dname).join(Dep,isouter=True).all()
       
       3. 右连接:同左连接,只是把两个表的位置换一下
   
   子查询:
       1. 子查询当做一张表, subquery()
           # select * from (select * from emp where id > 2);
           
           res = session.query(
              session.query(Emp).filter(Emp.id>8).subquery()
           ).all()                                                    
       
       2. 子查询当做范围使用
          # select ename from emp where dep_id in (select id from dep where dname='销售');
          
          res = session.query(Emp.ename).filter(Emp.dep_id.in_(
              session.query(Dep.id).filter_by(dname='销售')
          )).all()
       
       3. 子查询当做select后的字段, as_scalar()
          # select ename as 员工姓名,(select dname from dep where id = emp.dep_id) as 部门名 from emp;
          
          sub_sql = session.query(Dep.name).filter(Dep.id==Emp.dep_id)
          res = session.query(Emp.ename,sub_sql.as_scalar()).all()  
   
   正反查询: 在含有外键的表中创建,relationship对象
      depart = relationship('Dep',backref='xxoo')    # 'Dep'为类名不是表名, depart(用于正向查询), xxoo(用于反向查询) 且都不会创建字段
      # 正向查
      res = session.query(Emp).first()
      res.depart.dename                     # 获得'一表'中的值
      
      # 反向查
      res = session.query(Dep).first()
      res.xxoo                             # 返回一个List, 包含'多表'中关联的对象
''' # 操作: 多表查询
