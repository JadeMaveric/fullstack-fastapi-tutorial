from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import todo_dal

app = FastAPI()

# Serve static files, primarily meant to import frontend libraries
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(todo_dal.router)
