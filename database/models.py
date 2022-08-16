from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Table, Text, Float, func
from sqlalchemy_utils import ChoiceType
from database.database import Base, db


user_group = Table('user_group', Base.metadata,
                   Column('user_id', Integer, ForeignKey('users.id'), primary_key = True),
                   Column('group_id', Integer, ForeignKey('groups.id'), primary_key = True)
                   )


from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text

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
    group = relationship('Group', secondary = user_group)
    
class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False)
    created_on = Column(DateTime, nullable = False)
    updated_on = Column(DateTime, nullable = False)
    user = relationship("User", secondary = user_group)



class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    detail = Column(String(200), nullable = True)
    price = Column(Float, nullable = False)
    brand = Column(String(50), nullable = False)
    quantity = Column(Integer, nullable = True)
    image = Column(String(300), nullable = True)
    product_status = [
        ('Out of Stock', "Out of Stock"),
        ('Instock', 'Instock')
    ]
    status = Column(ChoiceType(product_status), nullable = False)
    product_category = [
        ('Man', "Man"),
        ('Women', 'Women'),
        ('Kids', "Kids")
    ]
    category = Column(ChoiceType(product_category), nullable = False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable = False)
    updated_by = Column(Integer, ForeignKey("users.id"), nullable = True)
    created_on = Column(DateTime, default = datetime.now())
    updated_on = Column(DateTime, default = datetime.now())    

    
class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key = True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable = False)
    product = relationship('Product', uselist = False, foreign_keys = [product_id])
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    created_by = relationship("User", foreign_keys = [created_by_id])
    created_on = Column(DateTime, default = datetime.now())
    updated_on = Column(DateTime, default = datetime.now())
    updated_on = Column(DateTime, default = datetime.now())
