"""Consent schema"""
from enum import StrEnum

from pydantic import UUID4, BaseModel

class BaseDictionary(BaseModel):
    """BaseDictionary"""
    id: int
    name: str | None
    description: str | None
    short_description: str | None
    lang: str | None
    region_availability: str | None


class PrivacyPolicy(BaseDictionary):
    """BaseDictionary"""
    version: str | None

    class Config:
        """BaseDictionary"""
        orm_mode = True


class TermsCondition(BaseDictionary):
    """BaseDictionary"""
    version: str | None

    class Config:
        """BaseDictionary"""
        orm_mode = True


class ConsentType(StrEnum):
    """ConsentType type."""
    BILLING = "billing"
    POSTAL = "postal"


class TermsPolicies(BaseModel):
    """Consent schema."""
    privacy_policies: list[PrivacyPolicy] | None
    terms_conditions: list[TermsCondition] | None


class Consent(BaseModel):
    """Consent schema."""
    id: int | None
    uuid: UUID4 | None
    is_active: bool | None
    is_registered: bool | None
    is_email_verified: bool | None
    is_admin: bool | None
    password: str | None
    terms_conditions_and_privacy_policy_accepted: bool | None

    class Config:
        """Consent schema."""
        orm_mode = True


class UserStatusResponse(BaseModel):
    """User status schema."""
    is_active: bool
    is_registered: bool
    is_email_verified: bool
    terms_conditions_and_privacy_policy_accepted: bool
    country_filled_flag: bool | None
