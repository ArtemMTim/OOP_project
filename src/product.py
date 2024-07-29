class Product:
    """Класс представления продукта."""

    name: str
    description: str
    price: int | float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__price * self.quantity + other.__price * other.quantity
        else:
            raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_answer = input("Подтвердите снижение цены. Введите y/n: ")
            if user_answer == "y":
                self.__price = new_price
            elif user_answer == "n":
                self.__price = self.__price
        elif new_price > self.__price:
            self.__price = new_price

    @classmethod
    def new_product(cls, kwargs):
        return cls(**kwargs)
