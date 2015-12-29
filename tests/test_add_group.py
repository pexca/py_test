# -*- coding: utf-8 -*-

from model.group import *
import pytest
import random
import string


def randstring(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+' '*5  # add 5 spaces
    return prefix+''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

test_data = [Group(name="", header="", footer="")] + [
    Group(name=randstring('gname', 10), header=randstring('gheader', 10), footer=randstring('gfooter', 10))
    for i in range(4)
]


@pytest.mark.parametrize('group', test_data, ids=[str(x) for x in test_data])
def test_add_group(app, group):
    old_groups = app.group.get_gr_list()
    app.group.create(group)
    assert len(old_groups)+1 == app.group.count()
    new_groups = app.group.get_gr_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
