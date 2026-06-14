from sqlalchemy.orm.session import Session

from database.models import DbPost


def get_all_posts(db:Session):
    return db.query(DbPost).all()