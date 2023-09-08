from datetime import datetime

from pydantic import BaseModel


class PolicySchema(BaseModel):
    id: int
    title: str
    author_id: int
    assignee_id: int

    class Config:
        from_attributes = True


class PolicySchemaAdd(BaseModel):
    title: str
    author_id: int
    assignee_id: int