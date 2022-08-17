from pydantic import BaseModel  

class ProductAddSchema(BaseModel):
    type:str
    detail:str
    brand:str
    price:float
    quantity:int
    category:int

class ProductSchema(ProductAddSchema):
    id:int
    category:str
    
class ProductUpdateSchema(BaseModel):
    type:str
    detail:str
    brand:str
    price:float
    quantity:int
    is_active:bool