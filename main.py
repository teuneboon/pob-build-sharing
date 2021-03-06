from typing import Optional

from fastapi import FastAPI, Query, Depends, HTTPException, Header, UploadFile, File
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse, RedirectResponse, Response

import crud
import models
from database import engine
from get_db import get_db
from helpers import valid_content_length
from schemas import Build

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/', response_class=HTMLResponse, include_in_schema=False)
def home():
    return 'You probably want to visit <a href="/docs">/docs</a> or <a href="/redoc">/redoc</a> instead.<br />' \
           'Getting a build requires an <strong>accept: application/xml</strong> or <strong>accept: application/json</strong> header or you\'ll be redirect to this page.<br />' \
           'This should just be some fancy looking page made by someone who actually knows how to design stuff point ' \
           'people to the Path of Building download'


@app.get('/{build_id}')
def get_build(
        *,
        db: Session = Depends(get_db),
        build_id: str = Query(..., description='The ID of the build, for example: 1a2b3c4e'),
        accept: Optional[str] = Header(None),
):
    """ Returns the base64-encoded build code to import into Path of Building """
    # @TODO: I think there has to be a better way to check for application/xml/json
    if 'application/xml' not in accept and 'application/json' not in accept:
        return RedirectResponse('/')

    db_build = crud.get_build(db, build_id)
    if db_build:
        # @TODO: a bit scuffed
        if 'application/xml' in accept:
            return Response(content=db_build.code, media_type='application/xml')
        else:
            return Build.from_orm(db_build)
    else:
        raise HTTPException(status_code=404, detail='Build not found')


@app.post('/create', dependencies=[Depends(valid_content_length)])
def create_build(
        *,
        db: Session = Depends(get_db),
        build_file: UploadFile = File(...),
) -> str:
    """ Saves a build into the database and returns you with a code to retrieve the build with """
    # @TODO: read the file in chunks for more DoS safety
    build = str(build_file.file.read(), 'utf-8')

    # @TODO: this validation is not great, but should prevent most accidental issues
    if len(build) > 65000 or '<PathOfBuilding>' not in build:
        raise HTTPException(422, detail='Not a valid Path of Building code.')

    # @TODO: this can technically fail(returns None if it does), handle that properly
    db_build = crud.create_build(db, build)
    return db_build.guid
