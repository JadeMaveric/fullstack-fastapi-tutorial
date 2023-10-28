from pprint import pprint

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/todo")


class Todo(BaseModel):
    id: int
    description: str
    completed: bool = False


# Mock database
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
def create_new_todo(description: str) -> Todo:
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
def change_todo_description(todo_id: int, description: str) -> Todo:
    todo = _todo_database[todo_id]
    todo.description = description
    return todo


# For testing...
def print_database():
    pprint(_todo_database)
