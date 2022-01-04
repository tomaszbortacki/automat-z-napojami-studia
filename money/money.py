from items import Items


class Money(Items):
    """
        Klasa przechowuje informacje o ilość monet o różnej wartości
    """

    def __init__(self, coin: float, qty: int, pre=2, curr='PLN'):
        self.__curr = curr
        super().__init__(coin, qty, pre)

    def set(self, qty: int):
        """Metoda ustawia ilość monet"""

        if not isinstance(qty, int):
            raise TypeError("QTY must be a float")

        if qty > self.get_qty():
            qty = self.get_qty()

        self.set_qty(qty)

    def get(self, qty: int):
        """Metoda zwraca ilość monet"""

        if not isinstance(qty, int):
            raise TypeError("QTY must be a float")

        if qty > self.get_qty():
            qty = self.get_qty()

        self.set_qty(-qty)
        return Money(self.get_float_val(), qty)


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
