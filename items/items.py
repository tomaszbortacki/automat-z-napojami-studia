class Items:
    """
        Klasa, która przechowuje informacje o produktach, które mają takie same cechy,
        zwłaszcza informacje o wartościach dla pojedyńczych przedmiotow
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

    def get(self, qty: int):
        """Metoda abstrakcyjna. Zwraca ilość rzeczy"""

        raise NotImplementedError('Method (get) is not implemented')

    def get_qty(self) -> int:
        """Metoda zwraca ilość rzeczy"""

        return self.__qty

    def get_int_val(self) -> int:
        """Metoda zwraca wartość danej rzeczy w postaci int."""

        return self.__val

    def get_float_val(self) -> float:
        """Metoda zwraca wartość danej rzeczy w postaci zmiennoprzecinkowej"""

        return self.__val / 10 ** self.__pre

    def get_sum_int_val(self) -> int:
        """Zwraca całkowitą dokładną wartość przemiotów w jednostce przechowywania."""

        return self.__qty * self.__val

    def get_sum_float_val(self) -> float:
        """Metoda zwraca wszystkie rzeczy w postaci zmienno przecinkowej"""

        return self.__qty * self.__val / 10 ** self.__pre

    def get_formatted_val(self) -> str:
        """Metoda zwraca wartość jednej rzeczy w postaci stringa z precyzją"""

        return ("{:." + str(self.__pre) + "f}").format(self.get_float_val())

    def get_formatted_sum_val(self) -> str:
        """Metoda zwraca wartość wszystkich rzeczy w postaci stringa z precyzją"""

        return ("{:." + str(self.__pre) + "f}").format(self.get_sum_float_val())

if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass