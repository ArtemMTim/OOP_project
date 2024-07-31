from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый класс описания продукта."""

    @classmethod
    @abstractmethod
    def new_product(cls, kwargs):
        pass
