from tkinter import NORMAL, DISABLED, Button, messagebox
from utils import statics

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
    """Metoda odpowiedzialna za przypisanie poprawnych nazw do monet"""

    if coin >= 1:
        return (str(int(coin)) if isinstance(coin, int) or coin.is_integer() else "{:.2f}".format(coin)) + ' zł'
    else:
        return str(int(coin * 100)) + ' gr'


def change_buttons_state(buttons: list[Button], button_state: bool) -> None:
    """Metoda odpowiedzialna za włączanie i wyłączanie przycisków"""

    for button in buttons:
        if button['text'] != statics['button_clear_text']:
            button.config(
                state=NORMAL if button_state else DISABLED,
                bg=statics['button_color'] if button_state else statics['button_color_disabled'],
                cursor='hand2' if button_state else ''
            )


def show_info(info) -> None:
    """Metoda wyświetla informacje"""

    messagebox.showinfo('Info', info)


def show_error(error) -> None:
    """Metoda wyświetla błędy"""

    messagebox.showerror('Error', error)


def multipy(number: (int, float)) -> (int, float):
    """Metoda za pomocą lambdy zwraca wartość z potęgą"""

    if not isinstance(number, (int, float)):
        print('NUMBER must be an int for a float')

    return lambda x: x ** number


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
