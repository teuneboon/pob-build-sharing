from pydantic import BaseModel, Field


class Build(BaseModel):
    code: str = Field(..., max_length=65000)

    class Config:
        orm_mode = True
