from pydantic import BaseModel
from apps.users.schema import UserSchema

class Token(BaseModel):
    access_token: str
    token_type: str

    
class TokenData(BaseModel):
    username:str 
    
class UserInDB(UserSchema):
    hashed_password: str