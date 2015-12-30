import pytest
from fixture.appl import Application
import json
import os.path

fixture = None
target = None


@pytest.fixture  # инициализация и проверка работоспособности фикстуры
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    if target is None:
        #  путь к конфигурационному файлу
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--target'))
        with open(config_file) as f:  # переменная f указывает на объект, который указывает на открытый файл
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target["username"], password=target['password'])
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
    parser.addoption('--target', action='store', default="target.json")
