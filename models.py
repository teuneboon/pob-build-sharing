import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from database import Base


class Build(Base):
    __tablename__ = 'builds'

    id = Column(Integer, primary_key=True, index=True)
    # @TODO: not 255 length maybe
    guid = Column(String(255), nullable=False)

    # @TODO: Text is limited to 65k chars iirc, I think that's enough right?
    code = Column(Text, unique=True)

    creation_time = Column(DateTime(), default=datetime.datetime.utcnow)
    # @TODO: figure out if this is legal to always log, I think it's allowed for spam protection but might need to be in a privacy policy or something?
    # @TODO: String for IP is super lazy programming
    creator_ip = Column(String(255))
