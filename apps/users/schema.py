from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    id:int
    username:str
    first_name:str
    last_name:str
    email:EmailStr
    password:str
    phone:str
    group:list 
    
    class Config:
        orm_mode = True
        
class UserCreateSchema(BaseModel):  
    first_name:str
    last_name:str
    email:EmailStr
    phone:str
    password:str
    group_id:int
    
    class Config:
        orm_mode = True
        
class UserActiveSchema(UserSchema):
    is_active:bool


        