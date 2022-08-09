from fastapi import APIRouter, Depends
from apps.authentication.auth import get_current_active_user
from database.models import User

router = APIRouter(prefix='/auth/user/product_owner', tags=['Product-Owner'], dependencies=[Depends(get_current_active_user)])
