import unittest

from core import Core
from exceptions import EmptyProductError, WrongProductError
from product import Product


class Tests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.__products = [
            Product('Produkt 1', 9.90, 1)
        ]
        super().__init__(*args, **kwargs)

    def test_1(self):
        """Sprawdzenie ceny jednego towaru - oczekiwana informacja o cenie."""

        core = Core(self.__products)
        self.assertEqual(core.get_product_price(30), '9.90')

    def test_2(self):
        """Wrzucenie odliczonej kwoty, zakup towaru - oczekiwany brak reszty."""

        core = Core(self.__products)
        core.get_product_price(30)
        core.pay(5)
        core.pay(2)
        core.pay(2)
        core.pay(0.5)
        core.pay(0.2)
        # Jeżeli płatność osiągnie cenę produktu, to akceptuje transakcję i wydaje resztę, jeżeli takowa jest
        info = core.pay(0.2)

        # Metoda u mnie zwraca string'a i jeżeli zawiera on samą nazwę produktu, to znaczy, że nie ma reszty
        self.assertEqual(info, 'Wydano: Produkt 1')

    def test_3(self):
        """Wrzucenie większej kwoty, zakup towaru - oczekiwana reszta."""

        core = Core(self.__products)
        core.get_product_price(30)
        core.pay(5)
        info = core.pay(5)

        self.assertEqual(info, 'Wydano: Produkt 1\nZwrócono monetę o nominale: 10 gr w ilości: 1\n')

    def test_4(self):
        """Wykupienie całego asortymentu, próba zakupu po wyczerpaniu towaru - oczekiwana informacja o braku."""

        core = Core(self.__products)
        core.get_product_price(30)
        core.pay(5)
        info = core.pay(5)
        core.clear(5)
        # Sprawdzenie, czy pierwszy produkt został wydany
        self.assertEqual(info, 'Wydano: Produkt 1\nZwrócono monetę o nominale: 10 gr w ilości: 1\n')

        core.get_product_price(30)
        core.pay(5)
        with self.assertRaises(EmptyProductError):
            core.pay(5)  # Wyrzuci błąd o braku produkty

    def test_5(self):
        """Sprawdzenie ceny towaru o nieprawidłowym numerze (<30 lub >50) - oczekiwana informacja o błędzie."""

        core = Core(self.__products)
        with self.assertRaises(WrongProductError):
            self.assertEqual(core.get_product_price(25), '9.90')

    def test_6(self):
        """Wrzucenie kilku monet, przerwanie transakcji - oczekiwany zwrot monet."""

        core = Core(self.__products)
        core.get_product_price(30)
        core.pay(0.1)
        core.pay(0.1)
        core.pay(0.1)
        rest = core.clear()

        self.assertEqual(rest, 'Zwrócono monetę o nominale: 10 gr w ilości: 3\n')

    def test_7(self):
        """
            Wrzucenie za małej kwoty, wybranie poprawnego numeru towaru,
            wrzucenie reszty monet do odliczonej kwoty, ponowne wybranie poprawnego numeru towaru
            - oczekiwany brak reszty
        """

        core = Core(self.__products)
        core.pay(5)
        core.pay(2)
        core.pay(2)
        core.get_product_price(30)
        core.pay(0.5)
        core.pay(0.2)
        info = core.pay(0.2)

        self.assertEqual(info, 'Wydano: Produkt 1')  # Brak reszty

    def test_8(self):
        """
            Zakup towaru płacąc po 1 gr - suma stu monet ma być równa 1zł
            (dla floatów suma sto razy 0.01+0.01+...+0.01 nie będzie równa 1.0).
            Płatności można dokonać za pomocą pętli for w interpreterze.
        """

        core = Core(self.__products)
        core.get_product_price(30)
        for i in range(989):  # W pętli obracamy 9.89zł
            core.pay(0.01)

        rest = core.pay(0.01)  # Ostatni grosz zwraca produkt

        self.assertEqual(rest, 'Wydano: Produkt 1')  # Bez reszty
