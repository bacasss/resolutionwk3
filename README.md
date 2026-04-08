A simple todo list API utilising FastAPI that can utlisises GET, POST, PATCH and DELETE.
each task has an ID, a name, a completion status and a priority(set to medium by default)

Features:
list tasks: /tasks
add a task: /tasks via POST
mark as completed: /tasks/task_id/done
delete a task: /tasks/task_id/delete
filter by completion: /tasks/filter (i didnt use a query parameter D:)
search tasks: /tasks/search
edit task name: /tasks/task_id/edit
change task priority: /tasks/task_id/priority
delete all completed tasks: /tasks/cleardone

ALL these were tested on the FastAPI Swagger UI

**remember to fastapi dev todo-api (i think thats how it works i havent tried)