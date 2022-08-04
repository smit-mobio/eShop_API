from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table, Text
from database import Base


user_group = Table('user_group', Base.metadata,
                   Column('user_id', Integer, ForeignKey('users.id'), primary_key = True),
                   Column('group_id', Integer, ForeignKey('groups.id'), primary_key = True)
                   )


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    first_name = Column(String(50), nullable = True)
    last_name = Column(String(50), nullable = True)
    username = Column(String(50), nullable = False)
    email = Column(String(30), nullable = False)
    password = Column(Text, nullable = False)
    is_active = Column(Boolean, default = True)
    phone = Column(String(10), nullable = True)
    profile_picture = Column(String(100), nullable = True)
    created_on = Column(DateTime, nullable = False)
    updated_on = Column(DateTime, nullable = True)
    group = relationship('Group', secondary = user_group)
    
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    user = relationship("User", secondary = user_group)


    

    
