"""Common enumerations."""

from enum import Enum


__all__ = ["ContactType"]


class ContactType(Enum):
    """Type of contact."""

    ADMINISTRATIVE = "Verwaltung"
    SOFTWARE = "Software"
    TECHNICAL = "Technik"
