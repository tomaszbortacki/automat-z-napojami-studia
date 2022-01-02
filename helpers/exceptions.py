class RestError(Exception):
    """Wyjątek - Nie można wydać reszty"""

    def __init__(self, *args: object) -> None:
        super(self).__init__(*args)


class MoneyError(Exception):
    """Wyjątek - brak wydania danej ilości monet"""

    def __init__(self, *args: object) -> None:
        super(self).__init__(*args)


class EmptyProductError(Exception):
    """Wyjatek - Produkt się skończył"""

    def __init__(self, *args: object) -> None:
        super(self).__init__(*args)


class PaymentError(Exception):
    """Wyjątek - niewystarczająca zaplata"""

    def __init__(self, *args: object) -> None:
        super(self).__init__(*args)
