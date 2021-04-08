"""Web server gateway interface."""

from flask import request

from his import CUSTOMER, Application, admin, authenticated, authorized
from wsgilib import JSON, JSONMessage

from contactmgr.functions import get_contact, get_contacts
from contactmgr.orm import Contact


__all__ = ['APPLICATION']


APPLICATION = Application('contactmgr')


@APPLICATION.route('/', methods=['GET'], strict_slashes=False)
@authenticated
@authorized('contactmgr')
@admin
def list_() -> JSON:
    """Lists available contacts."""

    return JSON([contact.to_json() for contact in get_contacts(CUSTOMER.id)])


@APPLICATION.route('/', methods=['POST'], strict_slashes=False)
@authenticated
@authorized('contactmgr')
@admin
def add() -> JSONMessage:
    """Adds a new contact."""

    contact = Contact.from_json(request.json, CUSTOMER.id)
    contact.save()
    return JSONMessage('Contact added.', status=201, id=contact.id)


@APPLICATION.route('/<int:ident>', methods=['PATCH'], strict_slashes=False)
@authenticated
@authorized('contactmgr')
@admin
def patch(ident: int) -> JSONMessage:
    """Patches a contact."""

    contact = get_contact(CUSTOMER.id, ident)
    contact.patch_json(request.json)
    return JSONMessage('Contact patched.', status=200)


@APPLICATION.route('/<int:ident>', methods=['DELETE'], strict_slashes=False)
@authenticated
@authorized('contactmgr')
@admin
def delete(ident: int) -> JSONMessage:
    """Deletes a contact."""

    get_contact(CUSTOMER.id, ident).delete_instance()
    return JSONMessage('Contact deleted.', status=200)
