from model.group import Group
from random import randrange


def test_modify_gName(app):
    if app.group.count() == 0:
        app.create_group(Group(name="test"))
    old_groups = app.group.get_gr_list()
    idx = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[idx].id  # remember id
    app.group.modify_idxgroup(idx, group)
    new_groups = app.group.get_gr_list()
    assert len(old_groups) == len(new_groups)
    old_groups[idx] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

"""
def test_modify_gHeader(app):
    if app.group.count() == 0:
        app.create_group(Group(name="test"))
    old_groups = app.group.get_gr_list()
    app.group.modify_fst_g(Group(header="New header"))
    new_groups = app.group.get_gr_list()
    assert len(old_groups) == len(new_groups)
    """

