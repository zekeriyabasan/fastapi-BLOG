import datetime

from sqlalchemy.orm import Session
from database.models import DbPost
from routers.schemas import PostBase


def create(db: Session, post: PostBase):
    db_post = DbPost(
        title=post.title,
        content=post.content,
        image_url=post.image_url,
        created_at=datetime.datetime.now(),
        created_by=post.created_by,
        timestamp=datetime.datetime.now()

    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post