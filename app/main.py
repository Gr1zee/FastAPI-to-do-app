import uvicorn
from fastapi import FastAPI

# from app.tasks.views import router as tasks_router
# from app.users.views import router as users_router

# from api import router as api_router

from app.core.config import settings

from contextlib import asynccontextmanager

from app.core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # start
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI()
# app.include_router(
#     prefix=settings.api.prefix,
# )

if __name__ == "__main__":
    # When running this file directly with python, use this path
    uvicorn.run("app.main:app", host=settings.run.host, port=settings.run.port, reload=True)