class Items:
    """
        Klasa, która przechowuje informacje o produktach, które mają takie same cechy,
        zwłaszcza informacje o wartościach dla pojedynczych przedmiotów
    """

    def __init__(self, val: (int, float), qty=1, pre=2):
        if not isinstance(qty, int) or not isinstance(pre, int):
            raise TypeError('QTY and PRE needs to be int type')

        if not isinstance(val, (int, float)):
            raise TypeError('VAL must be int or float type')

        if qty < 0:
            raise ValueError('QTY cannot be negative number')

        self.__val = int(round(val * 10 ** pre))
        self.__qty = qty
        self.__pre = pre

    def set_qty(self, add_qty) -> None:
        """Metoda dodaje odpowiednia ilość monet"""

        if add_qty < 0:
            raise ValueError('QTY cannot be negative')

        self.__qty += add_qty

    def get(self, qty: int):
        """Metoda abstrakcyjna. Zwraca ilość rzeczy"""

        raise NotImplementedError('Method (get) is not implemented')

    def get_qty(self) -> int:
        """Metoda zwraca ilość rzeczy"""

        return self.__qty

    def get_float_val(self) -> float:
        """Metoda zwraca wartość danej rzeczy w postaci zmiennoprzecinkowej"""

        return self.__val / 10 ** self.__pre

    def get_sum_float_val(self) -> float:
        """Metoda zwraca wszystkie rzeczy w postaci zmiennoprzecinkowej"""

        return self.__qty * self.__val / 10 ** self.__pre


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
