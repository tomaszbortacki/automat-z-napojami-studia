from items import Items


class Wrapper:
    """
        Klasa przechowująca słownik przedmiotów z identyfikatorami,
        dzięki czemu mamy posegregowane przedmioty według ich rodzaju
    """

    def __init__(self, types: (list, tuple), items: (list, tuple)):
        if not isinstance(types, (list, tuple)) or not isinstance(items, (list, tuple)):
            raise ValueError("TYPES and ITEMS needs to be list or tuple")

        if len(types) != len(items):
            raise ValueError('TYPES and ITEMS needs to have the same length')

        if not all(isinstance(item, Items) for item in items):
            raise ValueError('Items can only have values from Item type')

        self.__info = {
            types[i]: items[i] for i in range(len(items))
        }

    def __add__(self, other):
        """Metoda abstrakcyjna zakłada dodanie dwóch obiektów, które dziedziczą z Wrapper'a w postaci Items"""

        raise NotImplementedError('Method (__add__) is not implemented')

    def remove(self, one_type: int, qty: int) -> None:
        """Metoda usuwa dany przedmiot"""

        self.__info[one_type].get(qty)

    def get_name(self, one_type: int) -> str:
        """Metoda zwraca nazwę produktu"""

        return self.__info[one_type].get_name()

    def get_info(self) -> dict:
        """Zwraca informacje, które są przechowywane w tym obiekcie"""

        return self.__info

    def get_price(self, number: int) -> float:
        """Metoda zwraca cenę przedmiotu o podanym id"""

        return self.__info[number].get_float_val()

    def set(self, one_type: str, qty: int):
        """Metoda abstrakcyjna zakłada dodanie danej ilości przedmiotów do danego typu danych"""

        raise NotImplementedError('Method (set) is not implemented')


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
