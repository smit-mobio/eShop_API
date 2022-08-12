from pydantic import BaseModel  

class AddProductSchema(BaseModel):
    type:str
    detail:str
    brand:str
    price:float
    quantity:int
    category:int

class ProductSchema(AddProductSchema):
    id:int
    category:str
    