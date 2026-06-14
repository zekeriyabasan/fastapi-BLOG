from fastapi import FastAPI
from database.database import engine
from database import models

app = FastAPI()

@app.get('/')
def hw():
    return "SELAM ZEK !"

models.Base.metadata.create_all(engine)