# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_conts = app.contact.get_conts_lst()
    contact = Contact(firstname="Alla", lastname="Frolova", email="pexca@rambler.ru")
    app.contact.create_new_(contact)
    assert len(old_conts)+1 == app.contact.count()
    new_conts = app.contact.get_conts_lst()
    old_conts.append(contact)
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)


"""
def test_add_empty_contact(app):
    app.contact.create_new_(Contact(firstname="", lastname="", email=""))
"""