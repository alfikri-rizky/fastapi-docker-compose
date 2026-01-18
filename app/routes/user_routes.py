from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.models.engine import db_session
from app.schema.user import UserCreate, UserRead
from app.services.user_service import create_user, get_user, get_users

user_router = APIRouter(prefix="/users", tags=["users"])


@user_router.get("/", response_model=list[UserRead])
def get_users_api(db: Session = Depends(db_session)):
    return get_users(db)

@user_router.get("/{user_id}", response_model=UserRead)
def get_user_by_id_api(user_id: str, db: Session = Depends(db_session)):
    return get_user(db, user_id)

@user_router.post("/", response_model=UserRead)
def create_user_api(user_create: UserCreate, db: Session = Depends(db_session)):
    return create_user(db, user_create)
