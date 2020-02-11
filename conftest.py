import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def fi(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
