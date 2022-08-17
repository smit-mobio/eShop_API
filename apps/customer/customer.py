from fastapi import APIRouter, Depends, Response
from apps.authentication.jwt_handler import get_current_active_user
from utils.decorators import only_customer
from database.dao import dao_handler
router = APIRouter(prefix='/auth/user/customer', tags=['Customer'], dependencies=[Depends(get_current_active_user)])

@router.get('/products/')
@only_customer()
def all_products(response:Response, user = Depends(get_current_active_user)):
    products = dao_handler.inventory_dao.get_active_product()
    print(products)
    return products