from fastapi import APIRouter
from app.api import producers, properties, harvests, crops, dashboard
from app.auth import routes as auth_routes

router = APIRouter()

router.include_router(auth_routes.router)
router.include_router(producers.router)
router.include_router(properties.router)
router.include_router(harvests.router)
router.include_router(crops.router)
router.include_router(dashboard.router)
