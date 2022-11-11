from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

# SQLALCHEMY_DATABASE_URL = "mssql://User:123@DESKTOP-M0LHBL5/testfastapi?driver=ODBC Driver 17 for SQL Server"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://root:Cvfhnajy201*@192.168.0.2:3306/db_project"

# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:123@mysqls:3306/db_project"
# mysqls - название контейнера в котором находится бд
# порт указывается тот который указывался в mysql ибо здесь мы порт на пк не прокидываем

link_name_container_db_mysql = "mysqls"
link_name_db_mysql_dbname = "db_project"
link_name_db_mysql_port = "3306"

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://root:123@{link_name_container_db_mysql}:{link_name_db_mysql_port}/{link_name_db_mysql_dbname}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()


# ------------------------------------------------------------------------------------------------------------------------------------------------------
# так как при запихивании этого в отдельный файл я пока оставлю это тут)
class Group(Base):
    __tablename__ = 'Group'

    IdGroup = Column(Integer, primary_key=True)
    IdPerson = Column(ForeignKey('Person.IdPerson'), nullable=False, index=True)
    GroupName = Column(String(255), nullable=False)
    IdSpecial = Column(ForeignKey('Specialisation.IdSpecial'), nullable=False, index=True)


class Person(Base):
    __tablename__ = 'Person'

    IdPerson = Column(Integer, primary_key=True)
    LastName = Column(String(255), nullable=False)
    FirstName = Column(String(255), nullable=False)
    MiddleName = Column(String(255), nullable=False)
    Number = Column(String(255), nullable=False)
    IdGroup = Column(ForeignKey('Group.IdGroup'), index=True)


class Predmet(Base):
    __tablename__ = 'Predmet'

    idPredmet = Column(Integer, primary_key=True)
    PredmetName = Column(String(255), nullable=False)


class Role(Base):
    __tablename__ = 'Role'

    IdRole = Column(Integer, primary_key=True)
    RoleName = Column(String(255), nullable=False)


class Specialisation(Base):
    __tablename__ = 'Specialisation'

    IdSpecial = Column(Integer, primary_key=True)
    SpecialName = Column(String(255), nullable=False)
    Code = Column(String(255), nullable=False)


class Cvalifications(Base):
    __tablename__ = 'Cvalification'

    IdCvalification = Column(Integer, primary_key=True)
    IdSpecial = Column(ForeignKey('Specialisation.IdSpecial'), nullable=False, index=True)
    CvalificationName = Column(String(255), nullable=False)


class PredmetTeacher:
    __tablename__ = 'PredmetTeacher'

    Column('Idperson', ForeignKey('Person.IdPerson'), nullable=False, index=True),
    Column('IdPredmet', ForeignKey('Predmet.idPredmet'), nullable=False, index=True)


class RolePerson:
    __tablename__ = 'RolePerson',
    Column('IdRole', ForeignKey('Role.IdRole'), nullable=False, index=True),
    Column('IdPerson', ForeignKey('Person.IdPerson'), nullable=False, index=True)


class TimeTable(Base):
    __tablename__ = 'TimeTable'

    idRaspisanie = Column(Integer, primary_key=True)
    PredmetId = Column(ForeignKey('Predmet.idPredmet'), nullable=False, index=True)
    IdGroup = Column(ForeignKey('Group.IdGroup'), nullable=False, index=True)
    LessonNumber = Column(Integer, nullable=False)
    WeekDay = Column(String(255), nullable=False)


class Specialisationn(Base):
    __tablename__ = 'specialisation'

    IdSpecial = Column(Integer, primary_key=True)
    SpecialName = Column(String(255), nullable=False)
    Code = Column(String(255), nullable=False)
    IdCvalification = Column(ForeignKey('Cvalification.IdCvalification'), nullable=False, index=True)


# ------------------------------------------------------------------------------------------------------------------------------------------------------

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
