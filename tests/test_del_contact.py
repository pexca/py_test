from model.contact import Contact


def test_del_fstcontact(app):
    if app.contact.count() == 0:
        app.contact.create_new_(Contact(firstname='test'))
    old_conts = app.contact.get_conts_lst()
    app.contact.del_fstcontact()
    new_conts = app.contact.get_conts_lst()
    assert len(old_conts)-1 == app.contact.count()
    old_conts[0:1] = []
    assert old_conts == new_conts

