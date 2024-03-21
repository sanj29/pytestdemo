import pytest


# using pytest.mark.parametrize we can pass multiple values to our test cases
# used tuple to provide values to your test, based number of parameter test execution will occur.
@pytest.mark.parametrize("a,b,final", [(2, 6, 8), (5, 8, 15), (10, 5, 15)])
def test_sum(a, b, final):
    assert a + b == final, " some is incorrect"
