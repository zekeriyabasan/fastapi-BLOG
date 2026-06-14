from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database.database import engine
from database import models
from routers import delete, get, post
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(post.router)
app.include_router(get.router)
app.include_router(delete.router)

models.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="images"), name="images")

origins =[
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)