from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TaskStatus(str, Enum):
    INCOMPLETE = "Incomplete"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class TaskBase(BaseModel):
    task_name: str
    description: str
    due_date: datetime
    status: TaskStatus = TaskStatus.INCOMPLETE


class TaskCreate(TaskBase):
    created_at: datetime = datetime.now()

class Task(TaskBase):
    pass

class TaskUpdate(BaseModel):
    task_name: str | None = None
    description: str | None = None
    due_date: datetime | None = None
    status: str | None = None


class TaskInDB(TaskCreate):
    id: str
    user_username: str