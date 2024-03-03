from uuid import UUID

from sqlalchemy.orm import Session

from warehouse.domain import entities
from warehouse.infrastructure import models


def get_location(db: Session, location_id: UUID):
    return db.query(models.Location).filter(models.Location.id == location_id).first()


def get_locations(db: Session):
    return db.query(models.Location).all()


def create_location(db: Session, location: entities.LocationCreate):
    db_location = models.Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location
