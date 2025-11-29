from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.api_v1.crud.users import get_all_users
from app.core.models import db_helper
from app.core.schemas.user import UserRead


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=list[UserRead])
async def get_users(session: AsyncSession = Depends(db_helper.session_getter)):
    users = await get_all_users(session=session)
    return users
