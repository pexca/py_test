from model.contact import Contact
import random

'''
def test_del_somecontact(app):
    if app.contact.count() == 0:
        app.contact.create_new_(Contact(firstname='test'))
    old_conts = app.contact.get_conts_lst()
    idx = randrange(len(old_conts))  # generates random number from 0 to given value
    app.contact.del_cont_by_idx(idx)
    new_conts = app.contact.get_conts_lst()
    assert len(old_conts)-1 == len(new_conts)
    old_conts[idx:idx+1] = []
    assert old_conts == new_conts
'''


def test_del_somecontact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_(Contact(firstname='test'))
    old_conts = db.get_contact_list()
    contact = random.choice(old_conts)
    app.contact.del_cont_byid(contact.id)
    new_conts = db.get_contact_list()
    assert len(old_conts) == len(new_conts)
    assert old_conts == new_conts
    old_conts.remove(contact)
    if check_ui:
        assert sorted(new_conts, key=Contact.id_or_max) == sorted(app.contact.get_conts_lst(), key=Contact.id_or_max)

