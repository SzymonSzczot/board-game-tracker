from warehouse.infrastructure.models import config


config.Base.metadata.create_all(bind=config.engine)


def get_db():
    db = config.SessionLocal()
    try:
        yield db
    finally:
        db.close()
