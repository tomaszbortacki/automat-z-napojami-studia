from tkinter import Tk, Label, StringVar, Button, messagebox, DISABLED, NORMAL
from tkinter.font import Font
from typing import Optional
from helpers import utils, statics, set_proper_text, set_proper_coin, change_buttons_state


class Gui:
    """
        Klasa Gui

        Odpowiada za rysowanie oraz interakcje użytkownika z automatem do napojów

        Za jej pomocą możemy wybrać produkt oraz wrzucić odpowiednie monety, tak aby otrzymać odpowiedniu produkt
    """

    def __init__(self) -> None:
        # Ekran
        self.__main = Tk()
        self.__main.title('Automat z napojami - Tomasz Bortacki - JS')
        self.__main.minsize(480, 640)

        # Wyświetlacz
        self.__default_font = Font(family="sans-serif", size=14, weight="bold")
        self.__screen: Optional[Label] = None
        self.__screen_text = StringVar()
        self.__screen_text.set(statics['default_text_screen'])
        self.__screen_buttons: Optional[list[Button]] = None
        self.__screen_coins: Optional[list[Button]] = None
        self.__screen_current_number = ''
        self.__screen_price: Optional[Label] = None
        self.__screen_price_text = StringVar()
        self.__screen_temp_label: Optional[Label] = None  # Rozpychacz - eliminuje skakanie ekranu

        # Dodanie designu i ekranu
        self.design()

        # Wywołanie pętli
        self.__main.mainloop()

    def design(self) -> None:
        """Metoda odpowiedzialna za wyświetlenie ekranu, przycisków oraz monet za pomocą tkinter'"""

        # Ekran
        self.add_screen()

        # Przyciski
        self.add_buttons()

        # Monety
        self.add_coins()
        change_buttons_state(self.__screen_coins, False)

        # Siatka ekranu
        self.__main.grid_columnconfigure(tuple(i for i in range(12)), weight=1)  # tuple Comprehension
        self.__main.grid_rowconfigure(tuple(i for i in range(9)), weight=1)  # tuple Comprehension

    def add_screen(self) -> None:
        """Metoda odpowiedzialna za dodanie ekranu"""

        # Rozpycha ekran przez co po zmianie teksty docelowego, przyciski nie zmieniają szerokości
        self.__screen_temp_label = Label(
            self.__main,
            font=self.__default_font,
            fg="#2c3e50",
            bg="#2c3e50",
            text='AAAAAAAAAAAAAAAAAAAA'
        )

        self.__screen = Label(
            self.__main,
            font=self.__default_font,
            fg="#fff",
            bg="#2c3e50",
            textvariable=self.__screen_text,
            pady=32,
            padx=16
        )

        self.__screen_price = Label(
            self.__main,
            font=self.__default_font,
            fg="#fff",
            bg="#2c3e50",
            textvariable=self.__screen_price_text,
            pady=6,
            padx=16
        )

        self.__screen_temp_label.grid(column=0, row=0, columnspan=9, sticky="nswe")
        self.__screen.grid(column=0, row=0, columnspan=9, rowspan=4, sticky="nswe")
        self.__screen_price.grid(column=0, row=4, columnspan=9, sticky="nswe")

    def add_buttons(self) -> None:
        """Metoda odpowiedzialna za dodanie przycisków"""

        self.__screen_buttons = [
            Button(
                self.__main,
                text=set_proper_text(i),
                font=self.__default_font,
                fg="#fff",
                bg=statics['button_color'],
                activeforeground='#fff',
                activebackground="#2c3e50",
                bd=0,
                command=lambda number=i + 1: self.choose_product(number),
                cursor="hand2"
            ) for i in range(12)  # List Comprehension
        ]

        for idx, button in enumerate(self.__screen_buttons):
            button.grid(
                row=idx // 3 + 5,
                column=idx % 3 * 3,
                columnspan=3,
                sticky="nswe"
            )

    def add_coins(self) -> None:
        """Metoda odpowiedzialna za dodanie monet"""

        self.__screen_coins = [
            Button(
                self.__main,
                text=set_proper_coin(coin),
                font=self.__default_font,
                fg="#fff",
                bg=statics['button_color'],
                activeforeground='#fff',
                activebackground="#2c3e50",
                bd=0,
                cursor="hand2"
            ) for coin in utils.coins  # List Comprehension
        ]

        for idx, coin in enumerate(self.__screen_coins):
            coin.grid(
                row=idx,
                column=9,
                columnspan=3,
                sticky="nswe"
            )

    def choose_product(self, action_number: int) -> None:
        if action_number == 10:
            self.clear_screen()
            return
        elif action_number == 12:
            if not self.__screen_current_number:
                return

            number = int(self.__screen_current_number)

            if 30 <= number <= 50:
                change_buttons_state(self.__screen_buttons, False)
                change_buttons_state(self.__screen_coins, True)
            else:
                messagebox.showerror('Error', 'Nie ma takiego produktu')
                self.clear_screen()

            return
        elif action_number == 11:
            action_number = 0

        if len(self.__screen_current_number) >= 2 or self.__screen_current_number.startswith('0'):
            self.__screen_current_number = str(action_number)
        else:
            self.__screen_current_number += str(action_number)

        self.__screen_text.set(self.__screen_current_number)

    def clear_screen(self) -> None:
        """Metoda odpowiedzialna za czyszczenie ekranu"""

        self.__screen_current_number = ''
        self.__screen_text.set(statics['default_text_screen'])
        change_buttons_state(self.__screen_buttons, True)
        change_buttons_state(self.__screen_coins, False)


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
