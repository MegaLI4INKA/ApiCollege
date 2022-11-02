from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.college.databases import *
import requests
import redis

link_name_container_vitalika = "Apiv"

# redis_client = redis.Redis(host="localhost",port=6379,db=0)

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# берет расписание по группе в редиске
# @app.get("/api/get/raspisanie/id_group/{id}")
# def get_raspisanie(id: int):
#     redis_client = redis.Redis(host="localhost",port=6379,db=0)
#     return redis_client.json()


@app.get("/api/get/raspisanie/id/group/{id}")
def get_raspisanie(id: int, db: Session = Depends(get_db)):
    raspisaniesall = db.query(TimeTable).filter(TimeTable.IdGroup == id).all()
    return raspisaniesall


# ищет пупса по айди
@app.get("/api/get/person/id/{id}")
def get_person_id(id: int, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.IdPerson == id).first()
    return person


# ищет куратора группы
@app.get("/api/get/persons-to-group/idgroup/{idgroup}")
def get_all_pers_group(idgroup: int, db: Session = Depends(get_db)):
    KuratorsToGroups = db.query(Person).filter(Person.IdGroup == idgroup).all()
    return KuratorsToGroups


# ищет пупса по айди
@app.get("/api/get/person/id/{id}")
def get_person_id(id: int, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.IdPerson == id).first()
    return person


@app.get("/api/get/predmet/id/{id}")
def get_predmet_id(id: int, db: Session = Depends(get_db)):
    predmetId = db.query(Predmet).filter(Predmet.idPredmet == id).first()
    return predmetId


@app.get("/api/get/predmet/all")
def get_predmet_all(db: Session = Depends(get_db)):
    predmets = db.query(Predmet).all()
    return predmets


# ср балл
@app.get("/api/get/middle_point/group_name/{group}/id_student/{id_student}")
def get_person_ball(id_student, group: str):
    response = requests.get(f"http://{link_name_container_vitalika}:8080/get/middle_point/group/{group}/id_student/{id_student}")
    return response.json()


# вывод двоек
@app.get("/api/get/bad_point/group_name/{group}/id_student/{id_student}")
def get_person_ocenca(id_student, group: str):
    response = requests.get(f"http://{link_name_container_vitalika}:8080/get/bad_point/group/{group}/id_student/{id_student}")
    return response.json()

# вывод всех учеников со средним баллом
@app.get("/get/all_middle_grade/group/{link_table}")
def get_person_ocenca(link_table: str):
    response = requests.get(f"http://{link_name_container_vitalika}:8080/get/all_middle_grades/group/{link_table}")
    return response.json()

# все оценочки студента
@app.get("/get/grade/group/{link_table}/id_student/{id_student}")
def get_person_ocenca(link_table: str, id_student: str):
    response = requests.get(f"http://{link_name_container_vitalika}:8080/get/grades/group/{link_table}/id_student/{id_student}")
    return response.json()