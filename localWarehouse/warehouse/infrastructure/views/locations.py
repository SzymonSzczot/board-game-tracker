from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from db import get_db
from warehouse.domain import entities
from warehouse.infrastructure import adapters


router = APIRouter(
    prefix="/locations",
    tags=["warehouse", "locations"],
)


@router.post("/", response_model=entities.LocationRetrieve)
def create_location(location: entities.LocationCreate, db: Session = Depends(get_db)):
    location = adapters.create_location(db=db, location=location)
    return adapters.get_location(db=db, location_id=location.id)


@router.get("/{location_id}", response_model=entities.LocationRetrieve)
async def get_location(location_id: UUID, db: Session = Depends(get_db)):
    return adapters.get_location(db=db, location_id=location_id)


@router.get("/", response_model=list[entities.LocationRetrieve])
async def get_location(db: Session = Depends(get_db)):
    return adapters.get_locations(db=db)
