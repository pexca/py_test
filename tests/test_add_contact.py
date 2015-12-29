# -*- coding: utf-8 -*-

from model.contact import *
import pytest
import random
import string  # константы, хранящие списки символов


def randstring(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+' '*5  # add 5 spaces
    return prefix+''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    # генерирует строчку случайной длины, не прев.мах

#  add empty contact once, add random contact 4 times
test_data = [Contact(firstname="", lastname="", email="")] + [
    Contact(firstname=randstring('fname', 10), lastname=randstring('lname', 10), email=randstring('email', 10))
    for i in range(4)
]

'''
#  генерирует комбинации тестовых данных
test_data = [
    Contact(firstname=fname, lastname=lname, email=email)
    for fname in ['', randstring('fname', 10)]
    for lname in ['', randstring('lname', 10)]
    for email in ['', randstring('email', 10)]
]
'''


@pytest.mark.parametrize('contact', test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_conts = app.contact.get_conts_lst()
    app.contact.create_new_(contact)
    assert len(old_conts)+1 == app.contact.count()
    new_conts = app.contact.get_conts_lst()
    old_conts.append(contact)
    assert sorted(old_conts, key=Contact.id_or_max) == sorted(new_conts, key=Contact.id_or_max)
