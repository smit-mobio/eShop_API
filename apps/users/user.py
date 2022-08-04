from fastapi import APIRouter, Response, status
from database.database import db
import apps.users.schema as schema
import database.models as models
from werkzeug.security import generate_password_hash
from datetime import datetime

router = APIRouter(prefix='/users', tags=['Users'])

@router.get('/', response_model=list[schema.UserSchema])
def get_all_users():
    all_users = db.query(models.User).all()
    return all_users

@router.get('/info_user/{id}')
def get_user(id:int):
    user = db.query(models.User).filter_by(id=id).first()
    if not user:
        return {'error':'User you are looking for is not exists!'}
    return user

@router.post('/create_user/')
def create_user(user:schema.UserSchema):
    has_password = generate_password_hash(user.password, method="sha256")
    new_user = models.User(first_name = user.first_name, last_name = user.last_name, email=user.email, password = has_password, username = common_function.create_username(user.email), created_on = datetime.now(), phone = user.phone)
    db.add(new_user)
    db.commit()
    new_user = db.query(models.User).filter_by(username = new_user.username).first()
    return {'new_user': new_user}


@router.patch('/update_user/{id}/')
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

@router.delete('/delete_user/{id}')
def delete_user(id:int, response:Response):
    user_to_delete = db.query(models.User).filter_by(id=id).first()
    if not user_to_delete:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':'User you are looking for is not exists!'}
    db.delete(user_to_delete)
    db.commit()
    response.status_code = status.HTTP_200_OK
    return {'success':'User is deleted successfully!'}