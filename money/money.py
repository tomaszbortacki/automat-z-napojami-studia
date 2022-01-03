from items import Items


class Money(Items):
    """
        Klasa przechowuje informacje o ilość monet o różnej wartości
    """

    def __init__(self, coin: float, qty: int, pre=2, curr='PLN'):
        self.__curr = curr
        super().__init__(coin, qty, pre)

    def get(self, qty):
        """Metoda zwraca ilość monet"""

        if qty > self.get_qty():
            qty = self.get_qty()

        self.__qty -= qty
        return Money(self.get_float_val(), qty)


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
