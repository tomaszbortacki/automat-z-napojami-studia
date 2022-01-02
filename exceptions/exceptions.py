class RestError(Exception):
    """Wyjątek - Nie można wydać reszty"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class MoneyError(Exception):
    """Wyjątek - brak wydania danej ilości monet"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class EmptyProductError(Exception):
    """Wyjatek - Produkt się skończył"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PaymentError(Exception):
    """Wyjątek - niewystarczająca zaplata"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class WrongProductError(Exception):
    """Wyjatek - Nie ma takiego produktu"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class WrongMoneyError(Exception):
    """Wyjatek - Nie ma takiej waluty"""

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
