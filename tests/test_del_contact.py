from model.contact import Contact


def test_del_fstcontact(app):
    if app.contact.count() == 0:
        app.contact.create_new_(Contact(firstname = 'test'))
    app.contact.del_fstcontact()

