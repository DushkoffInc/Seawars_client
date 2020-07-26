# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Qtfiles/login_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/back lighthouse.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 180, 209, 30))
        self.frame.setMinimumSize(QtCore.QSize(209, 30))
        self.frame.setMaximumSize(QtCore.QSize(209, 30))
        self.frame.setStyleSheet("background-image: url(:/newPrefix/white back.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 209, 30))
        self.lineEdit.setMinimumSize(QtCore.QSize(209, 30))
        self.lineEdit.setStyleSheet("background-color: rgb(51,122,183); color: black; border-radius: 4px;")
        self.lineEdit.setMaxLength(32766)
        self.lineEdit.setObjectName("lineEdit")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 220, 209, 30))
        self.frame_2.setMinimumSize(QtCore.QSize(209, 30))
        self.frame_2.setMaximumSize(QtCore.QSize(209, 30))
        self.frame_2.setStyleSheet("background-image: url(:/newPrefix/white back.jpg);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 0, 209, 30))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(209, 30))
        self.lineEdit_2.setStyleSheet("background-color: rgb(51,122,183); color: black; border-radius: 4px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 260, 91, 23))
        self.pushButton.setStyleSheet("color: black; \n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 260, 91, 23))
        self.pushButton_2.setStyleSheet("color: black; \n"
"border-radius: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 70, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Californian FB")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(22, 96, 135);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 340, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-image: url(:/newPrefix/white back.jpg);color: black; border-radius: 4px;")
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(110, 340, 481, 51))
        self.textBrowser.setStyleSheet("background-image: url(:/newPrefix/white back.jpg);color: black; border-radius: 4px;")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.pushButton_2.showMenu)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Ваше имя"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.pushButton.setText(_translate("MainWindow", "Вход"))
        self.pushButton_2.setText(_translate("MainWindow", "Регистрация"))
        self.label.setText(_translate("MainWindow", "    SeaWars"))
        self.label_2.setText(_translate("MainWindow", "Check and logs:"))
# import xz_rc
