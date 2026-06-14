from fastapi import FastAPI
from database.database import engine
from database import models
from routers import post

app = FastAPI()
app.include_router(post.router)

models.Base.metadata.create_all(engine)