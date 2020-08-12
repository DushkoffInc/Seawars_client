import sys
import requests
from PyQt5 import QtWidgets
from WindFromQt.room_window import Ui_RoomUi
import login_registration_menu

from PyQt5.QtWidgets import (
    QApplication, QWidget, QToolTip, QPushButton, QMessageBox)
from PyQt5.QtCore import QCoreApplication, Qt

class NewRoomWindow(Ui_RoomUi, QtWidgets.QWidget):
    def __init__(self):
        super(NewRoomWindow, self).__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back_to_menu)

    def back_to_menu(self):
        login = user_name
        id = 12
        print(login, id )
            #
            # leave_room_request = requests.get(f'http://localhost:8080/game/leave', params=payload)

        #     if create_room_request.text == 'OK':
        #         self.roomWind = RoomWindow()
        #         self.roomWind.setWindowModality(Qt.ApplicationModal)
        #         self.roomWind.show()
        #         self.roomWind.label_2.setText(f"{self.name}, вы Хост")
        #         self.roomWind.textBrowser.append('Ожидайте второго игрока.')
        #     if create_room_request.text == 'NOK':
        #         print('Вы не можете создать новую комнату!')
        # self.close()




class RoomWindow(Ui_RoomUi, QtWidgets.QWidget):
    def __init__(self):
        super(RoomWindow, self).__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back_to_lobby)

    def back_to_lobby(self):
        self.close()

    def closeEvent(self, event):
        print('Вы вышли из проложения!')
        params = {'name': 'TESTER', 'gameId': 11}
        r = requests.get('http://localhost:8080/game/leave', params = params)
        print(r.text)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window2 = RoomWindow()
    window2.show()
    sys.exit(app.exec_())
