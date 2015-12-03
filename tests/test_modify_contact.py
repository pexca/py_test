from model.contact import Contact


def test_add_location(app):
    if app.contact.count() == 0:
        app.contact.create_new_(Contact(firstname='test'))
    app.contact.add_address()


def test_mod_fstc(app):
    if app.contact.count() == 0:
        app.contact.create_new_(Contact(firstname='test'))
    app.contact.mod_fstC(Contact(lastname='test'))
