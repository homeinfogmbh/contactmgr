"""Common functions."""

from peewee import ModelSelect

from his import CUSTOMER

from contactmgr.orm import Contact


__all__ = ['get_contacts', 'get_contact']


def get_contacts() -> ModelSelect:
    """Returns the contacts of the current customer."""

    return Contact.select(cascade=True).where(Contact.customer == CUSTOMER.id)


def get_contact(ident: int) -> Contact:
    """Returns the contact with the given ID of the current customer."""

    return get_contacts().where(Contact.id == ident).get()
