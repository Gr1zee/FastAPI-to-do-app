import uvicorn
from fastapi import FastAPI

from app.core.config import settings

from contextlib import asynccontextmanager

from app.core.models import db_helper, Base
from app.api.api_v1 import router as api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # start
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(prefix=settings.api.prefix, router=api_v1_router)

if __name__ == "__main__":
    # When running this file directly with python, use this path
    uvicorn.run(
        "app.main:app", host=settings.run.host, port=settings.run.port, reload=True
    )
