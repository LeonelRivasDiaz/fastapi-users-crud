from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from schemas import UserCreate, UserResponse
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
