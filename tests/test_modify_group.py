from model.group import Group


def test_modify_gName(app):
    if app.group.count() == 0:
        app.create_group(Group(name = "test"))
    app.group.modify_fst_g(Group(name="New group"))


def test_modify_gHeader(app):
    if app.group.count() == 0:
        app.create_group(Group(name = "test"))
    app.group.modify_fst_g(Group(header="New header"))
