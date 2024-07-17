def test_category_init(category_1, category_2, category_3):
    assert category_1.name == "Бытовая техника"
    assert category_1.description == "Техника для дома и быта"
    assert len(category_1.products) == 3
    assert category_1.category_count == 3
    assert category_2.category_count == 3
    assert category_3.category_count == 3
    assert category_1.product_count == 7
    assert category_2.product_count == 7
    assert category_3.product_count == 7
    assert len(category_3.products) == 1
