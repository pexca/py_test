from model.contact import Contact
from random import randrange


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

