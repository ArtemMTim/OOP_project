from src.product import Product


class Smartphone(Product):
    """Класс описывает смартфоны. Родительский класс - Product"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)
