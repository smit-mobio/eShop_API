from unicodedata import name
from fastapi import APIRouter, Response, status
import apps.group.schema as schema
import database.models as models
from database.models import Data
from database.dao import dao_handler
from datetime import datetime

router = APIRouter(prefix='/groups', tags=['User-Groups'])

@router.get('/', response_model=list[schema.GroupWithId])
def get_all_groups():
    all_groups = dao_handler.group_dao.get_all()
    return all_groups

@router.get('/info_group/{id}')
def get_group(id:int, response:Response):
    group = dao_handler.group_dao.get_by_id(id)
    if not group:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message':'Group you are looking for is not exists!'}
    return group

@router.post('/create_group/')
def create_group(group:schema.GroupSchema, response:Response ):
    if dao_handler.group_dao.get_by_name(group.name):
        response.status_code = status.HTTP_409_CONFLICT
        return {'message':f"'{group.name}' group  is already exists!"}
    new_group = models.Group(name = group.name, created_on = datetime.now(), updated_on = datetime.now())
    Data.add(new_group)
    response.status_code = status.HTTP_201_CREATED
    return {'message':f"New '{new_group.name}' group is created successfully!"}

@router.patch('/update_group/{id}')
def update_group(id:int, group:schema.GroupSchema, response:Response):
    group_to_update = dao_handler.group_dao.get_by_id(id)
    if not group_to_update:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message':'Group you are looking for is not exists!'} , 404
    group_to_update.name = group.name
    group_to_update.updated_on = datetime.now()
    Data.commit()
    return group_to_update