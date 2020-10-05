#!/usr/bin/env python

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import relationship, backref, sessionmaker
    from settings import DB_URI

    import base

    import models_card
    import models_link
    import models_tag

    engine = create_engine(DB_URI)
    base.Base.metadata.create_all(engine, checkfirst=True)


