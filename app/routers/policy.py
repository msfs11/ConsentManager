"""
A class for managing policies

Attributes:
id (str): The unique identifier

Methods:
get_one(id: int): Returns one policy
get(): Get list
create(): Create entity
update(id: int): Update entity
delete(id: int): Delete entity
"""
from fastapi import APIRouter, status


from dependencies import policy_service
from schemas.policy import PolicySchemaAdd
from services.policy import PolicyService
# from schemas.consent import ConsentType


router = APIRouter()


@router.get(
    path="/{name}",
    status_code=status.HTTP_200_OK,
)
def get(
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
