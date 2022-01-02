from core import Product, Wrapper


class Assortment(Wrapper):
    """
        Klasa, która przechowuje informacje o produktach oraz ich ilości
    """

    def __init__(self, products: list, init_number = 30):
        if not isinstance(products, list) and not all(isinstance(product, Product) for product in products):
            raise TypeError("PRODUCTS needs to be Product type")

        if not isinstance(init_number, int):
            raise TypeError('INIT_NUMBER need to be int type')

        if init_number < 0:
            raise ValueError('INIT_NUMBER cannot be negative')

        super().__init__([
            i + init_number for i in range(len(products))  # List comprehension
        ], products)

    def __add__(self, other):
        raise NotImplementedError("Nie można dodać produktu")

    def get_price(self, id: int) -> float:
        """Metoda zwraca cenę produktu o podanym id"""

        return self.__info[id].get_float_val();

    def get_qty(self, id: int) -> bool:
        """Metoda zwraca informacje i stanie produktów o podanym id, czy przypadkiem się nie skończył"""

        return self.__info[id].get_qty() <= 0

    def set(self, one_type: str, qty: int):
        raise NotImplementedError("Nie można dodać produktu")
