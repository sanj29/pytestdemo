# **Pytest**
pytest requires: Python 3.8+ or PyPy3.

Run the following command in your command line:
- ``` pip install -U pytest ```

Check that you installed the correct version:
```
  $ pytest --version
    pytest 8.1.1
  ```
  
# **Test Grouping**
Using marker we can group our test like 
  @pytest.mark.smoke
  @pytest.mark.skip
  @pytest.mark.xfail
  
**Execution**: 
```pytest -m  somke "it will run a test cases matching given mark" tag test using @pytest.mark.smoke/sanity/regression```
  
# **Parametrization** 

- pytest enables test parametrization at several levels:
-pytest.fixture() allows one to parametrize fixture functions.
- @pytest.mark.parametrize allows one to define multiple sets of arguments and fixtures at the test function or class.
- pytest_generate_tests allows one to define custom parametrization schemes or extensions.


``` 
#using pytest.fixture(params["a","b"]this will case multiple invocation of the fixture functions.
#you have to use request object as parameter in your method, and use this parametrize method name need to paas to your test case.
@pytest.fixture(params=["a", "b"])
def demo_fixture(request):
    print(request.param)


def test_param(demo_fixture):
    print("printing values")

import pytest
#using pytest.mark.parametrize we can pass multiple values to our test cases
#used tuple to provide values to your test, based number of parameter test execution will occur.
@pytest.mark.parametrize("a,b,final", [(2, 6, 8), (5, 8, 15), (10, 5, 15)])
def test_sum(a, b, final):
    assert a + b == final, " some is incorrect"


#Here browser is used  to take decision and launch specific browser based on input value.
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


#allows one to define custom parametrization schemes or extensions
#here we have added command line option for pytest to understand --browser and take value as chrome or FF
def pytest_addoption(parser):
    parser.addoption("--browser")


#this browser method will return the actual vaue to our setup tc_setup method
#ref:: https://docs.pytest.org/en/latest/how-to/parametrize.html#pytest-generate-tests
@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

```
