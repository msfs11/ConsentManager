""" Base Model """
from sqlalchemy import Column, DateTime, Integer, func

from ..database import Base


class BaseModel(Base):
    """ BaseModel """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
