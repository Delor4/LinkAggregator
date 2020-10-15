#!/usr/bin/env python
from classes.config import config

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import relationship, backref, sessionmaker

    import base

    import models.card
    import models.link
    import models.tag

    engine = create_engine(config['SQLALCHEMY_DATABASE_URI'])
    base.Base.metadata.create_all(engine, checkfirst=True)


