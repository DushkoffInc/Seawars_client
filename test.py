from tkinter import *

root = Tk()


w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
w = w//2 # середина экрана
h = h//2
w = w - 200 # смещение от середины
h = h - 200

def logining():
    a = txt_field_login.get()
    print(f"Пользователь, =__{a}=__  вошёл")


def clicked():
    registration_wind = Toplevel()
    print('Начата рагистрация пользователя')

    w = registration_wind.winfo_screenwidth()  # ширина экрана
    h = registration_wind.winfo_screenheight()  # высота экрана
    w = w // 2  # середина экрана
    h = h // 2
    w = w - 200  # смещение от середины
    h = h - 200

    registration_wind.title("Регистрация")
    registration_wind.geometry('400x400+{}+{}'.format(w, h))
    registration_wind.resizable(False, False)

    registration_wind.grab_set()
    registration_wind.focus_set()
    registration_wind.wait_window()

    registration_wind.mainloop()






root.title("SeaWars")
root.geometry('400x400+{}+{}'.format(w, h))
root.resizable(False, False)


#поле 'логин'
login = Label(root, text="Логин  ", font=("balthazar", 20))
login.grid(column=0, row=0)
txt_field_login = Entry(root,width=17)
txt_field_login.grid(column=1, row=0)

#поле 'пароль'
password = Label(root, text="  Пароль  ", font=("balthazar", 20))
password.grid(column=0, row=1)
txt_field_password = Entry(root,width=17)
txt_field_password.grid(column=1, row=1)

#кнопка входа
registration_button = Button(root, text="Войти", bg="black", fg="lightblue", command=logining)
registration_button.grid(column=0, row=4)

#кнопка регистрации
entry_button = Button(root, text="Зарегистрироваться", bg="grey", fg="yellow", command=clicked)
entry_button.grid(column=1, row=4)



root.mainloop()
