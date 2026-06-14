
from datetime import datetime
from pydantic import BaseModel

class PostBase(BaseModel):
    title : str
    content : str
    image_url : str
    created_by : str

class PostDisplay(PostBase):
    id : int
    title : str
    content : str
    image_url : str
    created_at : datetime
    created_by : str
    timestamp : datetime

    class Config:
        orm_mode = True