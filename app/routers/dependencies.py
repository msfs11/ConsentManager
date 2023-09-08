from repositories.policy import PolicyRepository
from repositories.consent import ConsentRepository
from services.policy import PolicyService
from services.consent import ConsentService


def policy_service():
    return PolicyService(PolicyRepository)


def consent_service():
    return ConsentService(ConsentRepository)