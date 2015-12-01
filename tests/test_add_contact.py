# -*- coding: utf-8 -*-
import pytest
from fixture.appl import Application
from model.contact import Contact


# метка инициализатора фикстуры
@pytest.fixture
def app(request):  # инициализировать фикстуру
    fixture = Application()
    request.addfinalizer(fixture.demolish)  # метод параметра request, разрушающий фикстуру
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_(Contact(firstname="Alla", lastname="Frolova", email="pexca@rambler.ru"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new_(Contact(firstname="", lastname="", email=""))
    app.session.logout()
