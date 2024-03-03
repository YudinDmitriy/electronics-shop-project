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


def test_name(item_smartph):
    assert item_smartph.name == 'Смартфон'
    item_smartph.name = 'СуперСмартфон'
    assert item_smartph.name == 'СуперСмарт'


def test_string_to_number(item_smartph):
    assert item_smartph.string_to_number('7') == 7
    assert item_smartph.string_to_number('7.0') == 7
    assert item_smartph.string_to_number('8.0') == 8


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_file_not_found_error():
    with pytest.raises(FileNotFoundError, match='Отсутствует файл item.csv'):
        Item.instantiate_from_csv('../src/item.csv')

