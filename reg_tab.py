import tkinter as tk
from tkinter import *


class Main(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        pass

    def open_dialog(self):
        pass
        Child()

def clicked():
    print('Начата рагистрация пользователя')
    window_new = Tk()
    window_new.mainloop()
    print('Начата рагистрация пользователя')

window = tk.Tk()

window.title("Добро пожаловать в seaWars")
window.geometry('400x250')

#поле 'логин'
login = Label(window, text="Логин  ", font=("balthazar", 20))
login.grid(column=0, row=0)
txt_field_login = Entry(window,width=17)
txt_field_login.grid(column=1, row=0)

#поле 'пароль'
password = Label(window, text="  Пароль  ", font=("balthazar", 20))
password.grid(column=0, row=1)
txt_field_password = Entry(window,width=17)
txt_field_password.grid(column=1, row=1)

#кнопка входа
registration_button = Button(window, text="Войти", bg="black", fg="lightblue")
registration_button.grid(column=0, row=4)

#кнопка регистрации
entry_button = Button(window, text="Зарегистрироваться", bg="grey", fg="yellow", command=clicked)
entry_button.grid(column=1, row=4)


def main():
    window.mainloop()


if __name__ == '__main__':
    main()