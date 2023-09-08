from models.consents import Consents
from utils.repository import SQLAlchemyRepository


class ConsentsRepository(SQLAlchemyRepository):
    model = Consents