from src.product import Product


def test_product_init(product_1):
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
