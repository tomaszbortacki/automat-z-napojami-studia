from money import Money
from utils import coins
from wrapper import Wrapper


class Bank(Wrapper):
    def __init__(self, money):
        self.__coins = coins
        self.__coins.sort(reverse=True)
        super().__init__(self.__coins, money)

    def __add__(self, other):
        """Metoda, która dodaje dwa obiekty do siebie"""

        if not isinstance(other, Bank) or list(self.__info.keys()) != list(self.__info.keys()):
            raise TypeError('Objects must be the same')

        temp_bank = Bank.change()
        for coin in coins:
            temp_bank[coin].set(other.__info[coin].get_qty() + self.__info[coin].get_qty())
        return temp_bank

    def __eq__(self, other):
        """Metoda porównuje dwa obiekty banku"""

        if list(self.__info.keys()) != list(self.__info.keys()):
            raise TypeError('Objects must be the same')

        for coin in coins:
            if self.__info[coin].get_qty() != other.__info[coin].get_qty():
                return False
        return True

    @classmethod
    def change(cls, qty=0):
        """Metoda odpowiedzialna za przypisanie ilości danej waluty, domyślnie resetuje"""

        return cls([
            Money(coin, qty) for coin in coins
        ])

    def set(self, coin: (int, float), qty, int):
        """Metoda dodaje monety do odpowiednich miejsc"""

        if not isinstance(coin, (int, float)):
            raise ValueError('COIN must be an int for a float')


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
