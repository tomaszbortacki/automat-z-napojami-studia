from tkinter import NORMAL, DISABLED, Button
from helpers import statics

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


def set_proper_coin(coin: float) -> str:
    """Metoda odpowiedzialna za przpisanie poprawnych nazw do monet"""

    if coin >= 1:
        return str(coin) + ' zł'
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
