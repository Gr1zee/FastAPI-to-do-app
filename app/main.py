import uvicorn
from fastapi import FastAPI

from app.tasks.views import router as tasks_router
from app.users.views import router as users_router

from api import router as api_router

from app.core.config import settings

app = FastAPI()
app.include_router(
    settings.api.prefix,
)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
