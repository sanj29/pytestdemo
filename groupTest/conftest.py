import pytest


@pytest.fixture(scope="package", autouse=True)
def tc_setup():
    print("\nLaunch browser")
    print("Login to app")
    print("Browse Product")
    yield
    print("\nLog off from app")
    print("Close Browse")