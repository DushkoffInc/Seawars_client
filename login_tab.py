import threading
import sys
from registration_qt import Ui_Registration
from PyQt5 import QtWidgets
from login_qt import Ui_MainWindow
import requests



class RegistrationForm(Ui_Registration):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Registration()
        self.ui.setupUi(self)


class SeaWarsApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.login_to_server)
        self.pushButton_2.clicked.connect(self.user_registration)
        # threading.Thread(target=self.refresh).start() # можно использовать многопоточку для независимого логирования

    def login_to_server(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        payload = {'name': login, 'password': password}
        r = requests.get('http://localhost:8080/user/check', params=payload)
        if str(r) == '<Response [200]>':
            if r.text == 'NOK':
                self.textBrowser.append('Пользователя с такой связкой имени и пароля не существует!')
            else:
                self.textBrowser.append(f'{login}, добро пожаловать в игру!')
            info_to_show = f' Status: {r}.  Пользователь {login}, Пароль: {password}'
            self.textBrowser.append(info_to_show)

        elif str(r) == '<Response [500]>':
            self.textBrowser.append(f'Не все поля заполнены')
            self.textBrowser.append(f'Status: {r}')
        else:
            self.textBrowser.append(' Сервер не доступен =(')
            self.textBrowser.append('')
            self.textBrowser.append(f'Status: {r}')

        self.textBrowser.append('====================')


    def user_registration(self):
        # self.textBrowser.append('погнали регаться')
        pass





if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = SeaWarsApp()
    window.show()
    sys.exit(app.exec_())
