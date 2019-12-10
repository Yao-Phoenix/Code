#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Date, Boolean

engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlou?charset=utf8')
Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    description = Column(String(1024))
    type = Column(String(64), index=True)
    students = Column(Integer)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    # 用户类型有普通用户和会员用户两种, 我们用布尔值字段来存储
    # 如果是会员用户, 该字段的值为 True, 否则为 False
    # 这里需要设置字段的默认值为 False
    is_vip = Column(Boolean, default=False)
    status = Column(String(64), index=True)
    school_job = Column(Integer, index=True)
    level = Column(Integer, index=True)
    join_date = Column(Date)
    learn_courses_num = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
