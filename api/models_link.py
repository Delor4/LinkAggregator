#!/usr/bin/env python

from api.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    card_id = Column(Integer, ForeignKey("cards.id"))
