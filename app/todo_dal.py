"""
todo_dal.py

When building large software, we often separate it into multiple modules,
where each module is responsible for one specific job.

A Data Access Layer (DAL) is a part of a software application responsible
for handling interactions with a database or data storage system.

This particular DAL is responsible for reading & writing TODOs
It exposes the following functionality to external modules
1. Get all todos
2. Get a particular todo
3. Create a new todo
4. Mark a todo as done
5. Delete a todo
6. Change the description of a todo
"""

from fastapi import APIRouter, Form, HTTPException
from pydantic import BaseModel


# A router allows the web server to be split into multiple files
# https://fastapi.tiangolo.com/tutorial/bigger-applications/
router = APIRouter(prefix="/api/todo")


# Pydantic makes it easy to write dataclasses with schema validation
# https://docs.pydantic.dev/latest/why/
class Todo(BaseModel):
    id: int
    description: str
    completed: bool = False


# Mock database
# Here, we use a Python dictionary instead of an actual database.
# This allows us to avoid the complexities of setting up and connecting to a database,
# while still showcasing the fundamental concept of how data is stored & accessed

# If we were using an actual database, the functions present here would be the same
# But instead of python dictionary lookups, we'd execute sql statements

# If you'd like to recreate this using a proper database I'd recommend using SQLAlchemy
# Install it using:
#     pip install SQLAlchemy
# The office tutorial for SQLAlchemy:
#     https://docs.sqlalchemy.org/en/20/tutorial/index.html
_todo_database: dict[int, Todo] = {
    0: Todo(id=0, description="Get out of bed", completed=True),
    1: Todo(id=1, description="Make breakfast", completed=False),
}
_todo_id_counter = len(_todo_database.values())


@router.get("/{todo_id}")
def fetch_todo(todo_id: int) -> Todo:
    try:
        return _todo_database[todo_id]
    except KeyError:
        raise HTTPException(404)


@router.get("/")
def fetch_all_todos() -> list[Todo]:
    return list(_todo_database.values())


@router.post("/")
def create_new_todo(description: str = Form(...)) -> Todo:
    global _todo_id_counter, _todo_database

    todo = Todo(id=_todo_id_counter, description=description, completed=False)

    # Update database
    _todo_database[todo.id] = todo
    _todo_id_counter += 1

    return todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: int) -> Todo:
    todo = _todo_database[todo_id]
    del _todo_database[todo_id]
    return todo


@router.put("/mark-as-done/{todo_id}")
def mark_todo_as_done(todo_id: int) -> Todo:
    todo = _todo_database[todo_id]
    todo.completed = True
    return todo


@router.put("/change-description/{todo_id}")
def change_todo_description(todo_id: int, description: str = Form(...)) -> Todo:
    todo = _todo_database[todo_id]
    todo.description = description
    return todo
