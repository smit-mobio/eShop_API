from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from database.database import Base
from database.database import db
class Data:
    
    def add(object):
        db.add(object)
        db.commit()
        
    def delete(object):
        db.delete(object)
        db.commit()
        
    def commit():
        db.commit()
        
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    first_name = Column(String(50), nullable = True)
    last_name = Column(String(50), nullable = True)
    username = Column(String(50), nullable = False)
    email = Column(String(30), nullable = False, unique = True)
    password = Column(Text, nullable = False)
    is_active = Column(Boolean, default = True)
    phone = Column(String(10), nullable = True)
    profile_picture = Column(String(100), nullable = True)
    created_on = Column(DateTime, nullable = False)
    updated_on = Column(DateTime, nullable = True)
    

    

    
