import pytest
from fixture.appl import Application


@pytest.fixture(scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.demolish)
    return fixture