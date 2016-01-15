from model.group import Group
import random


def test_modify_gName(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_byid(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_gr_list(), key=Group.id_or_max)


"""
def test_modify_gHeader(app):
    if app.group.count() == 0:
        app.create_group(Group(name="test"))
    old_groups = app.group.get_gr_list()
    app.group.modify_fst_g(Group(header="New header"))
    new_groups = app.group.get_gr_list()
    assert len(old_groups) == len(new_groups)
    """

