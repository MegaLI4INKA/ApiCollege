from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String
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

#SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://fionitos:Cvfhnajy201*@196.254.176.13:3306/db_project"
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://fionitos:Cvfhnajy201*@196.254.176.13:3306/db_project"
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


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)

@app.get("/Users", response_model=Person)
def Get_Person(db: Session = Depends(get_db)):
    operations = (
        db
        .query(Persons)
        .all()
    )
    return operations
