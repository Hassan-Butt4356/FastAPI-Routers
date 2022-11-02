from pydantic import BaseModel
from typing import Optional
from fastapi import Body



class CreateItem(BaseModel):
    name:str
    price:int=Body(gt=499)
    description:str
    

    
class UpdateItem(BaseModel):
    name:Optional[str]=None
    description:Optional[str]=None
    price:Optional[int]=Body(None,gt=499)