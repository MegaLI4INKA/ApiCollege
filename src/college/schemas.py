from pydantic import BaseModel


class PersonShemas(BaseModel):
    Personid: int
    LastName: str
    Firstname: str
    MiddleName: str
    Number: str

    class Config:
        orm_mode = True
