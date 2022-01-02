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

        if not isinstance(other, Bank) or list(self.get_info().keys()) != list(self.get_info().keys()):
            raise TypeError('Objects must be the same')

        temp_bank = Bank.change()
        for coin in coins:
            temp_bank[coin].set(other.get_info()[coin].get_qty() + self.get_info()[coin].get_qty())
        return temp_bank

    def __eq__(self, other) -> bool:
        """Metoda porównuje dwa obiekty banku"""

        if list(self.get_info().keys()) != list(self.get_info().keys()):
            raise TypeError('Objects must be the same')

        for coin in coins:
            if self.get_info()[coin].get_qty() != other.get_info()[coin].get_qty():
                return False
        return True

    @classmethod
    def change(cls, qty=0):
        """Metoda odpowiedzialna za przypisanie ilości danej waluty, domyślnie resetuje"""

        return cls([
            Money(coin, qty) for coin in coins
        ])

    def set(self, coin: (int, float), qty: int) -> None:
        """Metoda dodaje monety do odpowiednich miejsc"""

        if not isinstance(coin, (int, float)):
            raise ValueError('COIN must be an int for a float')

        self.get_info()[coin].set(qty)

    def load(self, money: Money) -> None:
        """Metoda, która dodaje monety"""

        if not isinstance(money, Money):
            raise ValueError('MONEY must be a Money type')

        self.get_info()[money.get_float_val()].set_qty(money.get_qty())

    def get_amount(self) -> float:
        """Metoda zwraca sumę wszystkich monet w banku"""

        amount = 0.0
        for coin in self.get_info().values():
            amount += coin.get_sum_float_val()

        return amount


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
