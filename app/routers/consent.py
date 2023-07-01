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
from fastapi import APIRouter, status

from ..schemas.consent import ConsentType


router = APIRouter()


@router.get(
    path="/{name}",
    status_code=status.HTTP_200_OK,
)
def get_consent_by_id(
    name: ConsentType,
):
    """Get dictionary by name.

    Args:
        name: Dictionary name.
        dictionaries_repository: Dictionaries repository.

    Returns:
        Dictionary: Dictionary.
    """
    if name == ConsentType.BILLING:
        return "billing"
    else:
        return "privacy_policies"
