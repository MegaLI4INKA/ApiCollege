from fastapi import FastAPI, Depends
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
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

@app.get("/FirstPerson")
def get_people(db: Session = Depends(get_db)):
    first = db.query(person).filter(person.Groupid == 2).first()
    return first

@app.get("/")
def get_people(db: Session = Depends(get_db)):
    people = db.query(person).filter(person.Groupid == 1).all()
    return people
