import pytest
from fixture.appl import Application
import json
import os.path
import importlib
import jsonpickle

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


def pytest_generate_tests(metafunc):  # via 'metafunc' object code can receive complete test-function info
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith('json_'):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_module(module):
    return importlib.import_module('data.%s' % module).test_data


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/%s.json' % file)) as f:
        return jsonpickle.decode(f.read())

