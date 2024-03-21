import pytest


@pytest.mark.smoke
def test_checkout_one_item_case():
    print("1 item checked-out  successfully ...")


def test_checkout_two_item_case():
    print("two item checked-out  successfully ...")


@pytest.mark.smoke
def test_checkout_all_item_case():
    print("all item checked-out  successfully ...")
