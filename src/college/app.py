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


@app.get("/tests")
def get_people(db: Session = Depends(get_db)):
    persona = db.query(person).filter(person.Firstname == 'Vadim').first()
    return PersonAndGroup(Firstname=persona.Firstname,GroupName=persona.PersonGroup.GroupName,
                          LastName=persona.LastName,MiddleName=persona.MiddleName,Number=persona.Numbers)

# ---------------------------------Persons------------------------------------
@app.get("/api/persons")
def get_people(db: Session = Depends(get_db)):
    persons = db.query(person).all()
    return persons

# Получает всех людей по id группы
@app.get("/api/persons/groupid/{id}")
def get_people(id: int, db: Session = Depends(get_db)):
    first = db.query(person).filter(person.Groupid == id).all()
    return first

# Получает всех людей по имени
@app.get("/api/persons/name/{name}")
def get_people(name: str,lastname:str=None, db: Session = Depends(get_db)):
    first = db.query(person).filter(person.Firstname == name).all()
    return first

# Получает группу и айди куратора по названию группы
@app.get("/kurator")
def get_people(db: Session = Depends(get_db)):
    kurator = db.query(Groups).filter(Groups.GroupName == '230c').all()
    return kurator