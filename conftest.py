import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", default="https://ya.ru", help="This is request url you want to test"
    )
    parser.addoption(
        "--status_code", default=200, type=int, help="This is status_code you are waiting for"
    )


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def status_code(request):
    return request.config.getoption("--status_code")


# def pytest_addoption(parser):
#     parser.addoption("--browser_name", action='store', default=None,
#                      help="Choose browser: chrome or firefox")
#
#
# @pytest.fixture(scope="function")
# def fi(request):
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
