import pytest
from fixture.appl import Application

fixture = None


@pytest.fixture  # инициализация и проверка работоспособности фикстуры
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption('--baseUrl')
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    elif not fixture.is_valid():
        fixture = Application(browser=browser, base_url=base_url)
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


def pytest_addoption(parser):  # запуск тестов с передачей параметров из командной строки
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--baseUrl', action='store', default="http://localhost/addressbook/")