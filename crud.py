from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    nuevo = User(name=user.name, email=user.email)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def get_users(db: Session):
    return db.query(User).all()
