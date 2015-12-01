# -*- coding: utf-8 -*-

import pytest
from fixture.appl import Application
from model.group import Group


# метка инициализатора фикстуры
@pytest.fixture
def app(request):  # инициализировать фикстуру
    fixture = Application()
    request.addfinalizer(fixture.demolish)  # метод параметра request, разрушающий фикстуру
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()