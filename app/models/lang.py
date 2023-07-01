""" Lang """
from sqlalchemy import Boolean, Column, String

from base_model import BaseModel


class LangORM(BaseModel):
    """ LangORM """
    __tablename__ = "lang"

    name: str = Column(String, nullable=False)
    is_enabled: bool = Column(Boolean, nullable=False, default=False)
