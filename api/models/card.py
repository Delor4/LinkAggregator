#!/usr/bin/env python

from api.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(String(255))
    links = relationship("Link", backref="cards.id")
    tags = relationship("CardTag", backref="cards.id")
