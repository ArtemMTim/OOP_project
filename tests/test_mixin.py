from src.product import Product
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass


def test_product_mixin(capsys):
    Product(name="Холодильник", description="Холодильник LG", price=30000, quantity=5)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Холодильник, Холодильник LG, 30000, 5)"


def test_smartphone_mixin(capsys):
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space, 210000.0, 8)"


def test_lawn_grass_mixin(capsys):
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)"
