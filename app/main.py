from fastapi import FastAPI
from app.tasks.views import router as tasks_router
import uvicorn
from app.users.views import router as users_router

app = FastAPI()
app.include_router(tasks_router)
app.include_router(users_router)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)