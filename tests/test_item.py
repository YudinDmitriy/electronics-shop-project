"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import *

@pytest.fixture
def item_smartph():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price(item_smartph):
    assert item_smartph.calculate_total_price() == 200000

def test_apply_discount(item_smartph):
    Item.pay_rate = 0.5
    assert item_smartph.apply_discount() == 5000