from pydantic import BaseModel


class Person(BaseModel):
    Personid: int
    LastName: str
    Firstname: str
    MiddleName: str
    Number: str

    class Config:
        orm_mode = True