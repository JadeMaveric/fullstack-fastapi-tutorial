from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import todo_dal

# FastAPI is a easy to use, but very powerful webserver
# https://fastapi.tiangolo.com/learn/
app = FastAPI()

# Serve static files, primarily meant to import frontend libraries
# https://fastapi.tiangolo.com/reference/staticfiles/
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# A router allows the web server to be split into multiple files
# https://fastapi.tiangolo.com/tutorial/bigger-applications/
app.include_router(todo_dal.router)


# https://fastapi.tiangolo.com/reference/templating
templates = Jinja2Templates(directory="app/templates")


# Homepage
@app.get("/")
def homepage(request: Request):
    todos = todo_dal.fetch_all_todos()
    return templates.TemplateResponse(
        "index.html", {"request": request, "todos": todos}
    )


@app.post("/app/add-todo")
def add_todo(request: Request, description: str = Form(...)):
    todo_dal.create_new_todo(description)
    return RedirectResponse("/", status_code=302)


@app.post("/app/mark-as-done/{todo_id}")
def mark_as_done(request: Request, todo_id: int):
    todo_dal.mark_todo_as_done(todo_id)
    return RedirectResponse("/", status_code=302)


