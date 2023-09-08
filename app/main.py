"""
app/main.py
"""
import sys
import logging
from loguru import logger

import uvicorn
from fastapi import FastAPI, Depends, Response, status
from sqlalchemy.orm import Session

from db.db import get_db
from settings import settings
from routers import all_routers
from utils import (
    HealthCheckResponse,
    HealthCheckStatus,
    do_health_checks_on_application_startup,
    get_health_check_status_for_database,
    get_health_check_status_for_redis,
)

logger.add(sys.stdout, format="{level}: {time} | {message}", level=logging.INFO)

app = FastAPI(title="ConsentManager")

for router in all_routers:
    app.include_router(router)
# app.include_router(consent_router, prefix="/consent", tags=["consent"])



@app.on_event("startup")
async def startup_event():
    """Execute when the application starts."""
    logger.info("Starting up...")
    await do_health_checks_on_application_startup()
    logger.info("Application started successfully.")


@app.on_event("shutdown")
async def shutdown_event():
    """Execute when the application shutdowns."""

@app.get("/health", response_model=HealthCheckResponse, status_code=status.HTTP_200_OK)
async def healthcheck(response: Response, 
                      Db: Session = Depends(get_db)): # pylint: disable=C0103
    """
    Health check endpoint.

    Args:
        response: The response object
        db: The database session

    Returns:
        A JSON object with a status key and value of "ok"
    """
    database_status = get_health_check_status_for_database(Db=Db)
    redis_status = await get_health_check_status_for_redis()
    if (database_status == HealthCheckStatus.FAIL 
        or redis_status == HealthCheckStatus.FAIL):
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE

    return HealthCheckResponse(
        database=database_status,
        redis=redis_status,
    )


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=settings.DEBUG_PORT)

# @app.get("/")
# async def read_root():
#     """
#     User operations
#     """
#     return await User.objects.all()


# @app.on_event("startup")
# async def startup():
#     """
#     User operations
#     """
#     if not database.is_connected:
#         await database.connect()
#     # create a dummy entry
#     await User.objects.get_or_create(email="test@test.com")


# @app.on_event("shutdown")
# async def shutdown():
#     """
#     User operations
#     """
#     if database.is_connected:
#         await database.disconnect()
