

def test_del_fstgroup(app):
    app.session.login(username="admin", password="secret")
    app.group.del_fst_group()
    app.session.logout()
