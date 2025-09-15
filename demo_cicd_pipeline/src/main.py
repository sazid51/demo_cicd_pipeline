from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    id: int
    name: str
    description: str

todos : List[Todo] = []

api = FastAPI()

@api.get("/")
def home():
    return {"message":"Hello World!"}

@api.get("/todos")
def get_todo():
    return todos


@api.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return todos

@api.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo:Todo):
    for index, todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return todos[index]
    return {"error":"error in updation"}

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id==todo_id:
            deleted_todo = todos.pop(index)
            return deleted_todo
    return {"error":"error in deletion"}