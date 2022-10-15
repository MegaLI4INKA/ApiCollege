from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from src.college import models
from src.college.schemas import *
from src.college.databases import *

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/Allpersons")
def get_people(db: Session = Depends(get_db)):
    persons = db.query(person).all()
    return persons
