# **Pytest**
Pytest is a powerful and flexible testing framework that makes it easy to write, organize, and run tests for Python projects of any size. Its simplicity and extensibility have made it a popular choice for testing within the Python community pytest requires: Python 3.8+ or PyPy3.

To install run the below command in command line:
- ``` pip install -U pytest ```

Check that you installed the correct version:
```
  $ pytest --version
    pytest 8.1.1
  ```

**Sample test** 
```
def test_loign_case():
    print("Login successfully ...")


def test_logoff_case():
    print("log off successfully ...")


def test_calculation_case():
    assert 2 + 2 == 4
```
- To run abive code, go to your file location via cli and execute below command
``` pytest -vs ```
*** Running test ***
  - Torun all the test cases preent in the folder
  - ``` pytest ```
- To run test will extra information
  ``` pytest -vs ```
- To run based on some key-words use -k option
  ```pytest -vsk test_add*```

# **Test Grouping**

Sometimes  we need to group our test cases like smoke, sanity, and regression. So, using marker we can group our test like 
  - @pytest.mark.smoke
  - @pytest.mark.skip
  - @pytest.mark.xfail

**Sample code:**
  ```
@pytest.mark.smoke
def test_checkout_one_item_case():
    print("1 item checked-out  successfully ...")


def test_checkout_two_item_case():
    print("two item checked-out  successfully ...")


@pytest.mark.smoke
def test_checkout_all_item_case():
    print("all item checked-out  successfully ...")
```
**Execution**: 
```pytest -m  somke "it will run a test cases matching given mark" tag test using @pytest.mark.smoke/sanity/regression```

# **Using Fixture and Conftest.py** 

**pytest.fixture** is a decorator provided by the pytest framework for writing and managing setup code for tests. It allows you to define setup actions that need to be performed before executing one or more tests, and optionally, teardown actions that need to be performed after the test has completed. This helps in creating clean and maintainable test code by separating setup and teardown logic from the actual test functions.

**Here's how pytest.fixture works:**

**Definition**: You define a fixture function using the @pytest.fixture decorator. This function encapsulates the setup logic needed for your tests.

Usage: You can use the fixture function by passing it as an argument to other test functions. When a test function uses a fixture function as an argument, pytest automatically calls the fixture function and passes its return value to the test function.

**Execution**: The fixture function is executed before the test function that depends on it. If multiple test functions depend on the same fixture function, the fixture function is only executed once, and its result is cached for subsequent use.

**Teardown**: Optionally, you can define teardown logic within the fixture function using a yield statement. Any code after the yield statement serves as teardown code and is executed after the dependent test function completes execution. This ensures proper cleanup of resources used during setup.

Here's an example to illustrate the usage of pytest.fixture:
```
@pytest.fixture(scope="package", autouse=True)
def tc_setup():
    print("\nLaunch browser")
    print("Login to app")
    print("Browse Product")
    yield
    print("\nLog off from app")
    print("Close Browse")

# Test function that depends on the tc_setup fixture
def test_app_login(tc_setup):
    assert 2+3 > 0
```

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
