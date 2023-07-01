"""
Database operations
"""

import databases
import ormar
import sqlalchemy

from .settings import settings

database = databases.Database(settings.DATABASE_URI)
metadata = sqlalchemy.MetaData()

class BaseMeta(ormar.ModelMeta):
    """
    User operations
    """
    metadata = metadata
    database = database

class User(ormar.Model):
    """
    User operations
    """
    class Meta(BaseMeta):
        """
        Meta operations
        """
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)


engine = sqlalchemy.create_engine(settings.DATABASE_URI)
metadata.create_all(engine)
