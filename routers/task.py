from models.task import Task, TaskCreate, TaskUpdate, TaskInDB
from fastapi import APIRouter, HTTPException, status, Depends
from crud.task import task_crud
from dep import get_current_user

Task_router = APIRouter()


@Task_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_task(task: Task, current_user=Depends(get_current_user)):
    created = task_crud.create_task(task, current_user)
    return created

@Task_router.get("/getall", status_code=status.HTTP_200_OK)
def get_all_tasks(current_user=Depends(get_current_user)):
    tasks = task_crud.get_all_tasks(current_user)
    if not tasks:
        raise HTTPException(status_code=404, detail="No tasks found for this user")
    return {"message": "Tasks retrieved successfully", "data": tasks}


@Task_router.get("/get{id}", status_code=status.HTTP_202_ACCEPTED)
def get_task_by_ID(id: str, current_user=Depends(get_current_user)):
    payload = task_crud.get_task_by_id(id)
    return payload


@Task_router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_task(id: str, task: TaskUpdate, current_user=Depends(get_current_user)):
    details = task_crud.update_task(id, task)
    return details


@Task_router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_task(id: str, current_user=Depends(get_current_user)):
    deleted = task_crud.delete_task(id)
    return {"message": "Task deleted successfully", "data": deleted}
