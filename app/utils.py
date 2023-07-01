""" Various utils """
from enum import StrEnum

from loguru import logger
from pydantic import BaseModel, EmailStr, validate_email
from sqlalchemy.orm import Session
from tenacity import TryAgain, retry, stop_after_attempt, wait_fixed

from .database import get_db
from .services.caching import redis_service
from .settings import settings

RETRY_TRIES = 1 if settings.DEBUG else 5
RETRY_WAIT_SECONDS = 1 if settings.DEBUG else 2

class LowerEmailStr(EmailStr):
    """Lower email str."""

    @classmethod
    def validate(cls, value: str) -> str:
        """Validate.

        Args:
            value: Email str.

        Returns:
            Any: Lower Email str.
        """
        email = validate_email(value)[1]
        return email.lower()


class HealthCheckStatus(StrEnum):
    """Health check status."""

    OK = "ok"
    FAIL = "fail"


class HealthCheckResponse(BaseModel):
    """Health check status."""
    database: HealthCheckStatus
    redis: HealthCheckStatus


def get_health_check_status_for_database(Db: Session) -> HealthCheckStatus: # pylint: disable=C0103
    """Get health check status for database.

    Args:
        db: Database session.

    Returns:
        HealthCheckStatus: Health check status.

    Raises:
        Exception: If database health check failed.
    """
    try:
        Db.execute("SELECT 1")
        return HealthCheckStatus.OK
    except Exception as error:  # pragma: no cover
        logger.debug(f"Database health check failed with error: {error}")
        return HealthCheckStatus.FAIL


async def get_health_check_status_for_redis() -> HealthCheckStatus:
    """Get health check status for redis.

    Returns:
        HealthCheckStatus: Health check status.

    Raises:
        Exception: If redis health check failed.
    """
    try:
        if await redis_service.ping():
            return HealthCheckStatus.OK
        return HealthCheckStatus.FAIL
    except Exception as error:  # pragma: no cover
        logger.debug(f"Redis health check failed with error: {error}")
        return HealthCheckStatus.FAIL


@retry(
    stop=stop_after_attempt(RETRY_TRIES),
    wait=wait_fixed(RETRY_WAIT_SECONDS),
)
async def do_health_checks_on_application_startup() -> None:
    """Do health checks on application startup.

    Raises:
        TryAgain: If health check failed.

    """
    database_status = get_health_check_status_for_database(Db=next(get_db()))
    logger.info(f"Database status: {database_status}")
    redis_status = await get_health_check_status_for_redis()
    logger.info(f"Redis status: {redis_status}")
    if database_status == HealthCheckStatus.FAIL or redis_status == HealthCheckStatus.FAIL:
        logger.error("Application startup failed, Redis is not ready.")
        raise TryAgain
