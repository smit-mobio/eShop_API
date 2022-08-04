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
    
    
class DaoHandler:
    user_dao = UserDao()
    
dao_handler = DaoHandler()
