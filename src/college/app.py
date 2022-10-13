from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from src.college import models
from src.college.schemas import Person
from src.college.routerdiles import app_router
from src.college import routerdiles

app = FastAPI()

app.include_router(app_router)

routerdiles.GetUsers()

SQLALCHEMY_DATABASE_URL = "mysql://root@127.0.0.1:3306/CollegeBD"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
# def create_user(db: Session, user: schemas.User):
#     db_user = models.User()
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
