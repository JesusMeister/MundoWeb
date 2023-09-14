from pydantic import BaseModel
from datetime import date

class Post(BaseModel):
    title:str
    content:str
    project:str
    startDate:date
    endDate:date
    hoursPerDay:int
    status:bool = False