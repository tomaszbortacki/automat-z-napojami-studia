from assortment import Assortment
from bank import Bank
from exceptions import WrongProductError, WrongMoneyError
from money import Money
from utils import price_generator, coins


class Core:
    def __init__(self, products):
        self.__assortment = Assortment(products, 30)
        self.__product_number = 0
        self.__product_price = 0
        self.__bank = Bank.change(50)
        self.__bank_temp = Bank.change()

    @classmethod
    def init(cls, rng: range, qty=5):
        """Metoda, która generuje podstawową ilość produktów o podanej ilości (Domyślnie 5)"""

        return cls([
            product for product in price_generator(rng, qty)
        ])

    def get_product_price(self, number: int) -> str:
        """Metoda wyszukuje produktu o podanym id oraz zwraca jego cene"""

        if not isinstance(number, int):
            raise ValueError('ID must be an int')

        if not 30 <= number <= 50:
            raise WrongProductError('Nie ma takiego produktu')

        self.__product_number = number
        self.__product_price = self.__assortment.get_price(number)

        return "{:.2f}".format(self.__product_price)

    def pay(self, coin: float) -> None:
        """Metoda odpowiedzialna za placenie"""

        if not isinstance(coin, (int, float)) or coin not in coins:
            raise WrongMoneyError('Nie ma takiej waluty')

        self.__bank_temp.load(Money(coin, 1))

    def clear(self):
        self.__product_number = 0
        self.__product_price = 0

    def get_money(self) -> float:
        """Metoda zwraca wartość wrzuconych monet"""

        return self.__bank_temp.get_amount()


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
