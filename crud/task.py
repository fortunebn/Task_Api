from models.task import Task, TaskCreate, TaskUpdate, TaskInDB
from models.user import UserDb
from fastapi.encoders import jsonable_encoder
from database import Task_Collection
from bson import ObjectId
from serializers import task_serializer
from fastapi import HTTPException


class Taskcrud:
    @staticmethod
    def create_task(task: Task, user: UserDb) -> TaskInDB:
        task_data = task.model_dump()
        task_data["user_username"] = user.username
        task_data_in = jsonable_encoder(task_data)
        task_id = Task_Collection.insert_one(task_data_in).inserted_id
        task_record = Task_Collection.find_one({"_id": task_id})
        payload = task_serializer(task_record)
        return {"message": "Task created successfully", "data": payload}
    

    @staticmethod
    def get_all_tasks(user: UserDb):
        tasks = Task_Collection.find({"user_username": user.username})
        if tasks:
            return [task_serializer(task) for task in tasks]
        raise HTTPException(status_code=404, detail="No tasks found for this user")

    @staticmethod
    def get_task_by_id(task_id: str):
        task_record = Task_Collection.find_one({"_id": ObjectId(task_id)})
        if task_record:
            return task_serializer(task_record)
        raise HTTPException(status_code=404, detail="Task not found")

    @staticmethod
    def update_task(task_id: str, task_update: TaskUpdate):
        task_data = task_update.model_dump(exclude_unset=True)
        result = Task_Collection.update_one(
            {"_id": ObjectId(task_id)}, {"$set": task_data}
        )
        if result.modified_count == 0:
            raise HTTPException(
                status_code=404, detail="Task not found or no changes made"
            )
        updated_task = Task_Collection.find_one({"_id": ObjectId(task_id)})
        return {
            "message": "Task updated successfully",
            "data": task_serializer(updated_task),
        }

    @staticmethod
    def delete_task(task_id: str):
        result = Task_Collection.delete_one({"_id": ObjectId(task_id)})
        if not result:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task deleted successfully"}


task_crud = Taskcrud()
