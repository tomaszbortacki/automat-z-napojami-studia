from core import Items
from helpers import WrongProductError


class Product(Items):
    """
        Przechowuje następujące informacje o produkcie:
        - nazwa
        - cena
        - ilość
    """

    def __init__(self, name: str, price: float, qty=5, pre=2):
        if not isinstance(name, str):
            raise TypeError('NAME need to be a string')

        if not isinstance(price, float):
            raise TypeError('PRICE need to be a float')

        if not name or not price:
            raise ValueError('NAME and PRICE cannot be empty')

        self.__name = name
        super().__init__(price, qty, pre)

    def get(self, qty):
        """Metoda zwraca podaną ilość produktów"""

        if qty > self.get_qty():
            raise WrongProductError('Not enough products')

        self.__qty -= qty

        return Product(self.__name, self.__val, qty)
