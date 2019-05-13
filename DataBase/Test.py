from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

egine=create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/test2',max_overflow=5)

Base=declarative_base()

class Dep(Base):
    __tablename__='dep'
    id=Column(Integer,primary_key=True,autoincrement=True)
    dname=Column(String(64),nullable=False,index=True)

class Emp(Base):
    __tablename__='emp'
    id=Column(Integer,primary_key=True,autoincrement=True)
    ename=Column(String(32),nullable=False,index=True)
    dep_id=Column(Integer,ForeignKey('dep.id'))

    #在ForeignKey所在的类内添加relationship的字段,注意:
    #1:Dep是类名
    #2:depart字段不会再数据库表中生成字段
    #3:depart用于Emp表查询Dep表(正向查询),而xxoo用于Dep表查询Emp表(反向查询),
    depart=relationship('Dep',backref='xxoo')

def init_db():
    Base.metadata.create_all(egine)

def drop_db():
    Base.metadata.drop_all(egine)

Session=sessionmaker(bind=egine)
session=Session()

if __name__ == '__main__':
    # res = session.query(Emp)
    # for row in res:
    #     print(row.ename, row.id, row.depart.dname)

    res = session.query(Dep).first()
    print(res.xxoo)