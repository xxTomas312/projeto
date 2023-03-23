from fastapi import FastAPI
from src.routers import root

api = FastAPI(
    title="dakee_api",
    description="An API for dakee"
)

routers = [
    root.router
]

for router in routers:
    api.include_router(router=router)