from fastapi import APIRouter, Response, status
from apps.users import schema
from database.models import Data
from database import models
from utils import common_function
from database.dao import dao_handler
from werkzeug.security import generate_password_hash
from datetime import datetime

router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/', response_model=list[schema.UserSchema])
def get_all_users():
    all_users = dao_handler.user_dao.get_all()
    return all_users

@router.get('/info_user/{id}')
def get_user(id:int, response:Response):
    user = dao_handler.user_dao.get_by_id(id)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':'User you are looking for is not exists!'}
    return user

@router.post('/create_user/', description=f"Pass group_id in group field to select group.<br>{dao_handler.group_dao.get_group_with_id()}")
def create_user(user:schema.UserCreateSchema, response:Response):
    has_password = generate_password_hash(user.password, method="sha256")
    new_user = models.User(first_name = user.first_name, last_name = user.last_name, email=user.email, password = has_password, username = common_function.create_username(user.email), created_on = datetime.now(), phone = user.phone)
    if user.group_id not in [i.id for i in dao_handler.group_dao.get_all()]:
        response.status_code = status.HTTP_404_NOT_FOUND
        return  {'error':'Please enter a valid group_id'}
    get_group = dao_handler.group_dao.get_by_id(user.group_id)
    new_user.group = [get_group] 
    Data.add(new_user)
    new_user = dao_handler.user_dao.get_by_id(new_user.id)
    return {'new_user': new_user}


@router.patch('/update_user/{id}/')
def update_user(id:int, user:schema.UserSchema, response:Response):
    user_to_update = dao_handler.user_dao.get_by_id(id)
    if not user_to_update:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':'User you are looking for is not exists!'}
    user_to_update.first_name = user.first_name
    user_to_update.last_name = user.last_name
    user_to_update.phone = user.phone
    user_to_update.update_on = datetime.now()
    Data.commit()
    return {'message':'User profile is successfully updated!'}

@router.delete('/delete_user/{id}')
def delete_user(id:int, response:Response):
    user_to_delete = dao_handler.user_dao.get_by_id(id)
    if not user_to_delete:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':'User you are looking for is not exists!'}
    Data.delete(user_to_delete)
    response.status_code = status.HTTP_200_OK
    return {'success':'User is deleted successfully!'}