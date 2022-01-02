from tkinter import Tk, Label, StringVar, Button, messagebox
from tkinter.font import Font
from typing import Optional

from . import utils

DEFAULT_SCREEN_TEXT = 'Wybierz produkt (30 - 50)'


def set_proper_text(number: int) -> str:
    if number == 9:
        return 'CLS'
    elif number == 10:
        return '0'
    elif number == 11:
        return 'OK'
    else:
        return str(number + 1)


def set_proper_coin(coin: float) -> str:
    if coin >= 1:
        return str(coin) + ' zł'
    elif coin == 0.02:
        return str(int(coin * 100)) + ' grosze'
    elif coin == 0.01:
        return str(int(coin * 100)) + ' grosz'
    else:
        return str(int(coin * 100)) + ' groszy'


class Gui:
    def __init__(self) -> None:
        # Ekran
        self.__main = Tk()
        self.__main.title('Automat z napojami - Tomasz Bortacki - JS')
        self.__main.minsize(480, 640)

        # Wyświetlacz
        self.__default_font = Font(family="sans-serif", size=16, weight="bold")
        self.__screen: Optional[Label] = None
        self.__screen_text = StringVar()
        self.__screen_text.set(DEFAULT_SCREEN_TEXT)
        self.__screen_buttons: Optional[list[Button]] = None
        self.__screen_coins: Optional[list[Button]] = None
        self.__screen_current_number = ''

        # Dodanie designu i ekranu
        self.design()

        # Wywołanie pętli
        self.__main.mainloop()

    def design(self) -> None:
        # Ekran
        self.add_screen()

        # Przyciski
        self.add_buttons()

        # Monety
        self.add_coins()

        # Siatka ekranu
        self.__main.grid_columnconfigure(tuple(i for i in range(12)), weight=1)
        self.__main.grid_rowconfigure(tuple(i for i in range(9)), weight=1)

    def add_screen(self) -> None:
        self.__screen = Label(
            self.__main,
            font=self.__default_font,
            fg="#fff",
            bg="#2c3e50",
            textvariable=self.__screen_text,
            pady=32,
            padx=16
        )

        self.__screen.grid(column=0, row=0, columnspan=9, rowspan=5, sticky="nswe")

    def add_buttons(self) -> None:
        self.__screen_buttons = [
            Button(
                self.__main,
                text=set_proper_text(i),
                font=self.__default_font,
                fg="#fff",
                bg="#34495e",
                activeforeground='#fff',
                activebackground="#2c3e50",
                bd=0,
                command=lambda number=i + 1: self.choose_product(number),
                cursor="hand2"
            ).grid(
                row=i // 3 + 5,
                column=i % 3 * 3,
                columnspan=3,
                sticky="nswe"
            ) for i in range(12)
        ]

    def add_coins(self) -> None:
        self.__screen_coins = [
            Button(
                self.__main,
                text=set_proper_coin(coin),
                font=self.__default_font,
                fg="#fff",
                bg="#34495e",
                activeforeground='#fff',
                activebackground="#2c3e50",
                bd=0,
                cursor="hand2"
            ).grid(
                row=idx,
                column=9,
                columnspan=3,
                sticky="nswe"
            ) for idx, coin in enumerate(utils.coins)
        ]

    def choose_product(self, action_number: int) -> None:
        if action_number == 10:
            self.__screen_text.set(DEFAULT_SCREEN_TEXT)
            return
        elif action_number == 12:
            if not self.__screen_current_number:
                return

            number = int(self.__screen_current_number)

            if 30 <= number <= 50:
                messagebox.showinfo('Success', 'Podałeś poprawny number')
            else:
                messagebox.showerror('Error', 'Nie ma takiego produktu')
                self.__screen_current_number = ''
                self.__screen_text.set(DEFAULT_SCREEN_TEXT)

            return
        elif action_number == 11:
            action_number = 0

        if len(self.__screen_current_number) >= 2 or self.__screen_current_number.startswith('0'):
            self.__screen_current_number = str(action_number)
        else:
            self.__screen_current_number += str(action_number)

        self.__screen_text.set(self.__screen_current_number)


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
