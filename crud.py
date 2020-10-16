import uuid

from sqlalchemy.orm import Session

import models
import schemas


def get_build(db: Session, guid: str):
    return db.query(models.Build).filter(models.Build.guid == guid).one_or_none()


def create_build(db: Session, build: schemas.Build):
    # @TODO: obviously should be much better than this
    guid = str(uuid.uuid4())
    # @TODO: actually log ip address
    db_build = models.Build(code=build.code, guid=guid, creator_ip='127.0.0.1')
    db.add(db_build)
    db.commit()
    db.refresh(db_build)
    return db_build
