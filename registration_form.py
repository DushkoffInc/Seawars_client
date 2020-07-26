
import time
from registration_qt import Ui_Registration
from PyQt5 import QtWidgets

class RegistrationForm(Ui_Registration, QtWidgets.QWidget):
    def __init__(self):
        super(RegistrationForm, self).__init__()
        self.setupUi(self)
        self.back_btn.clicked.connect(self.back_to_login_tab)
        self.ok_btn.clicked.connect(self.registr_to_server)

    def back_to_login_tab(self):
        self.close()
        self.login_window = SeaWarsApp()
        self.login_window.show()

    def registr_to_server(self):
        self.login_window = SeaWarsApp()
        login = self.line_name.text()
        password = self.line_password.text()
        varif_password = self.line_varif_password.text()

        print(type(login), password, varif_password)


        if (login == '' ) or (password == '') or (varif_password == ''):
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

            payload = {'name': login, 'password': password}
            r = requests.get('http://localhost:8080/user/data', params=payload)
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