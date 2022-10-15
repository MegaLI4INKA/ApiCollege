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
