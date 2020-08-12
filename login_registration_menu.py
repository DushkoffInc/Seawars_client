import requests
import sys
import time
import datetime
import threading
import re
import json
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem
import WindFromQt.xz  # Для визуального оформления окошка Log-in
from WindFromQt.main_menu_window import UiMainMenuWindow
from WindFromQt.login_window import UiLogIn
from WindFromQt.registration_window import UiRegistration
from WindFromQt.room_window import Ui_RoomUi
from WindFromQt.lobby_window import Ui_Lobby_menu

import get_field_and_save_field as gf_sf
import property as prop

name_user = None
game_id = None


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
            user_check = prop.user_check_request
            r = requests.get(user_check, params=payload)

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
                user_create = prop.user_create_request
                payload = {'name': login, 'password': password}
                r = requests.get(user_create, params=payload)
                if str(r) == '<Response [200]>':
                    if r.text == 'NOK':
                        self.logsBrows.append('Такой пользователь уже существует')
                    else:
                        self.logsBrows.append(f'{login}, вы зарегистрированы')
                        info_to_show = f' Status: {r}.  Пользователь {login}, Пароль: {password}'
                        self.logsBrows.append(info_to_show)
                        time.sleep(0.4)
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
        host_name = name_user
        try:
            payload = {'name': host_name}
            create_room = prop.game_create_room
            create_room_request = requests.get(create_room, params=payload)

            if create_room_request.text == 'OK':
                self.roomWind = NewRoomWindow()
                self.roomWind.setWindowModality(Qt.ApplicationModal)
                self.roomWind.show()
                self.roomWind.label_2.setText(f"{self.name}, вы Хост")
                self.roomWind.info_browser.append('Ожидайте второго игрока.')
            if create_room_request.text == 'NOK':
                print('Вы не можете создать новую комнату!')
        except Exception as ex:
            print(f'Произошла ошибка ===>  {ex}  <===, сервер не доступен')

    def going_to_lobby(self):
        self.lobby = Lobby_menu_window()
        self.close()
        self.lobby.show()


class NewRoomWindow(Ui_RoomUi, QtWidgets.QWidget):
    def __init__(self):
        super(NewRoomWindow, self).__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back_to_menu)
        self.enter_btn.clicked.connect(self.enter_data)
        self.t = threading.Thread(target=self.update_game)
        self.t.daemon = True
        self.t.start()

        self.get_field = gf_sf.get_field_for_user(name_user, game_id)


    def enter_data(self):
        self.info_browser.clear()
        data = self.game_line.text()
        self.info_browser.append(f'Вы ввели: {data}')



    def back_to_menu(self):
        self.close()

    def game_id(self):
        try:
            game_found = prop.game_found
            active_rooms_list = requests.get(game_found)

            first_request = json.loads(active_rooms_list.text)
            for i, player in enumerate(first_request):
                if player['userHost']['name'] == name_user:
                    global game_id
                    game_id = player['id']
                    print(f'Ваша игра: {game_id}')
        except:
            print('Ошибка!')

    def closeEvent(self, event):
        print('Вы вышли из приложения!')
        self.name = name_user
        payload = {'name': self.name, 'gameId': game_id}
        game_leave = prop.game_leave
        r = requests.get(game_leave, params=payload)
        print(r.text)

    def update_game(self):
        self.game_id()
        self.check_text_to_rooms = None
        self.second_user_name = None

        while True:
            self.show_time = time.strftime("%H:%M:%S", time.localtime())
            try:
                self.params = {'gameId': game_id}
                update_game = prop.game_update_game
                self.request_to_update = requests.get(update_game, params=self.params)
                self.request_to_update_json = json.loads(self.request_to_update.text)
                if self.check_text_to_rooms != str(self.request_to_update_json):
                    self.check_text_to_rooms = str(self.request_to_update_json)
                    self.text_to_rooms = self.request_to_update_json
                    if self.text_to_rooms['secondUser'] is not None:
                        self.info_browser.append(
                            f'{self.show_time}: К Вам подключился >> {self.text_to_rooms["secondUser"]["name"]} <<')
                        self.second_user_name = self.text_to_rooms['secondUser']['name']
                    else:
                        if self.second_user_name == None:
                            self.info_browser.append(
                                f'{self.show_time}: ID вашей игры: {self.text_to_rooms["id"]}, Вы один в комнате.')
                        else:
                            self.info_browser.append(
                                f'{self.show_time}: >> {self.text_to_rooms["id"]} <<:  отключился, Вы один в комнате.')

                print('Начало обновление игры')
                time.sleep(0.5)
            except Exception as ex:
                self.info_browser.append(f'Ошибка! , {ex}')
                time.sleep(1)


