# -*- coding: utf-8 -*-

from model.contact import *
import random
import string  # константы, хранящие списки символов


# @pytest.mark.parametrize('contact', test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, json_contacts):  # второй параметр указывает на источник тестовых данных
    contact = json_contacts
    old_conts = app.contact.get_conts_lst()
    app.contact.create_new_(contact)
    assert len(old_conts)+1 == app.contact.count()
    new_conts = app.contact.get_conts_lst()
    old_conts.append(contact)
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)
