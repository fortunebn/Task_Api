from fastapi import FastAPI
from routers.user import user_routers
from routers.task import Task_router


app = FastAPI()
app.include_router(user_routers, tags=["User"])
app.include_router(Task_router, tags=["Task"])


@app.get("/")
def Welcome():
    return "Welcome to this Task api"

