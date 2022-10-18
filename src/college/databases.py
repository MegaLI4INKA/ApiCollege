from importlib.metadata import metadata

from fastapi import FastAPI
from mysqlx import Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.testing.schema import Table

# SQLALCHEMY_DATABASE_URL = "mssql://User:123@DESKTOP-M0LHBL5/testfastapi?driver=ODBC Driver 17 for SQL Server"
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://fionitos:Cvfhnajy201*@196.254.176.13:3306/db_project"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()


# ------------------------------------------------------------------------------------------------------------------------------------------------------
# так как при запихивании этого в отдельный файл я пока оставлю это тут)
class Cvalification(Base):
    __tablename__ = 'cvalification'

    idCvalification = Column(Integer, primary_key=True)
    CvalificationName = Column(String(255), nullable=False)


class Group(Base):
    __tablename__ = 'group'

    IdGroup = Column(Integer, primary_key=True)
    IdPerson = Column(ForeignKey('person.IdPerson'), nullable=False, index=True)
    GroupName = Column(String(255), nullable=False)
    IdSpec = Column(ForeignKey('specialisation.IdSpecial'), nullable=False, index=True)


class Person(Base):
    __tablename__ = 'person'

    IdPerson = Column(Integer, primary_key=True)
    IdGroup = Column(ForeignKey('group.IdGroup'), index=True)
    LastName = Column(String(255), nullable=False)
    FirstName = Column(String(255), nullable=False)
    MiddleName = Column(String(255), nullable=False)
    Number = Column(String(255), nullable=False)


class Predmet(Base):
    __tablename__ = 'predmet'

    idPredmet = Column(Integer, primary_key=True)
    PredmetName = Column(String(255), nullable=False)


class Role(Base):
    __tablename__ = 'role'

    IdRole = Column(Integer, primary_key=True)
    RoleName = Column(String(255), nullable=False)


class predmetteachere(Base):
    __tablename__ = 'predmetteacher'

    Idperson = Column(Integer, ForeignKey('person.IdPerson'), primary_key=True, nullable=False),
    IdPredmet = Column(Integer, ForeignKey('predmet.idPredmet'), primary_key=True, nullable=False)


class roleprson(Base):
    __tablename__ = 'roleprson'

    IdRole = Column(Integer, ForeignKey('role.IdRole'), primary_key=True, nullable=False),
    IdPerson = Column(Integer, ForeignKey('person.IdPerson'), primary_key=True, nullable=False)


class Specialisation(Base):
    __tablename__ = 'specialisation'

    IdSpecial = Column(Integer, primary_key=True)
    SpecialName = Column(String(255), nullable=False)
    Code = Column(String(255), nullable=False)
    IdCvalification = Column(ForeignKey('cvalification.idCvalification'), nullable=False, index=True)

class Timetable(Base):
    __tablename__ = 'timetable'

    idRaspisanie = Column(Integer, primary_key=True)
    PredmetId = Column(ForeignKey('predmet.idPredmet'), nullable=False, index=True)
    Idgroup = Column(ForeignKey('group.IdGroup'), nullable=False, index=True)
    LessonNumber = Column(Integer, nullable=False)
    WeekDay = Column(String(255), nullable=False)
    NumberRoom = Column(Integer)


# ------------------------------------------------------------------------------------------------------------------------------------------------------

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
