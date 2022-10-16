from pydantic import BaseModel


class PersonShemas(BaseModel):
    Personid: int
    LastName: str
    Firstname: str
    MiddleName: str
    Number: str
    Groupid: int

    class Config:
        orm_mode = True


class Group(BaseModel):
    Groupid: int
    GroupName: str
    Personid: int

    class Config:
        orm_mode = True


class PersonAndGroup(BaseModel):
    Firstname: str
    LastName: str
    MiddleName: str
    Number: str
    GroupName: str
