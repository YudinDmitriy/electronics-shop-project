import pytest

from src.phone import *


@pytest.fixture
def item_phone():
    return Phone("iPhone 14", 120000, 5, 3)


def test_number_of_sim(item_phone):
    assert item_phone.number_of_sim == 3


def test_repr(item_phone):
    assert repr(item_phone) == "Phone('iPhone 14', 120000, 5, 3)"
