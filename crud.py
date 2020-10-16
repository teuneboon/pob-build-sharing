import logging

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models
from helpers import generate_random_guid

MAX_ATTEMPTS = 3


def get_build(db: Session, guid: str):
    return db.query(models.Build).filter(models.Build.guid == guid).one_or_none()


def create_build(db: Session, build: str):
    """ Creates a build with a random guid, returns None if it fails to create a build """
    attempts = 0

    # @TODO: super scuffed way to make sure we generate a unique id. Assume an integrity error is a duplicate entry
    db_build = None
    while attempts < MAX_ATTEMPTS:
        attempts += 1

        guid = generate_random_guid()
        # @TODO: actually log ip address
        db_build = models.Build(code=build, guid=guid, creator_ip='127.0.0.1')
        db.add(db_build)

        try:
            db.commit()
        except IntegrityError:
            logging.getLogger().warning('Had a collision with build guid: {}'.format(guid))
            db.rollback()
            db_build = None
        else:
            break

    if db_build:
        db.refresh(db_build)

    return db_build
