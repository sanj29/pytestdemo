import pytest


# Here browser is used  to take decision and launch specific browser based on input value.
@pytest.fixture(scope="session", autouse=True)
def testcase_setup(browser):
    if browser == "chrome":
        print("Launch Chrome")
    elif browser == "ff":
        print("Launch firefox")
    else:
        print("provide correct browser")
    print("Login to app")
    print("Browse Product")
    yield
    print("\nLog off from app")
    print("Close Browse")


# allows one to define custom parametrization schemes or extensions
# here we have added command line option for pytest to understand --browser and take value as chrome or FF
def pytest_addoption(parser):
    parser.addoption("--browser")


# this browser method will return the actual vaue to our setup tc_setup method
# ref:: https://docs.pytest.org/en/latest/how-to/parametrize.html#pytest-generate-tests
@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
