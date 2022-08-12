from fastapi import APIRouter, Depends, Response, status
from apps.authentication.auth import get_current_active_user
from apps.users.schema import UserActiveSchema
from apps.product_owner.schema import AddProductSchema
from database.models import Data, User, Product

router = APIRouter(prefix='/auth/user/product_owner', tags=['Product-Owner'], dependencies=[Depends(get_current_active_user)])

@router.post('/add_product/', description="add category_id into category field. <br>Id : Category <br>---------------- <br>1 : Man <br>2 : Women <br>3 : Kids")
def add_product(form:AddProductSchema,response:Response,user:User = Depends(get_current_active_user)):
    if form.category not in [1,2,3]:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error':'Please enter a valid category_id.'}
    product_status = "Instock" if form.quantity > 0 else "Out of Stock"  
    category = {
        1:'Man',
        2:'Women',
        3:'Kids'
    }
    product = Product(name = form.type, detail = form.detail,price = form.price,  brand = form.brand, quantity = form.quantity, status = product_status, category = category[form.category], created_by = user.id, updated_by = user.id)
    Data.add(product)
    return {'message':"Your product is successfully added."}