from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    username:str
    first_name:str
    last_name:str
    email:EmailStr
    password:str
    phone:str
    
    class Config:
        orm_mode = True
        

        