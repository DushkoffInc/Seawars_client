import requests
import sys
import time
import datetime
from PyQt5 import QtWidgets
import WindFromQt.xz

from WindFromQt.main_menu_window import UiMainMenuWindow
from WindFromQt.login_window import UiLogIn
from WindFromQt.registration_window import UiRegistration

name_user = None


class LoginWindow(QtWidgets.QMainWindow, UiLogIn):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login_to_server)
        self.pushButton_2.clicked.connect(self.user_registration)

    def login_to_server(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        payload = {'name': login, 'password': password}
        global name_user
        name_user = login
        print(name_user)
        if password == '' or login == '':
            self.textBrowser.append(f'Не все поля заполнены')
            return
        try:
            r = requests.get('http://localhost:8080/user/check', params=payload)

            if r.text == 'NOK':
                self.textBrowser.append(str(datetime.datetime.now()))
                self.textBrowser.append('Пользователя с такой связкой имени и пароля не существует!')
                self.textBrowser.append(r.text)
            else:
                self.mainMenu = MainMenuWindow()
                self.close()
                self.mainMenu.show()

        except requests.exceptions.ConnectionError:
            self.textBrowser.append('Сервен не доступен.')
            return
        except Exception as ex:
            self.textBrowser.append('Произошла какая-то ошибка.')
            self.textBrowser.append(f'Ошибка:{ex}')

            return

    def user_registration(self):
        self.reg_form = RegistrationForm()
        self.close()
        self.reg_form.show()


class RegistrationForm(UiRegistration, QtWidgets.QWidget):
    def __init__(self):
        super(RegistrationForm, self).__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back_to_login_tab)
        self.ok_btn.clicked.connect(self.registr_to_server)

    def back_to_login_tab(self):
        self.login_window = LoginWindow()
        self.close()
        self.login_window.show()

    def registr_to_server(self):
        self.login_window = LoginWindow()
        login = self.line_name.text()
        password = self.line_password.text()
        varif_password = self.line_varif_password.text()

        if (login == '') or (password == '') or (varif_password == ''):
            self.logsBrows.append('')
            self.logsBrows.append('====================')
            self.logsBrows.append('Заполните все поля!')

        elif len(password) < 4:
            self.logsBrows.append('')
            self.logsBrows.append('====================')
            self.logsBrows.append('Пароль слишком короткий')

        elif varif_password != password:
            self.logsBrows.append('')
            self.logsBrows.append('====================')
            self.logsBrows.append('Пароли не совпадают!')

        else:
            try:
                payload = {'name': login, 'password': password}
                r = requests.get('http://localhost:8080/user/create', params=payload)  # заменить data на create
                if str(r) == '<Response [200]>':
                    if r.text == 'NOK':
                        self.logsBrows.append('Такой пользователь уже существует')
                    else:
                        self.logsBrows.append(f'{login}, вы зарегистрированы')
                        info_to_show = f' Status: {r}.  Пользователь {login}, Пароль: {password}'
                        self.logsBrows.append(info_to_show)
                        time.sleep(1)
                        self.close()
                        self.login_window.show()

            except requests.exceptions.ConnectionError:
                self.logsBrows.append('Сервен не доступен')
                return

            except:
                self.logsBrows.append('Произошла какая-то ошибка =(')
                return


class MainMenuWindow(UiMainMenuWindow, QtWidgets.QWidget):
    def __init__(self):
        super(MainMenuWindow, self).__init__()
        self.setupUi(self)
        self.name = name_user
        self.label.setText(f"{self.name}, добро пожаловать.")
        self.new_game_btn.clicked.connect(self.create_room)
        self.join_game_btn.clicked.connect(self.going_to_lobby)

    def create_room(self):
        host_name = user_name
        create_room_request = requests.get(f'http://localhost:8080/game/createRoom/?name={host_name}')
        if create_room_request.text == 'OK':
            self.roomWind = RoomWindow()
            self.roomWind.setWindowModality(Qt.ApplicationModal)
            self.roomWind.show()

    def going_to_lobby(self):
        self.lobby = Lobby_menu_window()
        self.close()
        self.lobby.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
