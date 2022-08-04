from pydantic import BaseModel

class GroupSchema(BaseModel):
    name:str
      
    class Config:
        orm_mode = True