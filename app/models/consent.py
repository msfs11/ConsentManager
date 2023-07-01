"""
A class for managing user consents.

Attributes:
user_id (str): The unique identifier for the user.
consent (dict): A dictionary containing the user's consent preferences.

Methods:
get_consent(): Returns the user's current consent preferences.
set_consent(consent: dict): Sets the user's consent preferences.
delete_consent(): Deletes the user's consent preferences.
"""
from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from base_model import BaseModel

if TYPE_CHECKING:
    from models.lang import LangORM


class ConsentORM(BaseModel):
    """ ConsentORM """
    __tablename__ = "consent"

    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True)
    profile_id: int = Column(
        Integer,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        nullable=False,
    )
    profile: LangORM = relationship(
        "LangORM",
        back_populates="addresses",
    )

    type: str = Column(String, nullable=False)

    country: str = Column(String, nullable=True)
    city: str = Column(String, nullable=True)
    street: str = Column(String, nullable=True)
    apartment: str = Column(String, nullable=True)
    post_code: str = Column(String, nullable=True)

    def __repr__(self):
        return f"Address(id={self.id!r})"
