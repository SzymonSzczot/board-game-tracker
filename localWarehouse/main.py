from fastapi import FastAPI

import warehouse.infrastructure.router

app = FastAPI()

app.include_router(warehouse.infrastructure.router.router)
