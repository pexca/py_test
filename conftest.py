import pytest
from fixture.appl import Application
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):  # загрузка кофигурационного файла для фикстур
    global target
    if target is None:
        #  путь к конфигурационному файлу
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:  # переменная f указывает на объект, который указывает на открытый файл
            target = json.load(f)
    return target


@pytest.fixture  # инициализация и проверка работоспособности фикстуры
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    web_config = load_config(request.config.getoption('--target'))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config["username"], password=web_config['password'])
    return fixture


@pytest.fixture(scope='session')  # метод инициализации фикстуры для работы с ДБ
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    db_fixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])

    def fin():
        db_fixture.demolish()  # finalize
    request.addfinalizer(fin)
    return db_fixture


@pytest.fixture(scope="session", autouse=True)  # создание фикстуры для финализации
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.demolish()
    request.addfinalizer(fin)
    return fixture

# autouse=True - параметр автоматического србатывания фикстуры, если она нигде не указана


@pytest.fixture
def check_ui(request):
    return request.config.getoption('--check_ui')


def pytest_addoption(parser):  # запуск тестов с передачей параметров из командной строки
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default="target.json")
    parser.addoption('--check_ui', action='store_true')


def pytest_generate_tests(metafunc):  # via 'metafunc' object code can receive complete test-function info
    for fixture in metafunc.fixturenames:
        if fixture.startswith('data_'):
            test_data = load_from_module(fixture[5:])  # загружаем тестовые данные из фикстуры, имя кот.нач. с data
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith('json_'):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_module(module):
    return importlib.import_module('data.%s' % module).test_data  # импортируем модуль и берём из него test_data


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/%s.json' % file)) as f:
        return jsonpickle.decode(f.read())  # перекодируем в набор объектов Python


