import pytest
from fixture.appl import Application

fixture = None


@pytest.fixture  # инициализация и проверка работоспособности фикстуры
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    elif not fixture.is_valid():
        fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)  # создание фикстуры для финализации
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.demolish()
    request.addfinalizer(fin)
    return fixture

# autouse=True - параметр автоматического србатывания фикстуры, если она нигде не указана
