from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,Integer,String


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
