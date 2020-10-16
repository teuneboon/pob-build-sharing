from pydantic import BaseModel


class Build(BaseModel):
    code: str

    class Config:
        orm_mode = True
