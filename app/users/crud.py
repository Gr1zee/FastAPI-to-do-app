from fastapi import APIRouter
from users.schemas import CreateUser
router = APIRouter(prefix="/users")

@router.post("/")
def create_user(user: CreateUser):
    return "success"