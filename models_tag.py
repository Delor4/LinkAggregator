#!/usr/bin/env python

from base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    cards = relationship("CardTag", backref="tags.id")

class CardTag(Base):
    __tablename__ = 'cardtags'
    id = Column(Integer, primary_key=True)

    card_id = Column(Integer, ForeignKey("cards.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))
