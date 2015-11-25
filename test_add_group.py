# -*- coding: utf-8 -*-

from group import Group
from appl import Application
import pytest

# метка инициализатора фикстуры
@pytest.fixture
def app(request):  # инициализировать фикстуру
    fixture = Application()
    request.addfinalizer(fixture.demolish)  # метод параметра request, разрушающий фикстуру
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="qwerty", header="qwerty", footer="qwerty"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()