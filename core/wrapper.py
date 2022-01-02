from core import Items


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

    def get(self, one_type: str, qty: int):
        """Metoda zwraca dany przedmiot"""

        return self.__info[one_type].take(qty)

    def set(self, one_type: str, qty: int):
        """Metoda abstrakcyjna zakłada dodanie danej ilości przedmiotów do danego typu danych"""

        raise NotImplementedError('Method (set) is not implemented')

