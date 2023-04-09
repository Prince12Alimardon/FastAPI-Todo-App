from typing import List
from fastapi import FastAPI
import uvicorn

from model import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


todos_db = []


# CREATE
@app.post("/todos/")
async def create_todo(todo: Todo):
    todos_db.append(todo)
    return todo


# READ ALL
@app.get("/todos/")
async def read_todos(skip: int = 0, limit: int = 10):
    return todos_db[skip: skip + limit]


# READ ONE
@app.get("/todos/{todo_id}")
async def read_todo(todo_id: int):
    return todos_db[todo_id]


# UPDATE
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
    todos_db[todo_id] = todo
    return {"message": "Todo has been updated successfully!"}


# DELETE
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    todos_db.pop(todo_id)
    return {"message": "Todo has been deleted successfully!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
