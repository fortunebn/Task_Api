from models.user import UserDb
from models.task import TaskInDB

def user_serializer(user)-> UserDb:
    user_dict = {
        "id": str(user.get("_id")),
        "username": user.get("username"),
        "last_name": user.get("last_name"),
        "email": user.get("email"),
        "password": user.get("password")
    }
    return UserDb(**user_dict)

def task_serializer(task) -> TaskInDB:
    task_dict = {
        "id": str(task.get("_id")),
        "task_name": task.get("task_name"),
        "description": task.get("description"),
        "due_date": task.get("due_date"),
        "status": task.get("status"),
        "user_username": task.get("user_username"),
    }
    return TaskInDB(**task_dict)
