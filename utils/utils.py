import random
from tkinter import NORMAL, DISABLED, Button, messagebox
from utils import statics
from product import Product

coins: list[float] = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]  # Nominały


def set_proper_text(number: int) -> str:
    """Metoda odpowiedzialna za przypisanie poprawnych nazw dla przycisków wyboru"""

    if number == 9:
        return statics['button_clear_text']
    elif number == 10:
        return '0'
    elif number == 11:
        return statics['button_accept_text']
    else:
        return str(number + 1)


def set_proper_coin(coin: (int, float)) -> str:
    """Metoda odpowiedzialna za przpisanie poprawnych nazw do monet"""

    if coin >= 1:
        return (str(int(coin)) if isinstance(coin, int) or coin.is_integer() else "{:.2f}".format(coin)) + ' zł'
    else:
        return str(int(coin * 100)) + ' gr'


def change_buttons_state(buttons: list[Button], button_state: bool) -> None:
    """Metoda odpowiedzialna za włączanie i wyłączanie przyciskow"""

    for button in buttons:
        if button['text'] != statics['button_clear_text'] and button['text'] != statics['button_accept_text']:
            button.config(
                state=NORMAL if button_state else DISABLED,
                bg=statics['button_color'] if button_state else statics['button_color_disabled']
            )


def show_error(error) -> None:
    messagebox.showerror('Error', error)


def price_generator(rng: range, qty=5):
    """Metoda generuje losowe ceny dla produtów z danego przedzialu oraz ustawia ich ilość (Domyślnie 5)"""

    for idx in rng:
        rand = random.randrange(100, 1000, qty) / 100
        yield Product('Produkt ' + str(idx), rand, qty)


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
