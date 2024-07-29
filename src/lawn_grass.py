from src.product import Product


class LawnGrass(Product):
    """Класс описывает газонную траву. Родительский класс - Product"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)
