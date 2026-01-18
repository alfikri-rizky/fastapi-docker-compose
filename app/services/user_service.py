from fastapi import HTTPException
from sqlmodel import Session, select
from starlette.status import HTTP_404_NOT_FOUND

from app.models.database import User
from app.schema.user import UserCreate


def create_user(db_session: Session, user: UserCreate):
    new_user = User(**user.model_dump())

    db_session.add(new_user)
    db_session.commit()
    db_session.refresh(new_user)

    return new_user

def get_user(db_session: Session, user_id: str):
    # # Approach 1
    # statement = select(User).options(selectinload(User.posts)).where(User.id == user_id)
    # if not db_session.exec(statement).first():
    #     raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    # return db_session.exec(statement).first()
    statement = select(User).where(User.id == user_id)
    user = db_session.exec(statement).first()

    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="User not found")

    #  Lazy load posts
    _ = user.posts

    return user

def get_users(db_session: Session):
    return db_session.exec(select(User)).all()
