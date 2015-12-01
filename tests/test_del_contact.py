

def test_del_fstcontact(app):
    app.session.login(username="admin", password="secret")
    app.contact.del_fstcontact()
    app.session.logout()
