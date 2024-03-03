from uuid import UUID

from warehouse.domain.entities.location.location import Location


class LocationRetrieve(Location):
    id: UUID

    class Config:
        orm_mode = True
