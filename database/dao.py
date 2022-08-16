from database.database import db
from database import models

class GenericDao:
    model = None
    
    def get_all(self):
        return db.query(self.model).all()
    
    def get_by_id(self, id):
        return db.query(self.model).filter_by(id=id).first()
    
    def get_by_ids(self, ids:list):
        return db.query(self.model).filter(self.model.id.in_(ids)).all()
    
class UserDao(GenericDao):
    model = models.User
    
    def get_by_email(self, email):
        return db.query(self.model).filter_by(email = email).first()
    
    
    
class GroupDao(GenericDao):
    model = models.Group
    
    def get_by_name(self, name):
        return db.query(self.model).filter_by(name = name).first()
    
    def get_group_with_id(self):
        groups = super().get_all()
        group_dict = {}
        for i in groups:group_dict.update({i.name:i.id}) 
        return group_dict

class ProductDao(GenericDao):

    model = models.Product

    def get_products_of_product_owner(self, product_onwer_id):
        return db.query(self.model).filter_by(created_by = product_onwer_id).all()

    def get_product_of_product_owner(self, product_onwer_id, product_id):
        return db.query(self.model).filter_by(created_by = product_onwer_id, id = product_id).first()

class DaoHandler:
    user_dao = UserDao()
    group_dao = GroupDao()
    product_dao = ProductDao()

dao_handler = DaoHandler()

