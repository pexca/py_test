from model.group import Group
import random


def test_del_somegroup(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.create_group(Group(name='test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.del_group_byid(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups)-1 == len(new_groups)
    old_groups.remove(group)  # из списка будет удалён элемент, равный заданному
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_gr_list(), key=Group.id_or_max)


