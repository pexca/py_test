def test_rename_group(app):
    app.session.login(username="admin", password="secret")
    app.group.rename()
    app.session.logout()