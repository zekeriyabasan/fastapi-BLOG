import random
import shutil
import string

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
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
    
@router.post('/images')
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    random_string = ''.join(random.choice(letter) for i in range(10))
    file_location = f"images/{random_string}_{image.filename}"
    with open(file_location, "w+b") as buffer:
      shutil.copyfileobj(image.file, buffer)

    return {"info": f"file '{image.filename}' saved at '{file_location}'"}