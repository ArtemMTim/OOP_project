import pytest

from src.class_iterator import Iterator


def test_iterator(category_1):
    iterator_cat = Iterator(category_1)
    assert str(next(iterator_cat)) == "Холодильник, 30000 руб. Остаток: 5 шт."
    assert str(next(iterator_cat)) == "Плита, 10000 руб. Остаток: 10 шт."
    assert str(next(iterator_cat)) == "СВЧ, 5000 руб. Остаток: 15 шт."

    with pytest.raises(StopIteration):
        next(iterator_cat)
