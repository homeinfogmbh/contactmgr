"""Common functions."""

from typing import Union

from peewee import ModelSelect

from mdb import Customer

from contactmgr.orm import Contact


__all__ = ["get_contacts", "get_contact"]


def get_contacts(customer: Union[int, Customer]) -> ModelSelect:
    """Returns the contacts of the current customer."""

    return Contact.select(cascade=True).where(Contact.customer == customer)


def get_contact(customer: Union[int, Customer], ident: int) -> Contact:
    """Returns the contact with the given ID of the current customer."""

    return get_contacts(customer).where(Contact.id == ident).get()
