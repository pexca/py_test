

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_address()
    app.session.logout()