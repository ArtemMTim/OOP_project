class MixinLog:
    """Класс_миксин при создании объекта выводит в консоль информацию, от какого класса
    и с какими параметрами создан объект."""

    def __init__(self):
        self.__repr__()

    def __repr__(self):
        print(f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})")
