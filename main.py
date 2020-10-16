from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session

import crud
import models
from database import engine
from get_db import get_db
from schemas import Build

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/{build_id}')
def get_build(
        *,
        db: Session = Depends(get_db),
        build_id: str = Query(..., description='The ID of the build, for example: 1a2b3c4e'),
) -> Build:
    """ Returns the base64-encoded build code to import into Path of Building """
    return crud.get_build(db, build_id)


@app.post('/create')
def create_build(
        *,
        db: Session = Depends(get_db),
        build: Build,
) -> str:
    """ """
    db_build = crud.create_build(db, build)
    return db_build.guid
