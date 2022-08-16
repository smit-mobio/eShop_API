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
    