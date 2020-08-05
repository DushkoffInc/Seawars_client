import sys
import time
import datetime
import requests
import threading
import json
import re
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5 import QtWidgets
from registration_qt import Ui_Registration
from login_window import Ui_MainWindow
from main_menu_window import Ui_Main_menu_window
from lobbi_window import Ui_Lobby_menu
from room_window import Ui_room
import xz

user_name = None


class RegistrationForm(Ui_Registration, QtWidgets.QWidget):
    def __init__(self):
        super(RegistrationForm, self).__init__()
        self.login_window = SeaWarsApp()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back_to_login_tab)
        self.ok_btn.clicked.connect(self.registr_to_server)

    def back_to_login_tab(self):
        self.close()
        self.login_window.show()

    def registr_to_server(self):
        self.login_window = SeaWarsApp()
        login = self.line_name.text()
        password = self.line_password.text()
        varif_password = self.line_varif_password.text()

        if (login == '') or (password == '') or (varif_password == ''):
            self.logsBrows.append('')
            self.logsBrows.append('====================')
            self.logsBrows.append('Заполните все поля!')

        elif len(password) < 5:
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


class SeaWarsApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(SeaWarsApp, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login_to_server)
        self.pushButton_2.clicked.connect(self.user_registration)

    def login_to_server(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        payload = {'name': login, 'password': password}
        global user_name
        user_name = login
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
                self.textBrowser.append(f'{login}, добро пожаловать в игру!')
                self.hide()
                self.mainMenu.show()

        except requests.exceptions.ConnectionError:
            self.textBrowser.append('Сервен не доступен.')
            return
        except:
            self.textBrowser.append(f'Произошла какая-то ошибка.')
            return

    def user_registration(self):
        self.reg_form = RegistrationForm()
        self.close()
        self.reg_form.show()


class MainMenuWindow(Ui_Main_menu_window, QtWidgets.QWidget):
    def __init__(self):
        super(MainMenuWindow, self).__init__()
        self.setupUi(self)
        global user_name
        self.label.setText(f"{user_name}, добро пожаловать.")
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


class RoomWindow(Ui_room, QtWidgets.QWidget):
    def __init__(self):
        super(RoomWindow, self).__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back_to_lobby)

    def back_to_lobby(self):
        self.close()
        self.lobby = Lobby_menu_window()
        self.lobby.listWidget.repaint()


class Lobby_menu_window(Ui_Lobby_menu, QtWidgets.QWidget):
    rooms_stack = []
    host_id = None
    def __init__(self):
        super(Lobby_menu_window, self).__init__()
        self.setupUi(self)
        self.user_name.setText(f"{user_name}, добро пожаловать.")
        self.listWidget.itemDoubleClicked.connect(self.host_id_identification)
        self.listWidget.itemDoubleClicked.connect(self.join_the_game)
        # self.listWidget.itemClicked.connect(self._on_item_clicked)
        # self.join_to_game_btn.clicked.connect(self.join_the_game)
        self.back_btn.clicked.connect(self.back_to_menu)
        self.t = threading.Thread(target=self.refresh_rooms_at_lobby)
        self.t.daemon = True
        self.t.start()

    def refresh_rooms_at_lobby(self):
        while True:
            try:
                active_rooms_list = requests.get('http://localhost:8080/game/found')
            except:
                print('Какая-то ошибка произошла')
                time.sleep(1)
                continue

            first_request = json.loads(active_rooms_list.text)
            for i, player in enumerate(first_request):
                if player not in self.rooms_stack:
                    new_item = f'id: {player["id"]},      name: {player["userHost"]}'
                    self.listWidget.addItem(new_item)
                    self.rooms_stack.append(player)

            time.sleep(0.5)
            if len(first_request) != len(self.rooms_stack):

                print(self.rooms_stack)
                self.listWidget.clear()
                self.rooms_stack.clear()
                time.sleep(0.5)

    def back_to_menu(self):
        self.mainMenu = MainMenuWindow()
        self.mainMenu.show()
        self.mainMenu.setWindowModality(Qt.ApplicationModal)

    def host_id_identification(self, item: QListWidgetItem):
        self.textBrowser.append(f'====Widget item: {item.text()}====')
        self.textBrowser.append(f'====Widget item: {item.text()}====')
        result = re.findall(r'\d+', str(item.text()))
        self.textBrowser.append(f'=====Result: {result[0]}====')
        self.host_id = int(result[0])


    # Для книпки Join
    # def _on_item_clicked(self, item: QListWidgetItem):
    #     self.textBrowser.append(f'Нажали на {item.text()}')



    def join_the_game(self):
        self.lobby = Lobby_menu_window()
        payload = {'name': user_name, 'id': self.host_id}
        try:
            request_to_join = requests.get('http://localhost:8080/game/join', params=payload)
            if request_to_join.text == 'Have fun':
                self.roomWind = RoomWindow()
                self.roomWind.setWindowModality(Qt.ApplicationModal)
                self.roomWind.show()
            else:
                self.textBrowser.append('Комната занята!')
                return

        except Exception as ex:
            print('Метод "Join the game"')
            print('Произошла какая-то ошибка =(')
            print(f'Ошибка: {ex}')
            return
        self.textBrowser.append(f'Host id:  {self.host_id}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SeaWarsApp()
    window.show()
    sys.exit(app.exec_())




