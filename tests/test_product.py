import pytest

from src.product import Product


def test_product_init(product_1, capsys):
    assert product_1.name == "Холодильник"
    assert product_1.description == "Холодильник LG"
    assert product_1.price == 30000
    assert product_1.quantity == 5


def test_product_price(product_1, capsys):
    product_1.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product_1.price = 100000
    assert product_1.price == 100000


def test_new_product(product_2):
    product_new = Product.new_product(product_2)
    assert product_new.name == "Холодильник"
    assert product_new.description == "Холодильник LG"
    assert product_new.price == 30000
    assert product_new.quantity == 5


def test_add_product(product_1, product_3):
    assert product_1 + product_3 == 250000


def test_str_product(product_1):
    assert str(product_1) == "Холодильник, 30000 руб. Остаток: 5 шт."


def test_product_zero_quantity():
    with pytest.raises(ValueError):
        product = Product(name="Насос", description='Насос автомобильный "Силач 3000"', price=4000, quantity=0)
