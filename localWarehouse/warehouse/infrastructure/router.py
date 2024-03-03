from fastapi import APIRouter

from warehouse.infrastructure.views import locations

router = APIRouter(
    prefix="/warehouse",
    tags=["warehouse"],
    responses={404: {"description": "Notfsfds found"}},
)

router.include_router(locations.router)
