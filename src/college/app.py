from fastapi import FastAPI
from sqlalchemy import Column ,Integer, String
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

SQLALCHEMY_DATABASE_URL = "mysql://root@127.0.0.1:3306/CollegeBD"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# так как при запихивании этого в отдельный файл я пока оставлю это тут)
class Persons(Base):
    __tablename__ = "Person"

    Personid = Column(Integer, primary_key=True, index=True)
    LastName = Column(String, unique=True)
    Firstname = Column(String)
    MiddleName = Column(String)
    Number = Column(String)
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_Person(db: Session, person: Person):
    db_user = Person(Personid=person.Personid,LastName=person.LastName,Firstname=person.Firstname,MiddleName=person.MiddleName,Number=person.Number)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/User")
async def GetUsers(db_user=None):
    return {"person": db_user}
