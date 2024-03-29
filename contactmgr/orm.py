"""Contacts database."""

from __future__ import annotations
from typing import Union

from peewee import CharField, ForeignKeyField, ModelSelect

from mdb import Company, Customer
from peeweeplus import EnumField, JSONModel, MySQLDatabase

from contactmgr.config import CONFIG
from contactmgr.enumerations import ContactType


__all__ = ["Contact"]


DATABASE = MySQLDatabase.from_config(CONFIG)


class ContactModel(JSONModel):  # pylint: disable=R0903
    """Basic contact model."""

    class Meta:  # pylint: disable=C0115,R0903
        database = DATABASE
        schema = database.database


class Contact(ContactModel):  # pylint: disable=R0903
    """Represents a contact."""

    customer = ForeignKeyField(Customer, column_name="customer")
    first_name = CharField()
    last_name = CharField()
    type = EnumField(ContactType)
    phone = CharField(null=True)
    mobile = CharField(null=True)
    email = CharField(null=True)

    @classmethod
    def from_json(cls, json: dict, customer: Union[Customer, int]) -> Contact:
        """Creates a contact from a JSON-ish dict."""
        record = super().from_json(json)
        record.customer = customer
        return record

    @classmethod
    def select(cls, *args, cascade: bool = False, **kwargs) -> ModelSelect:
        """Selects contacts."""
        if not cascade:
            return super().select(*args, **kwargs)

        args = {cls, Customer, Company, *args}
        return super().select(*args, **kwargs).join(Customer).join(Company)
