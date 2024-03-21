import pytest


@pytest.mark.smoke
def test_loign_case():
    print("Login successfully ...")


@pytest.mark.skip
def test_logoff_case():
    print("log off successfully ...")


@pytest.mark.xfail
def test_calculation_case():
    assert 2 + 2 == 5
