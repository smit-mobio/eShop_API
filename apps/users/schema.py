from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    id:int
    username:str
    first_name:str
    last_name:str
    email:EmailStr
    password:str
    phone:str
    
    class Config:
        orm_mode = True
        

        