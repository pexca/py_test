from model.contact import Contact
import random
from model.group import *

'''
def test_add_location(app):
    if app.contact.count() == 0:
        app.contact.create_new_(Contact(firstname='test'))
    app.contact.add_address()


def test_mod_somecontact(app):
    if app.contact.count() == 0:
        app.contact.create_new_(Contact(firstname='test'))
    old_conts = app.contact.get_conts_lst()
    contact = Contact(lastname='test')
    idx = randrange(len(old_conts))
    contact.id = old_conts[idx].id
    app.contact.modify_idxcont(idx, contact)
    new_conts = app.contact.get_conts_lst()
    assert len(old_conts) == len(new_conts)
    old_conts[idx] = contact
    assert sorted(old_conts, key=Group.id_or_max) == sorted(new_conts, key=Group.id_or_max)
'''


def test_mod_somecontact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_(Contact(firstname='test'))
    old_conts = db.get_contact_list()
    contact = random.choice(old_conts)
    app.contact.modify_cont_byid(contact.id)
    new_conts = db.get_contact_list()
    assert len(old_conts) == len(new_conts)
    if check_ui:
        assert sorted(new_conts, key=Group.id_or_max) == sorted(app.contact.get_conts_lst(), key=Group.id_or_max)