class RoomWindow(Ui_RoomUi, QtWidgets.QWidget):
    def __init__(self):
        super(RoomWindow, self).__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back_to_lobby)
        self.t = threading.Thread(target=self.update_game)
        self.name = name_user
        self.label_2.setText(f"{self.name}, вы Join")
        self.t.daemon = True
        self.t.start()

    def back_to_lobby(self):
        self.close()

    def closeEvent(self, event):
        print('Вы вышли из проложения!')
        params = {'name': name_user, 'gameId': game_id}
        game_leave = prop.game_leave
        r = requests.get(game_leave, params=params)
        print(r.text)

    def update_game(self):
        self.check_text_to_rooms = None
        self.second_user_name = None

        self.show_time = time.strftime("%H:%M:%S", time.localtime())
        try:
            self.params = {'gameId': game_id}
            game_update = prop.game_update_game
            self.request_to_update = requests.get(game_update, params=self.params)
            self.request_to_update_json = json.loads(self.request_to_update.text)
            self.text_to_rooms = self.request_to_update_json
            self.textBrowser.append(
                f'{self.show_time}.:   Вы подключились к игре ID:{self.text_to_rooms["id"]}, имя хоста'
                f' >> {self.text_to_rooms["userHost"]["name"]} <<')
            print('Начало обновление игры')
        except Exception as ex:
            self.textBrowser.append(f'Ошибка! , {ex}')
            time.sleep(1)


class Lobby_menu_window(Ui_Lobby_menu, QtWidgets.QWidget):
    rooms_stack = []

    def __init__(self):
        super(Lobby_menu_window, self).__init__()
        self.setupUi(self)
        self.user_name.setText(f"{name_user}, добро пожаловать.")
        self.listWidget.itemDoubleClicked.connect(self.host_id_identification)
        self.listWidget.itemDoubleClicked.connect(self.join_the_game)
        # self.listWidget.itemClicked.connect(self._on_item_clicked)
        # self.join_to_game_btn.clicked.connect()
        self.refresh_btn.clicked.connect(self.refresh_rooms_at_lobby)
        self.back_btn.clicked.connect(self.back_to_menu)
        # self.t = threading.Thread(target=self.refresh_rooms_at_lobby)
        # self.t.daemon = True
        # self.t.start()

    def refresh_rooms_at_lobby(self):
        self.listWidget.clear()
        self.rooms_stack.clear()
        try:
            game_found = prop.game_found
            active_rooms_list = requests.get(game_found)

            first_request = json.loads(active_rooms_list.text)
            for i, player in enumerate(first_request):
                if player not in self.rooms_stack:
                    new_item = f'Game Id: {player["id"]},      Host Name: {player["userHost"]["name"]}'
                    self.listWidget.addItem(new_item)
                    self.rooms_stack.append(player)

        except:
            self.textBrowser.append('Какая-то ошибка произошла =(')
            print('Какая-то ошибка произошла')
            time.sleep(1)

    def back_to_menu(self):
        self.mainMenu = MainMenuWindow()
        self.mainMenu.show()
        self.mainMenu.setWindowModality(Qt.ApplicationModal)

    def host_id_identification(self, item: QListWidgetItem):
        self.textBrowser.append(f'====Widget item: {item.text()}====')
        self.textBrowser.append(f'====Widget item: {item.text()}====')
        result = re.findall(r'\d+', str(item.text()))
        self.textBrowser.append(f'=====Result: {result[0]}====')
        global game_id
        game_id = int(result[0])
        print(f'Метод Host_id_identification: {game_id}')

    # Для кнопки Join
    # def _on_item_clicked(self, item: QListWidgetItem):
    #     self.textBrowser.append(f'Нажали на {item.text()}')

    def join_the_game(self):
        self.lobby = Lobby_menu_window()
        payload = {'name': name_user, 'id': game_id}
        try:
            game_join = prop.game_join
            request_to_join = requests.get(game_join, params=payload)
            if request_to_join.text == 'OK':
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
        self.textBrowser.append(f'Host id:  {game_id}')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
