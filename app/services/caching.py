""" Caching """

from redis import asyncio as redis

from ..settings import settings


class RedisService:
    """
    Redis service
    """
    def __init__(self):
        self._redis = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            password=settings.REDIS_PASSWORD,
            ssl=settings.REDIS_SSL,
        )

    async def get(self, key: str) -> bytes:
        """Get value from redis.

        Args:
            key: The key to get the value for

        Returns:
            The value for the key
        """
        return await self._redis.get(key)

    async def set(self, key: str, value: str, expire: int) -> bool:
        """Set a value in redis.

        Args:
            key: The key to set the value for
            value: The value to set
            expire: The time in seconds to expire the key

        Returns:
            True if the value was set, False otherwise
        """
        return await self._redis.set(key, value, ex=expire)

    async def delete(self, key: str) -> bool:
        """Delete a key from redis.

        Args:
            key: The key to delete

        Returns:
            True if the key was deleted, False otherwise
        """
        return bool(await self._redis.delete(key))

    async def exists(self, key: str) -> bool:
        """Check if a key exists in redis.

        Args:
            key: The key to check

        Returns:
            True if the key exists, False otherwise
        """
        return bool(await self._redis.exists(key))

    async def ping(self) -> bool:
        """Ping redis.

        Returns:
            True if redis is up, False otherwise
        """
        return bool(await self._redis.ping())


redis_service = RedisService()
