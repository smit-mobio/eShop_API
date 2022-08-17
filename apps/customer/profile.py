from fastapi import APIRouter, Depends, Response
from apps.authentication.jwt_handler import get_current_active_user

router = APIRouter(prefix='/auth/user/customer', tags=['Customer'], dependencies=Depends(get_current_active_user))

@router.get('/profile/')

def customer_profile(response:Response ,user = Depends(get_current_active_user)):
    return user