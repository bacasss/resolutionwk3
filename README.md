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

**start with todo-api
if that doesnt work, try python -m resolution_week3_bacasss.main (worked for me in a test folder)

FastAPI Swagger UI showing featuresssss:
<img width="1919" height="1199" alt="image" src="https://github.com/user-attachments/assets/3667bfd7-9ccb-4692-ba4a-be8da9068c2f" />
