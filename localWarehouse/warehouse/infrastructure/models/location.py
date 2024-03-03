import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import  Uuid

from warehouse.infrastructure.models.config import Base


class Location(Base):
    __tablename__ = "warehouse_locations"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, default="")
