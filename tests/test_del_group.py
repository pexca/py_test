from model.group import Group
from random import randrange


def test_del_somegroup(app):
    if app.group.count() == 0:
        app.create_group(Group(name='test'))
    old_groups = app.group.get_gr_list()
    idx = randrange(len(old_groups))
    app.group.del_idxgroup(idx)
    new_groups = app.group.get_gr_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups[idx:idx+1] = []
    assert old_groups == new_groups



