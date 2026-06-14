from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import db_delete
from database.database import get_db
from routers.schemas import PostBase

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)

@router.delete('/{post_id}')
def delete_post(post_id: int, db: Session = Depends(get_db)):
    deleted_post = db_delete.delete_post(db, post_id)
    if not deleted_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully", "post": deleted_post}