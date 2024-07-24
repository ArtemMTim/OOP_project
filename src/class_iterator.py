class Iterator:
    """Класс описывает итератор, возвращающий вакансии из спсика вакансий"""

    def __init__(self, cat_object):
        self.cat_object = cat_object
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.cat_object.products_list):
            prod = self.cat_object.products_list[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration
