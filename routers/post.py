from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import db_post
from database.database import get_db
from routers.schemas import PostBase

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)

@router.post('/')
def create(post: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, post)
    