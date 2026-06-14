from sqlalchemy import Integer, String, Column, DateTime
from .database import Base

class DbPost(Base):
    __tablename__ = 'posts'
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    image_url = Column(String)
    created_at = Column(DateTime)
    created_by = Column(String)
    timestamp = Column(DateTime)