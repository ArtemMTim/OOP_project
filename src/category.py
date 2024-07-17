from src.product import Product


class Category:
    """Класс представления категории продуктов."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.products)

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price}. Остаток: {product.quantity}шт.\n"
        return products_str

    @property
    def products_list(self):
        return self.__products

    def add_product(self, product: Product):
        for item in self.__products:
            if item.name == product.name:
                item.quantity += product.quantity
                if item.price < product.price:
                    item.price = product.price
                return
        self.__products.append(product)
        Category.product_count += 1
