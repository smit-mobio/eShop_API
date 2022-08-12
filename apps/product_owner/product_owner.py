from datetime import datetime
from fastapi import APIRouter, Depends, Response, status, Request
from apps.authentication.auth import get_current_active_user
from apps.users.schema import UserActiveSchema
from apps.product_owner.schema import AddProductSchema, ProductSchema
from database.models import Data, User, Product
from database.dao import dao_handler
from utils.decorators import only_product_owner

router = APIRouter(prefix='/auth/user/product_owner', tags=['Product-Owner'], dependencies=[Depends(get_current_active_user)])

@router.post('/add_product/', description="add category_id into category field. <br>Id : Category <br>---------------- <br>1 : Man <br>2 : Women <br>3 : Kids")
@only_product_owner
def add_product(form:AddProductSchema,response:Response,user:User = Depends(get_current_active_user)):
    if form.category not in [1,2,3]:
        response.status_code = status.HTTP_400_BAD_REQUEST
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

@router.get('/products/')
@only_product_owner
def get_all_product(response:Response, user=Depends(get_current_active_user)):
    products = dao_handler.product_dao.get_products_of_product_owner(user.id)
    return products

@router.get('/products/{id}')
# @only_product_owner
def get_product(id, response:Response, user=Depends(get_current_active_user)):
    products = dao_handler.product_dao.get_product_of_product_owner(user.id, id)
    if products:
        return products
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error':'Product you are looking for is not exists!'}

    
@router.delete('/remove_product/{id}')
# @only_product_owner
def remove_product(id:int, response:Response,  user:User = Depends(get_current_active_user) ):
    product = dao_handler.product_dao.get_by_id(id)
    if product:
        Data.delete(product)
        return {'message': 'Your product is successfully removed!'}
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error':"Product you want to remove is not exists!"}

@router.patch('/edit_product/{id}', description="Add category_id into category field. <br>Id : Category <br>---------------- <br>1 : Man <br>2 : Women <br>3 : Kids")
def update_product(id, form:AddProductSchema, response:Response, user:User = Depends(get_current_active_user)):
    product = dao_handler.product_dao.get_by_id(id)
    if product:
        product.name = form.type
        product.detail = form.detail
        product.brand = form.brand
        product.price = form.price
        product.quantity = form.quantity
        product_status = "Instock" if form.quantity > 0 else "Out of Stock"
        product.status = product_status
        if form.category not in [1, 2, 3]:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {'error':'Please enter a valid category_id!'}
        category = {
            1:'Man',
            2:'Women',
            3:'Kids'
        }
        product.category = category[form.category]
        product.updated_by = user.id
        product.updated_on = datetime.now()
        Data.commit()
        return {'message':'Your product is successfully updated'}
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error':'Product you are looking for is not exitst.'}

