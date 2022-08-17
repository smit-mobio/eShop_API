from fastapi import APIRouter, Depends, Response, status
from apps.authentication.jwt_handler import get_current_active_user
from utils.decorators import only_product_owner
from apps.users import schema
from utils import common_function

router = APIRouter(prefix='/auth/user/product_owner', tags=['Product-Owner'], dependencies=[Depends(get_current_active_user)])

@router.get('/profile/')
@only_product_owner()
def product_owner_profile(response:Response, user = Depends(get_current_active_user)):
    return user

@router.patch('/profile/edit/')
@only_product_owner()
def update_product_owner_profile(response:Response, data:schema.UserEditSchema ,user = Depends(get_current_active_user)):
    if common_function.update_profile(data, user):
        response.status_code = status.HTTP_200_OK
        return {'message':'Your profile is successfully updated!'}
    response.status_code = status.HTTP_400_BAD_REQUEST
    return {'error':'Phone number is not valid!'}