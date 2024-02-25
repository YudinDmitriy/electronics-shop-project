import pytest

from src.keyboard import *


@pytest.fixture
def item_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(item_keyboard):
    item_keyboard.change_lang()
    assert str(item_keyboard.language) == "RU"
    item_keyboard.change_lang()
    assert str(item_keyboard.language) == "EN"
