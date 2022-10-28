from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.college.databases import *

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/get/raspisanie/id/{id}")
def get_raspisanie(id: int, db: Session = Depends(get_db)):
    raspisaniesall = db.query(TimeTable).filter(TimeTable.IdGroup == id).all()
    return raspisaniesall

# ищет пупса по айди
@app.get("/api/get/person/id/{id}")
def get_person(id: int, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.IdPerson == id).first()
    return person

# ищет куратора группы
@app.get("/api/get/persons-to-group/idgroup/{idgroup}")
def get_person(idgroup: int, db: Session = Depends(get_db)):
    KuratorsToGroups = db.query(Person).filter(Person.IdGroup == idgroup).all()
    return KuratorsToGroups

# ищет пупса по айди
@app.get("/api/get/person/id/{id}")
def get_person(id: int, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.IdPerson == id).first()
    return person

@app.get("/api/get/predmet/id/{id}")
def get_person(id:int,db: Session = Depends(get_db)):
    predmetId = db.query(Predmet).filter(Predmet.idPredmet == id).first()
    return predmetId

@app.get("/api/get/predmet/all")
def get_person(db: Session = Depends(get_db)):
    predmets = db.query(Predmet).all()
    return predmets
