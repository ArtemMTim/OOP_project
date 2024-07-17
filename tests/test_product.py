def test_product_init(product_1):
    assert product_1.name == "Холодильник"
    assert product_1.description == "Холодильник LG"
    assert product_1.price == 30000
    assert product_1.quantity == 5
