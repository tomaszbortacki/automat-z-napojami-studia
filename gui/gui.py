from tkinter import Tk


# Główna klasa interfejsu
class Gui:
    def __init__(self):
        self.__main = Tk()
        self.__main.title('Automat z napojami - Tomasz Bortacki - JS')
        self.__main.minsize(480, 640)
        self.__main.mainloop()


if __name__ == '__main__':
    print('Plik musi zostać zaimportowany')
else:
    pass
