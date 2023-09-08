from models.policy import Policy
from utils.repository import SQLAlchemyRepository


class PoliciesRepository(SQLAlchemyRepository):
    model = Policy