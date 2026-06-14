from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import db_get
from database.database import get_db

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)

@router.get('/')
def get_all_posts(db: Session = Depends(get_db)):
    return db_get.get_all_posts(db)
    