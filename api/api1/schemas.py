from pydantic import BaseModel
from typing import Optional

class CreateUser(BaseModel):
    name:str
    email:str
    age:int
    
class UpdateUser(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None
    age:Optional[int]=None