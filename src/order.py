from src.base_product_list import BaseProductList
from src.product import Product


class Order(BaseProductList):
    """Класс описывает заказ продуктов. В заказе может содержаться только один вид продуктов,
    возможно изменение количества единиц продукта в заказе. При попытке изменения либо добавления продукта поднимается ошибка.
    Выводит суммарную стоимость за единицы продукта в заказе. Родительский класс - BaseProductList."""

    product: Product
    quantity: int

    def __init__(self, product, quantity):
        self.__products = product
        self.__quantity = quantity
        self.__total_price = 0

    @property
    def products(self):
        return f"{self.__products.name}, {self.__products.description}"

    @products.setter
    def products(self, new_product):
        raise ValueError("Добавлять новый товар в уже созданный заказ невозможно!")

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity += new_quantity

    @property
    def total_price(self):
        self.__total_price = self.__quantity * self.__products.price
        return self.__total_price


if __name__ == "__main__":
    product = Product("Насос", 'Насос автомобильный "Силач 3000"', 3000, quantity=25)
    product2 = Product("Насос", 'Насос автомобильный "Силач 3000"', 3000, quantity=25)
    order = Order(product, 10)
    print(order.products)
    print(order.quantity)
    print(order.total_price)
    order.quantity = 15
    print(order.products)
    print(order.quantity)
    print(order.total_price)
