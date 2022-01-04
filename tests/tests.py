import unittest

from core import Core
from product import Product


class Tests(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.__products = [
            Product('Produkt 1', 7.50, 5)
        ]
        super().__init__(*args, **kwargs)

    def test_1(self):
        """Sprawdzenie ceny jednego towaru - oczekiwana informacja o cenie."""

        core = Core(self.__products)
        self.assertEqual(core.get_product_price(30), '7.50')

    # def test_2(self):
    #     """Wrzucenie odliczonej kwoty, zakup towaru - oczekiwany brak reszty."""
    #
    # def test_3(self):
    #     """Wrzucenie większej kwoty, zakup towaru - oczekiwana reszta."""
    #
    # def test_4(self):
    #     """Wykupienie całego asortymentu, próba zakupu po wyczerpaniu towaru - oczekiwana informacja o braku."""
    #
    # def test_5(self):
    #     """Sprawdzenie ceny towaru o nieprawidłowym numerze (<30 lub >50) - oczekiwana informacja o błędzie."""
    #
    # def test_6(self):
    #     """Wrzucenie kilku monet, przerwanie transakcji - oczekiwany zwrot monet."""
    #
    # def test_7(self):
    #     """
    #         Wrzucenie za małej kwoty, wybranie poprawnego numeru towaru,
    #         wrzucenie reszty monet do odliczonej kwoty, ponowne wybranie poprawnego numeru towaru
    #     """
    #
    # def test_8(self):
    #     """Oczekiwany brak reszty."""
    #
    # def test_9(self):
    #     """"""
    #
    # def test_10(self):
    #     """
    #         Zakup towaru płacąc po 1 gr - suma stu monet ma być równa 1zł
    #         (dla floatów suma sto razy 0.01+0.01+...+0.01 nie będzie równa 1.0).
    #         Płatności można dokonać za pomocą pętli for w interpreterze.
    #     """