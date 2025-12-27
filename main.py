from fastapi import FastAPI, HTTPException
from models import Task

app = FastAPI()

tasks: list[Task] = [
    Task(id=1, title="Learn FastAPI", description="Study FastAPI fundamentals"),
    Task(id=2, title="Build an API", description="Create a REST API with FastAPI"),
]

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/tasks", response_model=list[Task])
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")
