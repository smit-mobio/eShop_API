from fastapi import APIRouter, Depends, Response, status
from apps.authentication.jwt_handler import get_current_active_user
from utils.decorators import only_customer
from utils import common_function
from apps.users.schema import UserEditSchema

router = APIRouter(prefix='/auth/user/customer', tags=['Customer'], dependencies=[Depends(get_current_active_user)])

@router.get('/profile/')
@only_customer()
def customer_profile(response:Response ,user = Depends(get_current_active_user)):
    return user

@router.patch("/profile/update")
@only_customer()
def edit_profile(response:Response,data:UserEditSchema ,user = Depends(get_current_active_user)):
    if not common_function.update_profile(data=data, user=user):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'error':'Phone number is not valid!'}
    response.status_code = status.HTTP_200_OK
    return {'message':'Your profile is successfully updated!'}

