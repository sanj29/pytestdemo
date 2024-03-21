import pytest


# using pytest.fixture(params["a","b"]this will case multiple invocation of the fixture functions.
# you have to use request object as parameter in your method, and use this parametrize method name need to paas to your test case.
@pytest.fixture(params=["a", "b"])
def demo_fixture(request):
    print(request.param)


def test_param(demo_fixture):
    print("printing values")
