from datetime import datetime
from fastapi import FastAPI, status
import uvicorn
import schema
import models
from werkzeug.security import generate_password_hash
from fastapi.security import OAuth2AuthorizationCodeBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext

from utils import common_function
from database import db

SECRET_KEY = "a8f61fbb213a33775e551aedd4269cf79d68ce93"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
app = FastAPI()

@app.get('/')
def index():
    return {'message':'Hello World!'}

@app.get('/users/', response_model=list[schema.UserSchema])
def get_all_users():
    all_users = db.query(models.User).all()
    return all_users



@app.post('/users/')
def create_user(user:schema.UserSchema):
    has_password = generate_password_hash(user.password, method="sha256")
    new_user = models.User(first_name = user.first_name, last_name = user.last_name, email=user.email, password = has_password, username = common_function.create_username(user.email), created_on = datetime.now(), phone = user.phone)
    db.add(new_user)
    db.commit()
    new_user = db.query(models.User).filter_by(username = new_user.username).first()
    return {'new_user': new_user}


@app.patch('/users/{id}/')
def update_user(id:int, user:schema.UserSchema):
    user_to_update = db.query(models.User).filter_by(id = id).first()
    if not user_to_update:
        return {'error':'User you are looking for is not exists!'}
    user_to_update.first_name = user.first_name
    user_to_update.last_name = user.last_name
    user_to_update.phone = user.phone
    user_to_update.update_on = datetime.now()
    db.commit()
    return {'message':'User profile is successfully updated!'}

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=8000, reload= True)