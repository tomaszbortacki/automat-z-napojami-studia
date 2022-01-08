import math

from exceptions import MoneyError
from money import Money
from utils import coins, set_proper_coin
from wrapper import Wrapper


class Bank(Wrapper):
    """

    """
    def __init__(self, money):
        super().__init__(coins, money)

    def __add__(self, other):
        """Metoda, która dodaje dwa obiekty do siebie"""

        if not isinstance(other, Bank) or list(self.get_info().keys()) != list(self.get_info().keys()):
            raise TypeError('Objects must be the same')

        for coin in coins:
            self.get_info()[coin].set(other.get_info()[coin].get_qty())

        return self

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

    def get_rest(self) -> str:
        """Metoda zwraca wrzucone monety"""

        # string from list comprehension
        return ''.join(
            'Zwrócono monetę o nominale: ' + set_proper_coin(coin.get_float_val()) + ' w ilości: ' + str(
                coin.get_qty()) + '\n'
            if coin.get_qty() > 0 else ''
            for coin in self.get_info().values()
        )

    def get_diff(self, amount: (int, float)) -> (Money, int):
        """Metoda zwraca resztę"""

        if not isinstance(amount, (int, float)):
            raise TypeError('AMOUNT must be an int or a float')

        if amount < 0:
            raise ValueError("AMOUNT cannot be negative")

        if amount == 0:
            return 0

        amount = round(amount * 100)  # przeciwdziała floatowi, usuwa niepełne wartości typu: 10 miejsc po przecinku
        coin_id = 0
        rest = Bank.change()

        while amount > 0:
            if coin_id >= len(coins):
                raise MoneyError('Tylko odliczona kwota')

            coin = coins[coin_id]
            money = self.get_info()[coin].get(math.floor(amount / coin / 100))
            amount -= money.get_sum_int_val()
            coin_id += 1
            rest.load(money)

        return rest.get_rest()


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
