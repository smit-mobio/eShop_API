from msilib.schema import AppId
from fastapi import APIRouter, Depends
from apps.authentication.jwt_handler import get_current_active_user

router = APIRouter(prefix='/auth/user/customer', tags=['Customer'], dependencies=[Depends(get_current_active_user)])