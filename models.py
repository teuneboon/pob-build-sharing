from sqlalchemy import Column, Integer, String, Text

from database import Base


class Build(Base):
    __tablename__ = 'builds'

    id = Column(Integer, primary_key=True, index=True)
    # @TODO: not 255 length maybe
    guid = Column(String(255), nullable=False)

    # @TODO: Text is limited to 65k chars iirc, I think that's enough right?
    content = Column(Text)
