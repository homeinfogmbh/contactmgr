"""Contacts database."""

from peewee import CharField, ForeignKeyField

from mdb import Customer
from peeweeplus import EnumField, JSONModel, MySQLDatabase

from contactmgr.config import CONFIG
from contactmgr.enumerations import ContactType


__all__ = ['Contact']


DATABASE = MySQLDatabase.from_config(CONFIG)


class ContactModel(JSONModel):  # pylint: disable=R0903
    """Basic contact model."""

    class Meta:     # pylint: disable=C0115,R0903
        database = DATABASE
        schema = database.database


class Contact(ContactModel):    # pylint: disable=R0903
    """Represents a contact."""

    customer = ForeignKeyField(Customer, column_name='customer')
    first_name = CharField()
    last_name = CharField()
    type = EnumField(ContactType)
    phone = CharField(null=True)
    mobile = CharField(null=True)
    email = CharField(null=True)
