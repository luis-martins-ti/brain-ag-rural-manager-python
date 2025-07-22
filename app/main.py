from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router as api_router
from app.db.database import engine, Base
from loguru import logger

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Rural API",
    description="Sistema de cadastro e monitoramento de produtores rurais",
    version="1.0.0",
)

app.include_router(api_router)


@app.on_event("startup")
def startup_event():
    logger.info("🚀 Aplicação iniciada")


@app.on_event("shutdown")
def shutdown_event():
    logger.info("🛑 Aplicação finalizada")
