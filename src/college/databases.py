from fastapi import FastAPI
from mysqlx import Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://fionitos:Cvfhnajy201*@196.254.176.13:3306/db_project"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()


# ------------------------------------------------------------------------------------------------------------------------------------------------------
# так как при запихивании этого в отдельный файл я пока оставлю это тут)
class person(Base):
    __tablename__ = "person"

    IdPerson = Column(Integer, primary_key=True, index=True)
    LastName = Column(String)
    Firstname = Column(String)
    MiddleName = Column(String)
    Number = Column(String)


class specialisation(Base):
    __tablename__ = "specialisation"

    IdSpecial = Column(Integer, primary_key=True, index=True)
    SpecialName = Column(String)
    Code = Column(String)


class role(Base):
    __tablename__ = "role"

    IdRole = Column(Integer, primary_key=True, index=True)
    RoleName = Column(String, unique=True)


class timetable(Base):
    __tablename__ = "timetable"

    idRaspisanie = Column(Integer, primary_key=True, index=True)
    LessonNumber = Column(Integer)
    WeekDay = Column(String, unique=True)


class predmet(Base):
    __tablename__ = "predmet"

    idPredmet = Column(Integer, primary_key=True, index=True)
    PredmetName = Column(String)


# ------------------------------------------------------------------------------------------------------------------------------------------------------

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
