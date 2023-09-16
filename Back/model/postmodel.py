from sqlalchemy import Boolean, Column, Integer, String, Date

from database import Base

class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    project = Column(String)
    startDate = Column(Date)
    endDate = Column(Date)
    hoursPerDay = Column(Integer)
    status = Column(Boolean)
