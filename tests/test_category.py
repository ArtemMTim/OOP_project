import pytest


def test_category_init(category_1, category_2, category_3):
    assert category_1.name == "Бытовая техника"
    assert category_1.description == "Техника для дома и быта"
    assert len(category_1.products_list) == 3
    assert category_1.category_count == 3
    assert category_2.category_count == 3
    assert category_3.category_count == 3
    assert len(category_3.products_list) == 1


def test_category_str(category_3):
    assert category_3.products == "Насос, 3000 руб. Остаток: 25 шт.\n"


# Тестирование поиска аналогичного товара при добавлении товара в список по категории.
# При совпадении названий товара количество складывается, цена берётся большая.
def test_add_product(category_3, product_3):
    category_3.add_product(product_3)
    len(category_3.products_list) == 1
    for product in category_3.products_list:
        assert product.name == "Насос"
        assert product.price == 4000
        assert product.quantity == 50


def test_add_category_not_product(category_3, fake_product):
    with pytest.raises(TypeError):
        category_3.add_product(fake_product)


def test_str_category(category_1):
    assert str(category_1) == "Бытовая техника, количество продуктов: 30 шт."
