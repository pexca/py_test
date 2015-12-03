from model.group import Group


def test_del_fstgroup(app):
    if app.group.count() == 0:
        app.create_group(Group(name = "test"))
    app.group.del_fst_group()


