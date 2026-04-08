from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import json

app = FastAPI()

TASKS_FILE = "tasks.json"

# Each task will look like: {"id": 1, "task": "Buy milk", "done": False}

class TaskBody(BaseModel):
    task: str

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

@app.get("/tasks")
async def listtasks():
    tasks = load_tasks()
    return tasks

@app.post("/tasks")
async def addtask(taskss: TaskBody):
    tasks = load_tasks()
    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1]["id"] + 1
    tasks.append({"id": new_id, "task": taskss.task, "done": False, "priority": "medium"})
    save_tasks(tasks)
    return({"id": new_id, "task": taskss.task, "done": False})

@app.patch("/tasks/{task_id}/done")
async def completetask(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            tasks = load_tasks()
            return({"status": f"Task {task_id} marked as completed.", "task": task})
    raise HTTPException(status_code=404, detail="Task not found")
    
@app.delete("/tasks/{task_id}/delete")
async def deletetask(task_id: int):
    tasks = load_tasks()
    new_tasks = []
    for task in tasks:
        if task["id"] != task_id:
            new_tasks.append(task)
    if len(new_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks = new_tasks
    save_tasks(new_tasks)
    tasks = load_tasks()
    return({"status": f"Task {task_id} deleted.", "task": task})

@app.get("/tasks/filter")
async def filtertasks():
    tasks = load_tasks()
    incomplete = []
    complete = []
    for task in tasks:
        if task["done"] == False:
            incomplete.append(task)
        else:
            complete.append(task)
    filtered = incomplete + complete
    return filtered

@app.get ("/tasks/search")
async def searchtasks(keyword: str):
    tasks = load_tasks()
    matches = []
    for task in tasks:
        if keyword in task["task"]:
            matches.append(task)
    return matches

@app.patch ("/tasks/{task_id}/priority")
async def updatepriority(task_id: int, priority: str):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["priority"] = priority
            save_tasks(tasks)
            return({"status": f"Task {task_id} marked as {priority}.", "task": task})
    raise HTTPException(status_code=404, detail="Task not found")

@app.patch ("/tasks/{task_id}/edit")
async def edittask(task_id: int, newname:str):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = newname
            save_tasks(tasks)
            return({"status": f"Task {task_id} renamed to {newname}.", "task": task})
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete ("/tasks/cleardone")
async def cleardone():
    tasks = load_tasks()
    new_tasks = []
    for task in tasks:
        if task["done"] == False:
            new_tasks.append(task)
    
    tasks = new_tasks
    save_tasks(new_tasks)
    tasks = load_tasks()
    return({"status": f"Completed task cleared.", "task": new_tasks})

def main():
    import uvicorn
    uvicorn.run("resolution_week3_bacasss.main:app", host="127.0.0.1", port=8000)

if __name__ == "__main__":
    main()





# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel

# app = FastAPI()

# @app.get("/")
# async def hello_world():
#     return {"message": "Hello World", "status": "ok"}

# @app.get("/greet/{name}")
# async def greet(name: str):
#     return {"message": f"Hello, {name}!"}

# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     return {"item_id": item_id}

# class Recipe(BaseModel):
#     recipe: str
#     done: bool = False

# @app.post("/recipe")
# async def create_recipe(recipe: Recipe):
#     return {"recipe": recipe.recipe, "done": recipe.done}

# @app.get("/recipes/{recipe_id}")
# async def get_recipe(recipe_id: int):
#     recipes = load_recipes()
#     for recipe in recipes:
#         if recipe["id"] == recipe_id:
#             return recipe
#     raise HTTPException(status_code=404, detail="Recipe not found")
