#!/usr/bin/env python

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import relationship, backref, sessionmaker
    from app.settings import DB_URI

    import api.base as base

    import models.card
    import models.link
    import models.tag

    engine = create_engine(DB_URI)
    base.Base.metadata.create_all(engine, checkfirst=True)


