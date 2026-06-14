
from sqlalchemy.orm import Session

from database.models import DbPost


def delete_post(db: Session, post_id: int):
    post = db.query(DbPost).filter(DbPost.id == post_id).first()
    if not post:
        return None
    db.delete(post)
    db.commit()
    return post