"""Contacts manager."""

from contactmgr.config import CONFIG
from contactmgr.enumerations import ContactType
from contactmgr.functions import get_contact, get_contacts
from contactmgr.orm import Contact
from contactmgr.wsgi import APPLICATION


__all__ = [
    'APPLICATION',
    'CONFIG',
    'Contact',
    'ContactType',
    'get_contact',
    'get_contacts'
]
