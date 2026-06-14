from fastapi import FastAPI
from database.database import engine
from database import models
from routers import delete, get, post

app = FastAPI()
app.include_router(post.router)
app.include_router(get.router)
app.include_router(delete.router)

models.Base.metadata.create_all(engine)