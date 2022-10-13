import shutil
from fastapi import File, UploadFile, APIRouter, Query, Form
from sqlalchemy.orm import Session
from src.college import models
from src.college.schemas import Person

app_router = APIRouter()

@app_router.get("/Person")
async def GetUsers():
    person = Person(Personid=12,LastName="Lox",Firstname="Nazar",MiddleName="Beckbazarov",Number="89990349482")
    return {"person": person}
